def get_login_css():
    return """
    <style>
        /* Global Reset & Font */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
        }

        /* Animated Background */
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1550684848-fac1c5b4e853?q=80&w=2670&auto=format&fit=crop");
            background-size: cover;
            background-position: center;
        }
        
        /* Dark overlay for better text contrast if needed */
        .stApp::before {
            content: "";
            position: absolute;
            top: 0; 
            left: 0;
            width: 100%; 
            height: 100%;
            background: rgba(0, 0, 0, 0.4);
            pointer-events: none;
            z-index: 0;
        }

        /* Main Container - The "Glass Card" Wrapper 
           We will target the specific block where we put our columns. 
           In Streamlit, this is a bit tricky, but we can target the block by hierarchy.
        */
        
        div[data-testid="column"] {
            background: rgba(20, 20, 20, 0.6);
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 40px;
        }

        /* Left Column Specifics (Login Form) */
        div[data-testid="column"]:nth-of-type(1) {
            border-top-left-radius: 25px;
            border-bottom-left-radius: 25px;
            border-right: none;
        }

        /* Right Column Specifics (Testimonial/Branding) */
        div[data-testid="column"]:nth-of-type(2) {
            border-top-right-radius: 25px;
            border-bottom-right-radius: 25px;
            border-left: none;
            background: linear-gradient(135deg, rgba(0,0,0,0.8), rgba(20,20,20,0.9));
            display: flex;
            align-items: center;
            justify-content: center;
        }

        /* Headings */
        h1, h2, h3 {
            color: #FFFFFF !important;
            font-weight: 700 !important;
        }

        p, label {
            color: #d0d0d0 !important;
        }

        /* Input Fields */
        .stTextInput > div > div > input {
            background-color: #1a1a1a;
            color: white;
            border: 1px solid #333;
            border-radius: 30px; /* Pill shape */
            padding: 12px 20px;
        }

        .stTextInput > div > div > input:focus {
            border-color: #e73c7e;
            box-shadow: 0 0 10px rgba(231, 60, 126, 0.3);
        }

        /* Button Styling */
        .stButton > button {
            width: 100%;
            background: linear-gradient(90deg, #ff8a00, #e52e71);
            border: none;
            color: white;
            padding: 12px 0;
            border-radius: 30px;
            font-weight: 600;
            font-size: 16px;
            transition: transform 0.2s;
        }

        .stButton > button:hover {
            transform: scale(1.05);
            color: white;
        }

        /* Links / Toggle Text */
        .auth-toggle {
            text-align: center;
            margin-top: 15px;
            font-size: 0.9em;
            color: #aaa;
            cursor: pointer;
        }
        
        .auth-toggle:hover {
            color: #fff;
            text-decoration: underline;
        }

        /* Hide Streamlit Elements */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    """
