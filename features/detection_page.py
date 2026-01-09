from features.base_page import BasePage
import streamlit as st
import os
from utils.prediction import load_model, predict_image
from utils.report import generate_pdf
from PIL import Image

class DetectionPage(BasePage):
    def __init__(self, model_path, class_names):
        super().__init__("Disease Detection")
        self.model_path = model_path
        self.class_names = class_names

    def render(self):
        st.title("🔍 Disease Detection")
        st.write("Upload an image of a rice or pulse leaf to detect diseases.")

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
            
            # Predict Button
            if st.button("Predict Disease", disabled=(model is None)):
                if model is None:
                    st.error("Model is not available.")
                else:
                    with st.spinner('Analyzing...'):
                        predicted_class, confidence = predict_image(model, uploaded_file, self.class_names)
                        
                        if predicted_class:
                            st.success(f"Prediction: **{predicted_class}**")
                            st.info(f"Confidence: **{confidence:.2f}%**")
                            
                            # Custom feedback based on disease
                            if predicted_class == 'Healthy':
                                st.balloons()
                                st.markdown("### ✅ The plant looks healthy!")
                            else:
                                st.markdown(f"### ⚠️ Detected: {predicted_class}")
                                st.markdown("Please consult an agricultural expert for treatment.")
                            
                            # PDF Report Generation
                            st.markdown("---")
                            st.write("### 📄 Report")
                            
                            # Convert uploaded file to PIL Image for the report generator
                            # Seeking to 0 is important if the file has been read before
                            uploaded_file.seek(0)
                            image_pil = Image.open(uploaded_file)
                            
                            if st.button("Generate PDF Report"):
                                with st.spinner("Generating PDF..."):
                                    pdf_bytes = generate_pdf(image_pil, predicted_class, confidence)
                                    
                                    st.download_button(
                                        label="⬇️ Download PDF Result",
                                        data=pdf_bytes,
                                        file_name="disease_report.pdf",
                                        mime="application/pdf"
                                    )
                        else:
                            st.error("Could not make a prediction. Please try another image.")
