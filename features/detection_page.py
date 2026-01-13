from features.base_page import BasePage
import streamlit as st
import os
from utils.prediction import load_model, predict_image
from utils.report import generate_pdf
from utils.report import generate_pdf
from PIL import Image
import json
from utils.login_styles import get_main_app_css # Re-using styling if needed
from utils.history_manager import HistoryManager

class DetectionPage(BasePage):
    def __init__(self, model_path, class_names):
        super().__init__("Disease Detection")
        self.model_path = model_path
        self.class_names = class_names
        self.history_manager = HistoryManager()

    def render(self):
        st.title("🔍 Disease Detection")
        st.write("Upload an image of a rice or pulse leaf to detect diseases.")
        
        # Load Disease Info
        try:
            with open('utils/disease_info.json', 'r') as f:
                self.disease_info = json.load(f)
        except Exception as e:
            st.error(f"Error loading disease info: {e}")
            self.disease_info = {}

        # Check if model exists
        if not os.path.exists(self.model_path):
            st.error(f"Model file '{self.model_path}' not found. Please train the model first.")
            st.info("You can run the training script `train_model.py` to generate the model.")
            return

        # Load Model
        # Note: In a production app, we should use st.cache_resource for the model
        # But staying true to the original request of "without changing functionality" 
        # (and assuming original behavior was acceptable), we keep the loading logic similar 
        # but encapsulated here.
        model = load_model(self.model_path)
        if model is None:
            st.warning("⚠️ Model could not be loaded (TensorFlow missing or model file not found). Prediction is disabled.")
        
        # File Uploader
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            # Display Image
            st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
            
            # Use session_state to persist prediction results across reruns (e.g. when clicking download)
            # We use the filename to ensure we clear results if a new file is uploaded
            if 'last_uploaded_file' not in st.session_state or st.session_state.get('last_uploaded_file') != uploaded_file.name:
                st.session_state.prediction_result = None
                st.session_state.last_uploaded_file = uploaded_file.name

            # Predict Button
            if st.button("Predict Disease", disabled=(model is None)):
                if model is None:
                    st.error("Model is not available.")
                else:
                    with st.spinner('Analyzing...'):
                        predicted_class, confidence = predict_image(model, uploaded_file, self.class_names)
                        
                        if predicted_class:
                           st.session_state.prediction_result = {
                               'class': predicted_class,
                               'confidence': confidence
                           }
                           
                           # Save to History
                           if 'current_user' in st.session_state and st.session_state['current_user']:
                               self.history_manager.save_prediction(
                                   st.session_state['current_user'],
                                   predicted_class,
                                   confidence,
                                   uploaded_file.name
                               )
                               
                        else:
                            st.error("Could not make a prediction. Please try another image.")

            # Display Results (Persistent Block)
            if st.session_state.get('prediction_result'):
                result = st.session_state.prediction_result
                predicted_class = result['class']
                confidence = result['confidence']

                st.success(f"Prediction: **{predicted_class}**")
                st.info(f"Confidence: **{confidence:.2f}%**")
                
                # Custom feedback based on disease
                if predicted_class == 'Healthy':
                    if 'balloons_shown' not in st.session_state or st.session_state.balloons_shown != uploaded_file.name:
                         st.balloons()
                         st.session_state.balloons_shown = uploaded_file.name
                    st.markdown("### ✅ The plant looks healthy!")
                    st.info("Keep maintaining good agricultural practices.")
                else:
                    st.markdown(f"### ⚠️ Detected: {predicted_class}")
                    st.markdown("Please consult an agricultural expert for treatment.")
                
                # --- Detailed Disease Info ---
                if predicted_class in self.disease_info:
                    info = self.disease_info[predicted_class]
                    
                    st.markdown("---")
                    st.markdown("### 📋 Detailed Analysis")
                    
                    c1, c2, c3 = st.columns(3)
                    
                    with c1:
                        with st.container():
                            st.markdown("#### 🤒 Symptoms")
                            for s in info.get('symptoms', []):
                                st.markdown(f"- {s}")
                                
                    with c2:
                        with st.container():
                            st.markdown("#### 💊 Cure / Treatment")
                            for c in info.get('cure', []):
                                st.markdown(f"- {c}")

                    with c3:
                        with st.container():
                            st.markdown("#### 🛡️ Prevention")
                            for p in info.get('prevention', []):
                                st.markdown(f"- {p}")
                # -----------------------------
                
                # PDF Report Generation
                st.markdown("---")
                st.write("### 📄 Report")
                
                # Convert uploaded file to PIL Image for the report generator
                uploaded_file.seek(0)
                image_pil = Image.open(uploaded_file)
                
                # Direct download button (no intermediate "Generate" button needed)
                # We generate the bytes on the fly for the current result
                # Direct download button (no intermediate "Generate" button needed)
                # We generate the bytes on the fly for the current result
                # Pass the detailed info to the report generator
                details = self.disease_info.get(predicted_class, {})
                pdf_bytes = generate_pdf(image_pil, predicted_class, confidence, details)
                
                st.download_button(
                    label="⬇️ Download PDF Result",
                    data=pdf_bytes,
                    file_name="disease_report.pdf",
                    mime="application/pdf"
                )
