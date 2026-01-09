import streamlit.components.v1 as components

def inject_bot():
    """
    Injects the Botpress Client Webchat script into the Streamlit app.
    Uses the specific IDs extracted from the user's configuration.
    """
    # Use the specific Shareable URL provided by the user.
    # This renders the full chat interface immediately, which is better for sidebar usage
    # than a floating bubble that might get clipped or hidden.
    bot_url = "https://cdn.botpress.cloud/webchat/v2.2/shareable.html?configUrl=https://files.bpcontent.cloud/2026/01/08/13/20260108134110-VKCEHJIG.json"
    
    components.iframe(bot_url, height=600)
