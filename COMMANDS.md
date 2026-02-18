# 💻 Git & Deployment Commands Cheat Sheet

Quick reference for all commands you'll need.

---

## 🔧 Initial Setup (One Time Only)

### Install Git
```bash
# Windows: Download from https://git-scm.com/download/win
# Mac: 
brew install git
# Linux (Ubuntu):
sudo apt-get install git
```

### Configure Git
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Verify configuration
git config --list
```

---

## 📦 Project Setup

### Initialize New Repository
```bash
cd path/to/tanzania-gdp-predictor
git init
```

### First Commit
```bash
git add .
git commit -m "Initial commit: Tanzania GDP Predictor"
```

### Connect to GitHub
```bash
# Replace YOUR_USERNAME with your GitHub username
git remote add origin https://github.com/YOUR_USERNAME/tanzania-gdp-predictor.git
git branch -M main
git push -u origin main
```

---

## 🔄 Daily Workflow Commands

### Check Status
```bash
git status                    # See what files changed
git diff                      # See exact changes
git log --oneline            # See commit history
```

### Make Changes
```bash
git add .                     # Add all changes
git add filename.py          # Add specific file
git commit -m "Description"  # Commit with message
git push origin main         # Push to GitHub
```

### Update Local Code
```bash
git pull origin main         # Get latest changes from GitHub
```

---

## 🌿 Branching (For New Features)

### Create and Switch to New Branch
```bash
git checkout -b feature-name    # Create and switch to branch
git checkout main              # Switch back to main
```

### Merge Branch
```bash
git checkout main              # Switch to main
git merge feature-name         # Merge feature branch
git push origin main           # Push merged changes
```

### Delete Branch
```bash
git branch -d feature-name     # Delete local branch
git push origin --delete feature-name  # Delete remote branch
```

---

## 🐍 Python/Streamlit Commands

### Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Deactivate
deactivate
```

### Install Dependencies
```bash
pip install -r requirements.txt      # Install all packages
pip install streamlit               # Install specific package
pip freeze > requirements.txt       # Update requirements.txt
```

### Run Application
```bash
streamlit run app.py                # Run locally
python model_training.py            # Train models
jupyter notebook                    # Open Jupyter
```

---

## 🚀 Deployment Commands

### Streamlit Cloud
```bash
# Just push to GitHub, Streamlit auto-deploys
git push origin main
```

### Heroku
```bash
heroku login
heroku create tanzania-gdp-predictor
git push heroku main
heroku open
heroku logs --tail              # View logs
```

### Manual Deployment Check
```bash
# Test locally before deploying
streamlit run app.py
# Open http://localhost:8501
```

---

## 🔍 Debugging Commands

### View Logs
```bash
# Git logs
git log --oneline --graph        # Visual commit history
git log --author="Your Name"     # Your commits only

# Python/Streamlit logs (when running locally)
streamlit run app.py --server.fileWatcherType none  # Disable file watcher
```

### Fix Common Issues
```bash
# Remove file from Git tracking (but keep locally)
git rm --cached filename

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes) ⚠️ DANGEROUS
git reset --hard HEAD~1

# Discard local changes
git checkout -- filename
git checkout .                   # All files
```

---

## 📊 Data Commands

### Check Data
```bash
# Python
python -c "import pandas as pd; print(pd.read_csv('data/tanzania_gdp_data.csv').shape)"

# Show first few rows
head -10 data/tanzania_gdp_data.csv

# Count lines
wc -l data/tanzania_gdp_data.csv
```

---

## 🔐 Secrets Management

### Streamlit Secrets (Local)
```bash
# Create .streamlit/secrets.toml
mkdir .streamlit
echo 'API_KEY = "your-secret-key"' > .streamlit/secrets.toml

# In Python
import streamlit as st
api_key = st.secrets["API_KEY"]
```

### Streamlit Cloud Secrets
```
# Go to: share.streamlit.io → Your App → Settings → Secrets
# Add secrets in TOML format
```

---

## 📦 Package Management

### Check Versions
```bash
python --version
pip --version
git --version
streamlit --version
```

### Update Packages
```bash
pip install --upgrade pip
pip install --upgrade streamlit
pip install --upgrade -r requirements.txt
```

---

## 🆘 Emergency Commands

### Something Went Wrong?

```bash
# Start over with Git (keeps your files)
rm -rf .git
git init
git add .
git commit -m "Fresh start"

# Force push (⚠️ Use carefully!)
git push -f origin main

# Reset to remote state
git fetch origin
git reset --hard origin/main
```

### Streamlit Issues
```bash
# Clear Streamlit cache
streamlit cache clear

# Run with verbose logging
streamlit run app.py --logger.level=debug

# Run on different port
streamlit run app.py --server.port 8502
```

---

## 📝 Quick Workflows

### Complete Update Workflow
```bash
# 1. Check status
git status

# 2. Add changes
git add .

# 3. Commit
git commit -m "Updated model accuracy"

# 4. Push to GitHub
git push origin main

# 5. Wait for Streamlit auto-deploy (2-5 minutes)
# Check: https://share.streamlit.io/YOUR_USERNAME/tanzania-gdp-predictor
```

### Fix Typo Workflow
```bash
# Fix typo in last commit message
git commit --amend -m "New message"
git push -f origin main          # Force push

# Fix typo in file
# (edit file)
git add filename
git commit -m "Fix typo"
git push origin main
```

### Create New Feature Workflow
```bash
# 1. Create branch
git checkout -b new-feature

# 2. Make changes
# (edit files)

# 3. Commit changes
git add .
git commit -m "Add new feature"

# 4. Push branch
git push origin new-feature

# 5. Create Pull Request on GitHub
# 6. Merge when ready
```

---

## 🎓 Pro Tips

```bash
# Create aliases for common commands
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit

# Now use short versions:
git st      # instead of git status
git co main # instead of git checkout main
```

### View Beautiful Git Log
```bash
git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
```

### Find Large Files
```bash
git rev-list --objects --all | 
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' |
  sed -n 's/^blob //p' |
  sort --numeric-sort --key=2 |
  tail -n 10
```

---

## 📱 Mobile/Tablet Sharing

### Get App URL
```bash
# After Streamlit deployment, share this URL:
https://YOUR-APP-NAME.streamlit.app

# Or create QR code at: https://www.qr-code-generator.com/
```

---

## 🔗 Useful URLs

- **GitHub**: [github.com](https://github.com)
- **Streamlit Cloud**: [share.streamlit.io](https://share.streamlit.io)
- **Git Documentation**: [git-scm.com/doc](https://git-scm.com/doc)
- **Streamlit Docs**: [docs.streamlit.io](https://docs.streamlit.io)
- **Python Docs**: [docs.python.org](https://docs.python.org)

---

## 💡 Remember

- **Commit often** - Small commits are easier to manage
- **Write clear commit messages** - Future you will thank you
- **Pull before push** - Avoid merge conflicts
- **Test locally first** - Don't break production
- **Backup important data** - Git is not a backup system

---

**Happy coding! 🎉**

*Save this file for quick reference!*
