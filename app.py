from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load trained model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

# Home route (optional)
@app.route('/')
def home():
    return 'Diabetes Prediction API is running. Go to /predict_form for the web form.'

# API route for direct POST JSON
@app.route('/predict', methods=['POST'])
def predict_api():
    data = request.get_json()
    try:
        # Extract the 5 features
        features = ['HighChol', 'BMI', 'DiffWalk', 'HighBP', 'GenHlth']
        input_data = [data.get(f) for f in features]
        input_array = np.array([input_data])
        input_scaled = scaler.transform(input_array)
        prediction = model.predict(input_scaled)[0]
        return jsonify({'prediction': int(prediction)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Web form interface
@app.route('/predict_form', methods=['GET', 'POST'])
def predict_form():
    if request.method == 'POST':
        try:
            # Get values from the form
            features = ['HighChol', 'BMI', 'DiffWalk', 'HighBP', 'GenHlth']
            input_data = [int(request.form[f]) for f in features]

            input_array = np.array([input_data])
            input_scaled = scaler.transform(input_array)
            prediction = model.predict(input_scaled)[0]

            result = "Diabetic" if prediction == 1 else "Not Diabetic"
            return render_template("index.html", prediction=result)
        except Exception as e:
            return render_template("index.html", prediction=f"Error: {str(e)}")
    return render_template("index.html")

# Run app
if __name__ == '__main__':
    app.run(debug=True)
