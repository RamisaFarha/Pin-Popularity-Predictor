# -*- coding: utf-8 -*-
"""app

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1msYRKeqJxrSQ4P4objqt8B4RyvZ113vy
"""

from flask import Flask, request, jsonify
import joblib

# Load the trained model and vectorizer
model = joblib.load('svm_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Initialize the Flask app
app = Flask(__name__)

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get the JSON data from the POST request
    description = data.get('description', '')  # Get the description (default is empty)
    title = data.get('title', '')  # Get the title (default is empty)

    # Combine description and title into one string
    text = f"{description} {title}"

    # Vectorize the combined text
    vectorized_text = vectorizer.transform([text])

    # Make a prediction using the model
    prediction = model.predict(vectorized_text)

    # Return the prediction as a JSON response
    return jsonify({'prediction': int(prediction[0])})

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)