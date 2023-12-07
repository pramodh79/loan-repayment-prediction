# app.py
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np
from your_custom_optimizer_module import CustomAdam

app = Flask(__name__)

# Register the custom optimizer
custom_objects = {'CustomAdam': CustomAdam}

# Load your model (assuming it's named "your_model.h5")
model_path = "D:/practicalDataScience/model/loan_prediction_model.h5"
model = load_model(model_path, custom_objects=custom_objects)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input data from the POST request
        data = request.get_json(force=True)
        
        # Extract the features from the input data
        features = data.get('features', {})
        
        # Create a DataFrame from the input features
        input_data = pd.DataFrame([features])
        
        # Make predictions using the loaded model
        predictions = model.predict(input_data.values)
        
        # Assuming the model predicts a binary output (0 or 1)
        prediction_result = int(predictions[0][0])
        
        # Return the prediction as JSON
        return jsonify({'prediction': prediction_result})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)