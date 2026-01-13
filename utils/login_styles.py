def get_main_app_css():
    """Returns CSS that should be applied globally to the app"""
    return """
    <style>
        /* Global Reset & Font */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            color: #E0E0E0;
        }

        /* Abstract Modern Background - GLOBAL */
        .stApp {
            /* Sleek dark gradient background */
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            background-attachment: fixed;
        }
        
        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Sidebar Styling */
        section[data-testid="stSidebar"] {
            background: rgba(10, 10, 15, 0.7);
            backdrop-filter: blur(15px);
            border-right: 1px solid rgba(255, 255, 255, 0.05);
        }
        
        /* Botpress Iframe Styling */
        iframe[title="st.iframe"] {
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 4px 20px rgba(0,0,0,0.4);
            background-color: rgba(20, 20, 25, 0.8) !important; /* Attempt to blend before load */
        }
        
        section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] label {
            color: #ffffff !important;
        }

        /* Main Content Headings */
        h1, h2, h3, h4, h5, h6 {
            color: #FFFFFF !important;
            font-weight: 700 !important;
            letter-spacing: -0.5px;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }
        
        /* Markdown Text */
        .stMarkdown, p, li {
            color: #cccccc !important;
            line-height: 1.6;
        }

        /* Header Styling Strategy: Transparent Header, Visible Toggle, Hidden Utilities */
        
        /* 1. Make the main header transparent and pass-through, but visible for layout */
        header[data-testid="stHeader"] {
            background-color: transparent !important;
            visibility: visible !important;
        }

        /* 2. Hide the colored decoration line at the top */
        div[data-testid="stDecoration"] {
            visibility: hidden;
            display: none;
        }

        /* 3. Hide the Main Menu (kebab) and Toolbar */
        #MainMenu {visibility: hidden;}
        [data-testid="stToolbar"] {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* 4. Style and Force-Show the Sidebar Toggle Button */
        button[data-testid="stSidebarCollapsedControl"] {
            visibility: visible !important;
            display: block !important;
            color: #ffffff !important;
            background-color: rgba(255, 255, 255, 0.15);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 8px;
            padding: 0.5rem;
            margin-top: 1rem;
            margin-left: 1rem;
            z-index: 100000; /* Ensure it sits on top */
            transition: all 0.3s ease;
        }
        
        button[data-testid="stSidebarCollapsedControl"]:hover {
            background-color: rgba(255, 255, 255, 0.3);
            transform: scale(1.05);
        }

        /* Global Button Styling */
         .stButton > button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 10px 24px;
            border-radius: 8px;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        }

        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(118, 75, 162, 0.4);
        }
    </style>
    """

def get_login_css():
    """Returns CSS specifically for the login/signup page components"""
    return """
    <style>
        /* Main Glass Card Container for Split View */
        div[data-testid="column"] {
            background: rgba(18, 18, 18, 0.7);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
            padding: 40px;
        }

        /* Left Column (Forms) */
        div[data-testid="column"]:nth-of-type(1) {
            border-top-left-radius: 20px;
            border-bottom-left-radius: 20px;
            border-right: 1px solid rgba(255,255,255,0.05);
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

        /* Input Fields */
        .stTextInput > div > div > input {
            background-color: #121212;
            color: #E0E0E0;
            border: 1px solid #333;
            border-radius: 8px;
            padding: 12px 16px;
        }

        .stTextInput > div > div > input:focus {
            border-color: #764ba2;
            box-shadow: 0 0 0 2px rgba(118, 75, 162, 0.2);
        }
        
    </style>
    """
