import streamlit.components.v1 as components

def inject_bot():
    """
    Injects the Botpress Client Webchat script into the Streamlit app.
    Uses the specific IDs extracted from the user's configuration.
    """
    # User-provided custom embedding code for inline rendering
    # This renders the chat within a specific div (#webchat) instead of a floating bubble.
    custom_html = """
    <!-- Script -->
    <script src="https://cdn.botpress.cloud/webchat/v2.2/inject.js"></script>
    
    <!-- Custom Styles to un-float the chat -->
    <style>
      #webchat .bpWebchat {
        position: unset;
        width: 100%;
        height: 100%;
        max-height: 100%;
        max-width: 100%;
      }
      #webchat .bpFab {
        display: none; /* Hide the floating button */
      }
    </style>

    <!-- Container -->
    <div id="webchat" style="width: 100%; height: 500px; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"></div>

    <!-- Initialization -->
    <script>
      window.botpress.on("webchat:ready", () => {
        window.botpress.open();
      });
      window.botpress.init({
        "botId": "e7d1682e-a4a8-4721-87b8-fc9ab6f60952",
        "configuration": {
          "version": "v2",
          "botName": "Agri Support Agent",
          "botDescription": "",
          "website": {},
          "email": {},
          "phone": {},
          "termsOfService": {},
          "privacyPolicy": {},
          "color": "#58a963",
          "variant": "solid",
          "headerVariant": "glass",
          "themeMode": "light",
          "fontFamily": "inter",
          "radius": 3,
          "feedbackEnabled": false,
          "footer": "[⚡ by Botpress](https://botpress.com/?from=webchat)",
          "soundEnabled": false,
          "proactiveMessageEnabled": false,
          "proactiveBubbleMessage": "Hi! 👋 Need help?",
          "proactiveBubbleTriggerType": "afterDelay",
          "proactiveBubbleDelayTime": 10
        },
        "clientId": "90ba92f3-3719-4a18-b0e5-e5bab18a7ef6",
        "selector": "#webchat"
      });
    </script>
    """
    
    components.html(custom_html, height=520, scrolling=False)
