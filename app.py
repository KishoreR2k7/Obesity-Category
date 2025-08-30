import streamlit as st
import pickle
import numpy as np

# Load the trained model and scaler
model, scaler = pickle.load(open('trained_model.sav', 'rb'))

# Define the label mapping for prediction categories
label_map = {0: 'Normal weight', 1: 'Obese', 2: 'Overweight', 3: 'Underweight'}

st.title("Obesity Prediction")

st.write("Enter the details below to predict:")

# Get user input
Age = st.number_input('Age:')
Gender = st.number_input('Gender (Male : 0, Female : 1):')
Height = st.number_input('Height (in cm):')
Weight = st.number_input('Weight (in kg):')
BMI = st.number_input('BMI:')
PhysicalActivityLevel = st.number_input('Physical Activity Level (scale 1-5):')

# Prepare the features array for prediction
features = np.array([[Age, Gender, Height, Weight, BMI, PhysicalActivityLevel]])

# Scale the features
features_scaled = scaler.transform(features)

# Predict when the button is clicked
if st.button("Predict Obesity Category"):
    prediction = model.predict(features_scaled)
    st.success(f'Estimated Category: {label_map[prediction[0]]}')
