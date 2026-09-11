# CyberSentinel AI: Cloud Deployment & Hosting Guide

This guide walks you through deploying **CyberSentinel AI** to the cloud so you have a live, shareable HTTPS URL (`https://cybersentinel-ai.onrender.com`) to demonstrate during college project reviews, placements, and your final viva.

---

## Architecture: Why Deployment is So Easy

Thanks to our **Unified Production Architecture**, our FastAPI backend automatically serves the compiled React frontend directly from the `frontend/dist` directory. 
* **Single Container / Single Port:** You only need to deploy **one** web service.
* **Zero CORS Issues:** Frontend and backend run on the exact same domain.
* **Zero Cloud Costs:** Runs comfortably within free-tier resource limits.

---

## Method 1: Deploying to Render.com (Recommended - 100% Free)

Render is the industry standard for deploying Python + React full-stack applications with a free HTTPS certificate.

### Step 1: Push Your Code to GitHub
Ensure all code is committed and pushed to your personal GitHub repository:
```bash
git add .
git commit -m "feat: complete CyberSentinel AI platform with Live Radar"
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/cybersentinel-ai.git
git push -u origin main
```

### Step 2: Create a Free Web Service on Render
1. Go to [https://render.com](https://render.com) and Sign In (using your GitHub account).
2. Click the blue **"New +"** button in the top right and select **"Web Service"**.
3. Choose **"Build and deploy from a Git repository"** and select your `cybersentinel-ai` repository.

### Step 3: Configure Service Settings
Fill in the following fields:
* **Name:** `cybersentinel-ai` (or your preferred name)
* **Region:** Oregon (US West) or Frankfurt (EU)
* **Branch:** `main`
* **Root Directory:** *(leave blank)*
* **Runtime:** `Python 3`
* **Build Command:**
  ```bash
  pip install -r backend/requirements.txt && cd frontend && npm install && npm run build && cd ..
  ```
* **Start Command:**
  ```bash
  cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT
  ```
* **Instance Type:** `Free` ($0/month)

### Step 4: Environment Variables (Optional)
Under the **"Environment Variables"** tab:
* `SECRET_KEY`: Enter any random 32-character string.
* `GEMINI_API_KEY`: *(Optional)* Add your Gemini API key if you want live Google AI generation.

### Step 5: Click "Create Web Service"
Render will automatically:
1. Install Python dependencies and build the ChromaDB vector database.
2. Compile the React Vite frontend into optimized static assets.
3. Launch the FastAPI server.
4. Issue a free SSL/TLS certificate with a public URL:  
   `https://cybersentinel-ai.onrender.com`

---

## Method 2: Deploying with Docker (Railway or Fly.io)

If you prefer containerized deployment:

### Railway.app (1-Click)
1. Go to [https://railway.app](https://railway.app) and sign in with GitHub.
2. Click **"New Project"** $\to$ **"Deploy from GitHub repo"**.
3. Select `cybersentinel-ai`.
4. Railway automatically detects the project `Dockerfile` and deploys it.
5. In your Railway service settings under **"Networking"**, click **"Generate Domain"** to get your public HTTPS URL.

---

## Method 3: Local Tunneling (Instant 10-Second Demo Link)

If you want to share a live link with someone right this second without deploying to the cloud:
1. Ensure your local server is running (`./run_dev.sh`).
2. Open a new terminal tab and install/run `localtunnel` or `ngrok`:
   ```bash
   npx localtunnel --port 5173
   ```
3. It will give you a temporary public URL (e.g., `https://brave-fox-82.loca.lt`) that routes directly to your laptop!

---

## Production Health Checklist Before Final Viva

- [x] Pre-seeded accounts ready (`analyst` / `analyst123` and `admin` / `admin123`)
- [x] ChromaDB MITRE ATT&CK enterprise collection embedded and cached locally
- [x] All 9 automated pytest cases passing (`pytest -v`)
- [x] One-click PDF incident report generation verified
- [x] Live Radar telemetry stream running with instant attack wave simulation
