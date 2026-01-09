import streamlit.components.v1 as components

def inject_bot():
    """
    Injects the Botpress Client Webchat script into the Streamlit app.
    Uses the specific IDs extracted from the user's configuration.
    """
    # User requested v3.5 "Bubble" implementation.
    # We render this in a tall iframe so the floating bubble has space to appear 
    # at the bottom, and the chat window has space to open upwards.
    bot_code = """
    <script src="https://cdn.botpress.cloud/webchat/v2.2/inject.js"></script>
    <script src="https://files.bpcontent.cloud/2026/01/08/13/20260108134110-H77XUNJD.js"></script>
    """
    
    components.html(bot_code, height=800, scrolling=False)
