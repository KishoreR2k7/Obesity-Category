import streamlit as st
import pickle
import numpy as np



model , scaler = pickle.load(open('trained_model.sav', 'rb'))


st.title("Obesity Prediction")

st.write("Enter the details below to predict")

Age = st.number_input('Age:')
Gender = st.number_input('Gender:')
Height=st.number_input('Height:')
Weight=st.number_input('Weight:')
BMI=st.number_input('BMI:')
PhysicalActivityLevel=st.number_input('PhysicalActivityLevel:')

features = np.array([[Age,Gender,Height,Weight,BMI,PhysicalActivityLevel]])

features_scaled = scaler.transform(features)

if st.button("Obesity Price"):
    prediction = model.predict(features_scaled)
    st.success(f"Estimated Category: {prediction[0]:,.2f}k")