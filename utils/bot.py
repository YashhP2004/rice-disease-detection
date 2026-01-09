import streamlit.components.v1 as components

def inject_bot():
    """
    Injects the Botpress Client Webchat script into the Streamlit app.
    Uses the specific IDs extracted from the user's configuration.
    """
    bot_code = """
    <script src="https://cdn.botpress.cloud/webchat/v2.1/inject.js"></script>
    <script src="https://mediafiles.botpress.cloud/e7d1682e-a4a8-4721-87b8-fc9ab6f60952/webchat/v2.1/config.js"></script>
    """
    # Note: We use the hosted config.js based on the Bot ID as it ensures
    # the bot stays updated when the user changes settings in Botpress Studio.
    
    # Render with 0 height/width so it doesn't take up layout space 
    # but the script still runs (floating widget).
    components.html(bot_code, height=0, width=0)
