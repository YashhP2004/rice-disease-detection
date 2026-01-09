# Deployment Guide: Rice & Pulse Disease Detection App

This guide walks you through deploying your Streamlit application to the Streamlit Community Cloud.

## Prerequisites

1.  **GitHub Account**: You need a GitHub account.
2.  **Streamlit Cloud Account**: Sign up at [share.streamlit.io](https://share.streamlit.io/) using your GitHub account.

## Step 1: Push Code to GitHub

You need to push your code to a GitHub repository. We have already prepared the project for **Git LFS** (Large File Storage) to handle the model file.

1.  **Commit your changes**:
    ```bash
    git add .
    git commit -m "Prepare for deployment: Add dependencies and LFS tracking"
    ```

2.  **Create a new repository on GitHub**:
    - Go to GitHub and create a new repository (e.g., `rice-disease-detection`).
    - **Important**: Do *not* initialize with README, .gitignore, or License (since you already have them).

3.  **Push to GitHub**:
    - Copy the remote URL from GitHub (e.g., `https://github.com/YOUR_USERNAME/rice-disease-detection.git`).
    - Link your local folder to the remote repository and push:
    ```bash
    git remote add origin <YOUR_REPO_URL>
    git branch -M main
    git push -u origin main
    ```
    *(If you are already connected to a repo, just `git push`)*.

    > **Note**: The upload might take a moment due to the large model file (267MB).

## Step 2: Deploy on Streamlit Community Cloud

1.  Go to [share.streamlit.io](https://share.streamlit.io/).
2.  Click **"New app"**.
3.  Select your repository (`rice-disease-detection`), branch (`main`), and main file path (`app.py`).
4.  Click **"Deploy!"**.

## Step 3: Monitor Deployment

- Streamlit will start building your app.
- Watch the **"Manage app" -> "Logs"** section.
- It will automatically install:
    - Python libraries from `requirements.txt`
    - System dependencies (like `libgl1`) from `packages.txt`
- Once finished, your app will be live!

## Troubleshooting

- **"Model not found"**: Ensure Git LFS uploaded the actual `.h5` file and not just a pointer. You can check the file size on GitHub; it should be ~267MB.
- **"ModuleNotFoundError: No module named 'cv2'"**: This is handled by `packages.txt`. If it persists, ensure `opencv-python-headless` is in `requirements.txt` (it usually is safer for cloud environments than `opencv-python`).
