# 🚀 Deployment Guide — Beesma Sai Varma Portfolio

This guide outlines step-by-step methods to deploy your portfolio website live to the internet for **free** with high performance and automatic SSL/HTTPS.

---

## ⚡ Option 1: Netlify Drop (Fastest — 30 Seconds, No Git Required)

1. Open your browser and go to [app.netlify.com/drop](https://app.netlify.com/drop).
2. Sign in or sign up for a free Netlify account.
3. Open File Explorer on your computer and navigate to:
   ```
   C:\Users\hp\.gemini\antigravity\scratch\portfolio-beesma
   ```
4. **Drag and drop** the entire `portfolio-beesma` folder directly onto the Netlify Drop webpage.
5. In seconds, Netlify will build and provide you with a live URL (e.g., `https://beesma-portfolio.netlify.app`).

---

## 🐙 Option 2: GitHub Pages (Recommended for Developers)

### Step 1: Initialize Git and Push to GitHub
Open PowerShell or your terminal:
```powershell
cd C:\Users\hp\.gemini\antigravity\scratch\portfolio-beesma

# Initialize Git repository
git init
git add .
git commit -m "Initial commit of AI/ML Portfolio"

# Rename branch to main
git branch -M main
```

### Step 2: Create a New GitHub Repository
1. Go to [github.com/new](https://github.com/new).
2. Name the repository (e.g., `portfolio` or `beesmasai.github.io`).
3. Keep it **Public** and do NOT initialize with README.
4. Click **Create repository**.

### Step 3: Link and Push
```powershell
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

### Step 4: Enable GitHub Pages
1. On GitHub, go to your repository **Settings** > **Pages** (in the left sidebar).
2. Under **Build and deployment** > **Source**, choose **Deploy from a branch**.
3. Select branch: `main` and folder: `/ (root)`.
4. Click **Save**.
5. Your website will be live in ~1 minute at:
   `https://YOUR_GITHUB_USERNAME.github.io/YOUR_REPO_NAME/`

---

## ▲ Option 3: Vercel (High Performance Global Edge)

1. Go to [vercel.com](https://vercel.com) and sign in with GitHub.
2. Click **"Add New..."** > **"Project"**.
3. Import your GitHub repository (`portfolio`).
4. Keep the default settings (Framework Preset: *Other*, Root Directory: `./`).
5. Click **Deploy**.
6. Your portfolio is immediately live with automatic CI/CD whenever you push changes to GitHub.

---

## ☁️ Option 4: Cloudflare Pages

1. Go to [dash.cloudflare.com](https://dash.cloudflare.com) > **Workers & Pages**.
2. Click **Create Application** > **Pages** > **Connect to Git**.
3. Select your portfolio repository.
4. Set Build Output directory to `/`.
5. Click **Save and Deploy**.

---

## 📧 Contact Form Delivery in Production

Your contact form is already configured with dual-delivery:
1. **Direct API Dispatch to Gmail (`bheeshmasaivarma@gmail.com`)**:
   - The first time someone submits the form from your deployed live domain, FormSubmit will send a **one-time activation email** to `bheeshmasaivarma@gmail.com`.
   - Open that email and click **"Activate Form"**.
   - After that, all subsequent visitor messages will instantly arrive in your Gmail inbox!
2. **Direct Gmail Web Composer**:
   - Visitors can also click **"Compose Directly in Gmail Web"** to open Gmail with your address pre-filled.

---

## 🌐 Custom Domain Setup (Optional)

If you own a custom domain (e.g., `beesmasaivarma.com` or `beesma.dev`):
1. In your hosting dashboard (Vercel, Netlify, or GitHub Pages), go to **Domain Management**.
2. Add your custom domain.
3. Configure the DNS `CNAME` or `A` records at your domain registrar (GoDaddy, Namecheap, Google Domains).
4. Automatic SSL certificates are provisioned for you at no cost.

---

## 🛠️ Local Development & Testing

To test your portfolio locally at any time:
```powershell
cd C:\Users\hp\.gemini\antigravity\scratch\portfolio-beesma
node server.js
```
Then visit [http://localhost:3000](http://localhost:3000).
