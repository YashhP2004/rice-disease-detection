def get_login_css():
    return """
    <style>
        /* Global Reset & Font */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        /* Abstract Modern Background */
        .stApp {
            /* Sleek dark gradient background */
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
        }
        
        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Main Glass Card Container */
        div[data-testid="column"] {
            background: rgba(18, 18, 18, 0.85); /* Darker for better contrast */
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
            padding: 50px;
        }

        /* Left Column (Forms) */
        div[data-testid="column"]:nth-of-type(1) {
            border-top-left-radius: 20px;
            border-bottom-left-radius: 20px;
            border-right: 1px solid rgba(255,255,255,0.05); /* Subtle separator */
        }

        /* Right Column (Branding) */
        div[data-testid="column"]:nth-of-type(2) {
            border-top-right-radius: 20px;
            border-bottom-right-radius: 20px;
            background: linear-gradient(135deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01));
            display: flex;
            align-items: center;
            justify-content: center;
        }

        /* Typography */
        h1, h2, h3 {
            color: #FFFFFF !important;
            font-weight: 700 !important;
            letter-spacing: -0.5px;
        }

        p, label, .stMarkdown {
            color: #A0A0A0 !important;
            font-weight: 400;
        }

        /* Modern Input Fields */
        .stTextInput > div > div > input {
            background-color: #1E1E1E;
            color: #E0E0E0;
            border: 1px solid #333;
            border-radius: 12px;
            padding: 12px 16px;
            font-size: 14px;
            transition: all 0.3s ease;
        }

        .stTextInput > div > div > input:focus {
            border-color: #764ba2; /* Purple accent */
            box-shadow: 0 0 0 2px rgba(118, 75, 162, 0.2);
            background-color: #252525;
        }

        /* Primary Button (Login/Sign Up) */
        .stButton > button {
            width: 100%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); /* Modern Purple-Blue Gradient */
            color: white;
            border: none;
            padding: 14px 0;
            border-radius: 12px;
            font-weight: 600;
            font-size: 15px;
            letter-spacing: 0.5px;
            box-shadow: 0 4px 15px rgba(118, 75, 162, 0.4);
            transition: all 0.3s ease;
        }

        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(118, 75, 162, 0.6);
        }
        
        .stButton > button:active {
            transform: translateY(0px);
        }
        
        /* Secondary Button behavior (Simulated via CSS targeting if possible, 
           or just generalized since Streamlit buttons are same class. 
           We'll make the "Don't have an account?" look distinct if we can, 
           or keep them consistent but separated by spacing.
           For now, the gradient style works well for the primary action. 
           The 'type="secondary"' in Streamlit doesn't add a distinct class we can easily hook 
           without :nth-child hacks, so we'll stick to a consistent premium button style.
        */

        /* Hide Default Streamlit Chrome */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Alerts */
        .stAlert {
            background-color: rgba(255, 75, 75, 0.1);
            border: 1px solid rgba(255, 75, 75, 0.2);
            color: #ff4b4b;
            border-radius: 10px;
        }
        
        .stSuccess {
            background-color: rgba(0, 200, 83, 0.1);
            border: 1px solid rgba(0, 200, 83, 0.2);
            color: #00c853;
        }

    </style>
    """
