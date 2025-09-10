# Salary Predictor Web Application

## Overview
A streamlined web application that allows users to upload CSV salary data, trains machine learning models, and provides salary predictions based on job characteristics.

## Setup Instructions
1. Ensure Python 3.7+ is installed
2. Navigate to the project directory
3. Install required packages:
   ```
   pip install -r requirements.txt
   ```
4. Run the Flask app:
   ```
   python app.py
   ```

## Features
- CSV file upload with automatic data preprocessing
- Multiple machine learning model training and comparison
- Individual salary prediction interface
- Clean, responsive web interface

## Usage
1. Open browser and navigate to `http://localhost:5000`
2. Upload a CSV file containing salary data
3. View model performance metrics
4. Use the prediction form to estimate salaries

## Dependencies
- Flask
- Flask-CORS
- pandas
- scikit-learn
- numpy

## Requirements
- CSV file must contain a `salary_in_usd` column
- Supported job fields: Data Science, ML Engineering, Analytics
