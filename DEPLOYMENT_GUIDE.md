# 🚀 GitHub Deployment Guide for Tanzania GDP Predictor

## Complete Step-by-Step Instructions

### 📋 Prerequisites

Before starting, ensure you have:
- ✅ GitHub account (create at [github.com](https://github.com))
- ✅ Git installed on your computer ([download here](https://git-scm.com/downloads))
- ✅ Your GDP prediction notebook and data

---

## 🎯 Option 1: Deploy to Streamlit Cloud (RECOMMENDED - FREE & EASIEST)

### Step 1: Prepare Your Local Project

1. **Create project folder structure:**
```bash
tanzania-gdp-predictor/
├── app.py
├── tanzania_gdp_prediction.ipynb
├── requirements.txt
├── .gitignore
├── README.md
├── LICENSE
└── data/
    └── tanzania_gdp_data.csv
```

2. **Copy all files I created for you into this folder**

3. **Add your data file to the `data/` folder**

### Step 2: Initialize Git Repository

Open terminal/command prompt in your project folder:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Make first commit
git commit -m "Initial commit: Tanzania GDP Predictor"
```

### Step 3: Create GitHub Repository

1. Go to [github.com](https://github.com) and log in
2. Click the "+" icon (top right) → "New repository"
3. Fill in:
   - **Repository name**: `tanzania-gdp-predictor`
   - **Description**: "Machine learning model for predicting Tanzania's GDP"
   - **Public** (recommended for free deployment)
   - **DON'T** initialize with README (you already have one)
4. Click "Create repository"

### Step 4: Push Code to GitHub

GitHub will show you commands. Use these:

```bash
# Add GitHub as remote
git remote add origin https://github.com/YOUR_USERNAME/tanzania-gdp-predictor.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Replace `YOUR_USERNAME` with your actual GitHub username!**

### Step 5: Deploy to Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "Sign in with GitHub"
3. Click "New app"
4. Fill in:
   - **Repository**: `YOUR_USERNAME/tanzania-gdp-predictor`
   - **Branch**: `main`
   - **Main file path**: `app.py`
5. Click "Deploy!"

⏰ **Wait 2-5 minutes** for deployment to complete.

🎉 **Your app is now live!** You'll get a URL like: `https://YOUR_APP.streamlit.app`

---

## 🔧 Option 2: Deploy to Heroku

### Prerequisites
- Heroku account ([signup.heroku.com](https://signup.heroku.com))
- Heroku CLI ([devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli))

### Additional Files Needed

1. **Create `Procfile`** (no extension):
```bash
web: sh setup.sh && streamlit run app.py
```

2. **Create `setup.sh`**:
```bash
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

3. **Make setup.sh executable**:
```bash
chmod +x setup.sh
```

### Deployment Steps

```bash
# Login to Heroku
heroku login

# Create Heroku app
heroku create tanzania-gdp-predictor

# Push to Heroku
git push heroku main

# Open your app
heroku open
```

---

## 🌐 Option 3: Deploy to Render

1. Go to [render.com](https://render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Fill in:
   - **Name**: `tanzania-gdp-predictor`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py`
5. Click "Create Web Service"

---

## 🚂 Option 4: Deploy to Railway

1. Go to [railway.app](https://railway.app)
2. Click "Start a New Project"
3. Select "Deploy from GitHub repo"
4. Choose `tanzania-gdp-predictor`
5. Railway auto-detects Python
6. Add environment variables if needed
7. Deploy!

---

## 📝 Post-Deployment Checklist

After deployment, update your README.md with the live URL:

```bash
# Edit README.md and add your app URL
nano README.md  # or use any text editor

# Commit and push
git add README.md
git commit -m "Add live demo URL"
git push origin main
```

---

## 🔄 Making Updates

Whenever you want to update your deployed app:

```bash
# Make changes to your code
# Then:

git add .
git commit -m "Description of changes"
git push origin main
```

**Streamlit Cloud will automatically redeploy!** ✨

---

## 🛠️ Troubleshooting

### Problem: "Git not recognized"
**Solution**: Install Git from [git-scm.com](https://git-scm.com/downloads)

### Problem: "Permission denied (publickey)"
**Solution**: 
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Add to GitHub: Settings → SSH and GPG keys → New SSH key
```

Or use HTTPS instead:
```bash
git remote set-url origin https://github.com/YOUR_USERNAME/tanzania-gdp-predictor.git
```

### Problem: "Module not found" error on deployment
**Solution**: Make sure all packages are in `requirements.txt`

### Problem: "Data file not found"
**Solution**: Ensure `data/tanzania_gdp_data.csv` is in your repository and committed

### Problem: Streamlit app won't load
**Solution**: Check logs in Streamlit Cloud dashboard for error messages

---

## 🎨 Customization Tips

### Change App Theme
Create `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#2E86AB"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
```

### Add Custom Domain
In Streamlit Cloud:
1. Settings → Custom domain
2. Follow instructions to point your domain

---

## 📊 Monitoring Your App

### Streamlit Cloud
- View logs in the Streamlit Cloud dashboard
- Monitor app performance
- See visitor analytics (basic)

### Add Google Analytics (Optional)
Add to your `app.py`:
```python
# Google Analytics
st.markdown("""
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=YOUR-GA-ID"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'YOUR-GA-ID');
    </script>
""", unsafe_allow_html=True)
```

---

## 🔐 Security Best Practices

1. **Don't commit sensitive data:**
   - API keys
   - Passwords
   - Personal information

2. **Use environment variables for secrets:**
   ```python
   import os
   API_KEY = os.getenv('API_KEY')
   ```

3. **Add `.env` to `.gitignore`**

4. **In Streamlit Cloud:**
   - Settings → Secrets
   - Add secrets there, not in code

---

## 📚 Additional Resources

- **Streamlit Documentation**: [docs.streamlit.io](https://docs.streamlit.io)
- **Git Tutorial**: [git-scm.com/doc](https://git-scm.com/doc)
- **GitHub Guides**: [guides.github.com](https://guides.github.com)
- **Streamlit Community**: [discuss.streamlit.io](https://discuss.streamlit.io)

---

## ✅ Quick Command Reference

```bash
# Check git status
git status

# See commit history
git log --oneline

# Create new branch
git checkout -b feature-name

# Switch branches
git checkout main

# Pull latest changes
git pull origin main

# View remote URL
git remote -v

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Force push (use carefully!)
git push -f origin main
```

---

## 🎯 Next Steps

1. ✅ Deploy your app
2. 📝 Share the link with stakeholders
3. 📊 Gather feedback
4. 🔄 Iterate and improve
5. 📈 Add more features
6. 🌍 Expand to regional forecasting

---

## 🆘 Need Help?

- **Email**: your.email@example.com
- **GitHub Issues**: Open an issue in your repository
- **Streamlit Forum**: [discuss.streamlit.io](https://discuss.streamlit.io)

---

**Good luck with your deployment! 🚀**

*Last updated: February 2025*
