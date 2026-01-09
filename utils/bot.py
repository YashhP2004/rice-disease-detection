import streamlit.components.v1 as components

def inject_bot():
    """
    Injects the Botpress Client Webchat script into the Streamlit app.
    Uses the specific IDs extracted from the user's configuration.
    """
    # Reverting to "Inline/Embedded" mode because the "Bubble" script 
    # fails to render reliably inside Streamlit's iframe sandbox.
    # This ensures the chat interface is always visible in the sidebar.
    # RESTORED: Inline/Embedded mode with v2.2 script.
    # This is the ONLY configuration that guarantees the bot is visible and usable 
    # within the Streamlit Sidebar iframe restrictions.
    # Height is set to 550px to fit on standard screens without scrolling.
    # Switching to components.iframe() with the v3.5 Shareable URL.
    # This renders the hosted Botpress interface directly, bypassing local script injection issues.
    # It allows the user to "directly see the chat" as requested.
    bot_url = "https://cdn.botpress.cloud/webchat/v3.5/shareable.html?configUrl=https://files.bpcontent.cloud/2026/01/08/13/20260108134110-VKCEHJIG.json"
    
    components.iframe(bot_url, height=600)
