def get_login_css():
    return """
    <style>
        /* Global Reset & Font */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
        }

        /* Animated Background */
        .stApp {
            background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
        }

        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Center the Login Form */
        /* We'll use a specific container strategy in app.py to wrap content, 
           but generally we want the main block to be centered if possible.
           Streamlit puts everything in a block we can target slightly generally. */
        
        div[data-testid="stVerticalBlock"] > div:has(div.stTextInput) {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.18);
            padding: 40px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            max-width: 500px;
            margin: auto;
            margin-top: 50px;
        }

        /* Title Styling */
        h1 {
            color: #FFFFFF !important;
            text-align: center;
            font-weight: 700 !important;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            margin-bottom: 2rem !important;
        }

        /* Input Fields */
        .stTextInput > div > div > input {
            background-color: rgba(255, 255, 255, 0.1);
            color: white;
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            padding: 10px 15px;
            transition: all 0.3s ease;
        }

        .stTextInput > div > div > input:focus {
            background-color: rgba(255, 255, 255, 0.2);
            border-color: #ffffff;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
        }

        .stTextInput label {
            color: #e0e0e0 !important;
            font-weight: 500;
        }

        /* Button Styling */
        .stButton > button {
            width: 100%;
            background: linear-gradient(45deg, #FF512F 0%, #DD2476 51%, #FF512F 100%);
            background-size: 200% auto;
            color: white;
            padding: 12px 30px;
            border-radius: 50px;
            border: none;
            font-weight: 600;
            letter-spacing: 1px;
            text-transform: uppercase;
            transition: all 0.5s;
            box-shadow: 0 4px 15px 0 rgba(221, 36, 118, 0.75);
        }

        .stButton > button:hover {
            background-position: right center;
            transform: scale(1.02);
            box-shadow: 0 6px 20px 0 rgba(221, 36, 118, 0.9);
        }

        /* Hide Streamlit Elements */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
    </style>
    """
