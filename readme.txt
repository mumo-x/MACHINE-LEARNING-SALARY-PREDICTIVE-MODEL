# 📊 Data Science Salary Prediction App

A dynamic Flask web application to analyze and predict salaries of data science professionals using machine learning models.

---

## 🚀 Features
- Upload CSV dataset for model training & EDA
- Multiple regression models evaluated (Linear, Ridge, RF, GB, SVR)
- Interactive prediction form for new salary forecasts
- Visualizations embedded directly via base64 images

---

## 🗂️ Project Structure
```
├── app.py                    # Flask app logic
├── salary_prediction_ml.py  # ML class and logic
├── uploads/                 # Uploaded CSV files
├── templates/
│   ├── layout.html
│   ├── index.html
│   └── results.html
├── static/                  # (Optional future assets)
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/your-username/salary-prediction-app.git
cd salary-prediction-app
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
python app.py
```
Visit `http://127.0.0.1:5000` in your browser.

---

## 📄 Example CSV Columns
Your dataset should include:
- `experience_level`, `job_title`, `employee_residence`, `company_location`, `company_size`, `remote_ratio`, `employment_type`, `salary_in_usd`

---

## 📬 Contact
For any issues or feature requests, please contact `designerssplendor@gmail.com`

---

