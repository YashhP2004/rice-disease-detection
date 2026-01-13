from features.base_page import BasePage
import streamlit as st
import pandas as pd
from utils.history_manager import HistoryManager

class HistoryPage(BasePage):
    def __init__(self):
        super().__init__("History")
        self.history_manager = HistoryManager()

    def render(self):
        st.title("🕒 Prediction History")
        
        # Check login
        if 'current_user' not in st.session_state or not st.session_state['current_user']:
            st.error("Please login to view history.")
            return

        username = st.session_state['current_user']
        df = self.history_manager.get_analytics(username)
        
        if df is None or df.empty:
            st.info("No prediction history found. Go to 'Disease Detection' to run your first scan!")
            return

        # Top Analytics Section
        st.markdown("### 📊 Analytics Overview")
        c1, c2 = st.columns(2)
        
        with c1:
            st.markdown("#### Disease Distribution")
            chart_data = df['disease'].value_counts()
            st.bar_chart(chart_data)
            
        with c2:
            st.markdown("#### Recent Activity")
            # Convert timestamp to datetime for better sorting/display if needed
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            st.line_chart(df.set_index('timestamp')['confidence'])

        # Detailed Table
        st.markdown("---")
        st.markdown("### 📜 Scan Log")
        
        # Formatting for display
        display_df = df.copy()
        display_df = display_df[['timestamp', 'disease', 'confidence', 'image_name']]
        display_df = display_df.sort_values(by='timestamp', ascending=False)
        
        st.dataframe(
            display_df,
            column_config={
                "timestamp": "Date & Time",
                "disease": "Detected Disease",
                "confidence": st.column_config.NumberColumn("Confidence (%)", format="%.2f%%"),
                "image_name": "Image File"
            },
            hide_index=True,
            use_container_width=True
        )
