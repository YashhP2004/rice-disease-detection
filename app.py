import streamlit as st
import os
from auth_manager import AuthManager
from features.home_page import HomePage
from features.detection_page import DetectionPage
from features.about_page import AboutPage

from features.page_registry import PageRegistry
from utils.login_styles import get_login_css, get_main_app_css

# Constants configuration
MODEL_PATH = 'rice_leaf_disease_model.h5'
# Define class names EXACTLY as they appeared in training
CLASS_NAMES = [
    'Bacterial_Leaf_Blight',
    'Brown_Spot',
    'Healthy',
    'Leaf_Blast',
    'Leaf_Scald',
    'Sheath_Blight'
]

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Rice & Pulse Disease Detection",
        page_icon="🌿",
        layout="wide"
    )

    # Inject Global Custom CSS (Theme)
    st.markdown(get_main_app_css(), unsafe_allow_html=True)

    # Initialize Managers
    auth_manager = AuthManager()
    page_registry = PageRegistry()



    # Register Pages (Composition Root Configuration)
    page_registry.register("Home", HomePage())
    page_registry.register("Disease Detection", DetectionPage(MODEL_PATH, CLASS_NAMES))
    page_registry.register("About", AboutPage())

    # Authentication Check
    if not auth_manager.is_logged_in():
        # Inject Login-Specific CSS (Glass Card Layout)
        st.markdown(get_login_css(), unsafe_allow_html=True)
        
        # Initialize auth mode state
        if 'auth_mode' not in st.session_state:
            st.session_state.auth_mode = 'login'

        # Create Layout: Two columns for Split Screen
        # Use an empty container to center if needed, but for now we rely on CSS
        col1, col2 = st.columns([1, 1], gap="small")
        
        with col1:
            if st.session_state.auth_mode == 'login':
                st.markdown("<h2>Welcome back</h2>", unsafe_allow_html=True)
                st.markdown("<p>Please Enter your Account details</p>", unsafe_allow_html=True)
                
                username = st.text_input("Username", key="login_user")
                password = st.text_input("Password", type="password", key="login_pass")
                
                if st.button("Sign in"):
                    if auth_manager.login(username, password):
                        st.success("Logged in successfully!")
                        st.rerun()
                    else:
                        st.error("Invalid credentials")
                
                if st.button("Don't have an account? Sign Up", type="secondary"):
                    st.session_state.auth_mode = 'signup'
                    st.rerun()
            
            else: # Signup Mode
                st.markdown("<h2>Create Account</h2>", unsafe_allow_html=True)
                st.markdown("<p>Join us today!</p>", unsafe_allow_html=True)
                
                new_user = st.text_input("Username", key="signup_user")
                new_pass = st.text_input("Password", type="password", key="signup_pass")
                confirm_pass = st.text_input("Confirm Password", type="password", key="signup_confirm")
                
                if st.button("Sign Up"):
                    if new_pass != confirm_pass:
                        st.error("Passwords do not match")
                    elif len(new_pass) < 4:
                        st.error("Password must be at least 4 characters")
                    else:
                        success, msg = auth_manager.register(new_user, new_pass)
                        if success:
                            st.success(msg)
                            st.rerun()
                        else:
                            st.error(msg)
                
                if st.button("Already have an account? Sign In", type="secondary"):
                    st.session_state.auth_mode = 'login'
                    st.rerun()

        with col2:
            # Right side branding / testimonial
            st.markdown("""
            <div style="padding: 20px; color: white;">
                <h2>What's our Farmers Said.</h2>
                <br>
                <div style="font-style: italic; font-size: 1.1em;">
                "This tool has revolutionized how we detect disease in our crops. 
                Fast, accurate, and easy to use."
                </div>
                <br>
                <div style="font-weight: bold;">- Rajesh Kumar</div>
                <div style="font-size: 0.9em; opacity: 0.8;">Lead Farmer, Punjab</div>
                <br><br>
                <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 15px;">
                    <div style="font-weight: bold;">Trusted by 500+ Farmers</div>
                    <div style="font-size: 0.8em;">Join the community today.</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        return

    # Sidebar Navigation
    st.sidebar.title("Navigation")
    if st.sidebar.button("Logout"):
        auth_manager.logout()
        st.rerun()
        
    app_mode = st.sidebar.selectbox("Choose the app mode", page_registry.get_titles())

    # Render Active Page
    current_page = page_registry.get_page(app_mode)
    if current_page:
        current_page.render()

    # Inject Bot in Sidebar (at the bottom)
    with st.sidebar:
        st.markdown("---")
        # Header removed to avoid double-titles (Botpress has its own)
        from utils.bot import inject_bot
        inject_bot()

if __name__ == "__main__":
    main()
