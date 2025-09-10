from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pandas as pd
import math
from model import ModelTrainer, predict_salary

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        
        file = request.files['file']
        if file.filename == '' or not file.filename.lower().endswith('.csv'):
            return jsonify({'error': 'Please select a valid CSV file'}), 400
        
        df = pd.read_csv(file)
        if df.empty or 'salary_in_usd' not in df.columns:
            return jsonify({'error': 'CSV must contain salary_in_usd column and data'}), 400
        
        # Clean column names
        df.columns = df.columns.str.replace(' ', '_')

        # Handle missing values
        for col in df.select_dtypes(include=['number']).columns:
            df[col].fillna(df[col].median(), inplace=True)
        for col in df.select_dtypes(include=['object']).columns:
            df[col].fillna(df[col].mode()[0] if not df[col].dropna().empty else 'Unknown', inplace=True)

        # Train model
        trainer = ModelTrainer(df)
        trainer.encode_categorical_variables(df.columns)
        trainer.split_data('salary_in_usd')
        trainer.train_all_models()

        # Clean performance data
        cleaned_performance = {}
        for model_name, metrics in trainer.model_performance.items():
            if model_name == 'boxplot_paths':
                continue
            cleaned_metrics = {}
            for metric_name, value in metrics.items():
                if math.isinf(value):
                    cleaned_metrics[metric_name] = 999999.0 if value > 0 else -999999.0
                elif math.isnan(value):
                    cleaned_metrics[metric_name] = 0.0
                else:
                    cleaned_metrics[metric_name] = float(value)
            cleaned_performance[model_name] = cleaned_metrics
        
        # Get boxplot paths
        boxplot_paths = trainer.model_performance.get('boxplot_paths', {'before': '', 'after': ''})
        
        # Get first 5 rows for preview
        data_preview = df.head(5).to_dict('records')
        
        return jsonify({
            'performance': cleaned_performance,
            'boxplot_before': boxplot_paths['before'],
            'boxplot_after': boxplot_paths['after'],
            'data_preview': data_preview
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('predict.html')
    
    form_data = {
        'experience_level': request.form.get('experience_level'),
        'employment_type': request.form.get('employment_type'),
        'job_title': request.form.get('job_title'),
        'employee_residence': request.form.get('employee_residence'),
        'remote_ratio': request.form.get('remote_ratio'),
        'company_location': request.form.get('company_location'),
        'company_size': request.form.get('company_size')
    }

    if not all(form_data.values()):
        return render_template('predict.html', error="Please fill all fields.", form_data=form_data)

    try:
        input_data = form_data.copy()
        input_data['remote_ratio'] = int(input_data['remote_ratio'])
        predicted_salary = predict_salary(input_data)
        return render_template('predict.html', predicted_salary=predicted_salary, form_data=form_data)
    except Exception as e:
        return render_template('predict.html', error=f"Prediction error: {str(e)}", form_data=form_data)

if __name__ == '__main__':
    app.run(debug=True)
