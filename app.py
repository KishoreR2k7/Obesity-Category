import streamlit as st
import pickle
import numpy as np



model , scaler = pickle.load(open('trained_model.sav', 'rb'))

label_map=map({'Normal weight':0,'Obese':1,'Overweight':2,'Underweight':3})
st.title("Obesity Prediction")

st.write("Enter the details below to predict")

Age = st.number_input('Age:')
Gender = st.number_input('Gender (Male : 0 ,Female : 1):')
Height=st.number_input('Height:')
Weight=st.number_input('Weight:')
BMI=st.number_input('BMI:')
PhysicalActivityLevel=st.number_input('PhysicalActivityLevel:')

features = np.array([[Age,Gender,Height,Weight,BMI,PhysicalActivityLevel]])

features_scaled = scaler.transform(features)

if st.button("Obesity Price"):
    prediction = model.predict(features_scaled)
    st.success(f'Estimated Category: {label_map[prediction[0]]}')