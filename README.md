# 🇹🇿 Tanzania GDP Prediction Model

A machine learning model for predicting Tanzania's GDP using economic indicators. Built with Linear Regression and Decision Tree algorithms for quarterly GDP forecasting.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)

## 📊 About

This project uses machine learning to forecast Tanzania's GDP based on historical economic data and key indicators including:
- Export/Import values
- Foreign Direct Investment (FDI)
- Inflation rates
- Population metrics
- Agricultural production
- And more economic indicators

## 🚀 Live Demo

**🌐 Visit the app:** [Your-App-URL-Here]

*(Will be available after deployment)*

## ✨ Features

- **Dual Model Approach**: Compare Linear Regression vs Decision Tree predictions
- **Interactive Dashboard**: User-friendly web interface
- **Real-time Predictions**: Input economic indicators and get instant GDP forecasts
- **Data Visualization**: Beautiful charts and graphs
- **Model Comparison**: Side-by-side performance metrics
- **Export Results**: Download predictions as CSV

## 📁 Project Structure

```
tanzania-gdp-predictor/
├── app.py                          # Streamlit web application
├── tanzania_gdp_prediction.ipynb   # Jupyter notebook for analysis
├── model_training.py               # Model training script
├── requirements.txt                # Python dependencies
├── data/
│   └── tanzania_gdp_data.csv      # Dataset (sample)
├── models/
│   ├── linear_regression_model.pkl
│   └── decision_tree_model.pkl
├── .gitignore
├── README.md
└── LICENSE
```

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git

### Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/tanzania-gdp-predictor.git
cd tanzania-gdp-predictor
```

2. **Create virtual environment** (recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
streamlit run app.py
```

5. **Open your browser**
Navigate to `http://localhost:8501`

## 📦 Dependencies

```
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
scikit-learn>=1.3.0
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.17.0
joblib>=1.3.0
```

## 🎯 Usage

### Web Application

1. Launch the Streamlit app
2. Navigate through the sidebar menu:
   - **Home**: Overview and introduction
   - **Data Explorer**: View and analyze the dataset
   - **Make Prediction**: Input economic indicators for GDP forecast
   - **Model Comparison**: Compare model performance
   - **About**: Project information

### Jupyter Notebook

Open `tanzania_gdp_prediction.ipynb` in Jupyter:
```bash
jupyter notebook tanzania_gdp_prediction.ipynb
```

### Python Script

```python
import joblib
import numpy as np

# Load trained model
model = joblib.load('models/linear_regression_model.pkl')

# Make prediction
features = np.array([[...]]) # Your economic indicators
prediction = model.predict(features)
print(f"Predicted GDP: ${prediction[0]:.2f} Billion")
```

## 🌐 Deployment Options

### Option 1: Streamlit Community Cloud (FREE & EASIEST)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click "New app"
5. Select your repository
6. Deploy!

**✅ Recommended for beginners**

### Option 2: Heroku

```bash
# Install Heroku CLI
heroku login
heroku create tanzania-gdp-predictor
git push heroku main
heroku open
```

### Option 3: Render

1. Create account at [render.com](https://render.com)
2. Connect GitHub repository
3. Select "Web Service"
4. Deploy automatically

### Option 4: Railway

1. Visit [railway.app](https://railway.app)
2. "New Project" → "Deploy from GitHub"
3. Select repository
4. Deploy

## 📊 Model Performance

| Model | Train R² | Test R² | MAE | RMSE |
|-------|----------|---------|-----|------|
| Linear Regression | 0.XX | 0.XX | $X.XX B | $X.XX B |
| Decision Tree | 0.XX | 0.XX | $X.XX B | $X.XX B |

*(Update with actual metrics after training)*

## 📈 Data Sources

- National Bureau of Statistics (NBS) Tanzania
- Bank of Tanzania
- World Bank Open Data
- International Monetary Fund (IMF)

## 🔒 Legal & Compliance

This model complies with Tanzania's regulatory framework:
- ✅ Uses publicly available, non-personal data
- ✅ No Personal Data Protection Act (PDPA) registration required
- ✅ Follows Statistics Act, 2015 guidelines
- ✅ Transparent methodology

**Disclaimer**: This model is for informational and research purposes only. Predictions should not be used as the sole basis for investment or policy decisions. Always consult professional economists and financial advisors.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Your Name**
- GitHub: [@your-username](https://github.com/your-username)
- Email: your.email@example.com
- LinkedIn: [Your Profile](https://linkedin.com/in/your-profile)

## 🙏 Acknowledgments

- Tanzania Commission for Science and Technology (COSTECH)
- National Bureau of Statistics Tanzania
- Bank of Tanzania
- Open-source community

## 📞 Contact & Support

- **Issues**: [GitHub Issues](https://github.com/YOUR_USERNAME/tanzania-gdp-predictor/issues)
- **Email**: your.email@example.com
- **Documentation**: [Wiki](https://github.com/YOUR_USERNAME/tanzania-gdp-predictor/wiki)

## 🗺️ Roadmap

- [ ] Add more economic indicators
- [ ] Implement ensemble methods (Random Forest, XGBoost)
- [ ] Create REST API
- [ ] Add real-time data integration
- [ ] Expand to other East African countries
- [ ] Mobile application
- [ ] Advanced scenario modeling

## 📚 Citations

If you use this model in your research, please cite:

```bibtex
@software{tanzania_gdp_predictor,
  author = {Your Name},
  title = {Tanzania GDP Prediction Model},
  year = {2025},
  url = {https://github.com/YOUR_USERNAME/tanzania-gdp-predictor}
}
```

---

**Made with ❤️ for Tanzania's economic development**

*Last updated: February 2025*
