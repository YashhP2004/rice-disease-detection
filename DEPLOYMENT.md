# Deployment Guide: Rice & Pulse Disease Detection App

I have prepared your local environment for deployment. Follow these final steps to get your app live.

## Step 1: Create Repository on GitHub (Completed)

You have successfully pushed your code to:
**https://github.com/YashhP2004/rice-disease-detection**

## Step 2: Push Code (Completed)

The code and the large model file have been pushed to the remote repository.

> **Update**: The model file was initially ignored. I have forced a push of the model file. If you already deployed, please **Reboot** your app.

## Step 3: Deploy on Streamlit Community Cloud (IMPORTANT)

**Do NOT check the "Deploy" button in your local app's toolbar.** It often fails to detect new repositories immediately.

**Instead, follow these steps:**

1.  Open your browser and go to: **[share.streamlit.io](https://share.streamlit.io/)**
2.  Log in with your GitHub account.
3.  Click the **"New app"** button (top right).
4.  **Use existing repo**:
    - Select or Paste: `YashhP2004/rice-disease-detection`
5.  **Branch**: `main`
6.  **Main file path**: `app.py`
7.  Click **"Deploy!"**.

## Troubleshooting

- **"Model not found"**: 
    - This happens if the model file wasn't uploaded. I have just fixed this by forcing the upload. 
    - **Fix**: Go to your app on share.streamlit.io -> Manage App -> **Reboot App**.
- **"ModuleNotFoundError: No module named 'cv2'"**: This is handled by `packages.txt`. If it persists, ensure `opencv-python-headless` is in `requirements.txt` (it usually is safer for cloud environments than `opencv-python`).
- **"Unable to deploy" (Local Toolbar)**: Ignore this error in your VS Code/Local browser. Use the website method above.
