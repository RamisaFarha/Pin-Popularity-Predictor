## Introduction

The **Pin Popularity Predictor** helps users forecast the popularity of Pinterest pins based on the text content of the pin's description and title. It leverages natural language processing techniques to classify pins as popular or not based on historical data.

## Features

- Predicts the popularity of a pin based on its description and title.
- Flask API that accepts JSON requests and returns predictions.
- Model built using Support Vector Machines (SVM) and TF-IDF for text vectorization.
- Evaluated three different models, with SVM demonstrating the best performance in terms of accuracy and reliability.

## Requirements

Make sure you have the following dependencies installed:

- Python 3.7+
- Flask
- scikit-learn
- joblib
- numpy
- pandas
- TfidfVectorizer (scikit-learn)

## Model Training

The model used in this project is pre-trained and saved as `svm_model.pkl` and `tfidf_vectorizer.pkl`. You can retrain the model with your own dataset by following these steps:

1. Preprocess the data using TF-IDF.
2. Train the model using the SVM classifier from scikit-learn.
3. Save the trained model and vectorizer using `joblib`.
