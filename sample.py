import streamlit as st
import pandas as pd
import pickle

# Load the trained model and preprocessing steps
with open('Diabetes_Prediction_Model.pkl', 'rb') as model_file:
    model_and_preprocessing = pickle.load(model_file)

model = model_and_preprocessing['model']
column_transformer = model_and_preprocessing['preprocessing']

# Input interface
st.title("Diabetes Prediction")
st.subheader("Fill in the following information to predict the likelihood of diabetes.")

# Gender
gender = st.radio("Gender", ["Male", "Female"])

# Age
age = st.slider("Age", 1, 100, 25)

# Hypertension
hypertension = st.radio("Hypertension", ["No", "Yes"])

# Heart Disease
heart_disease = st.radio("Heart Disease", ["No", "Yes"])

# Smoking History
smoking_history = st.radio("Smoking History", ["Non-Smoker", "Current Smoker", "Past Smoker"])

# BMI
bmi = st.slider("BMI", 10.0, 50.0, 25.0, 0.1)

# HbA1c Level
hba1c_level = st.slider("HbA1c Level", 4.0, 10.0, 5.7, 0.1)

# Blood Glucose Level
blood_glucose_level = st.slider("Blood Glucose Level", 50, 200, 100)

# Make predictions
if st.button("Predict"):
    input_data = pd.DataFrame({
        'Gender': [gender],
        'Age': [age],
        'Hypertension': [1 if hypertension == "Yes" else 0],
        'Heart Disease': [1 if heart_disease == "Yes" else 0],
        'Smoking History': [smoking_history],
        'BMI': [bmi],
        'HbA1c Level': [hba1c_level],
        'Blood Glucose Level': [blood_glucose_level]
    })

    # Transform input data using the fitted ColumnTransformer
    input_data_transformed = column_transformer.transform(input_data)

    # Make predictions
    prediction = model.predict(input_data_transformed)

    # Display prediction result
    st.subheader("Prediction Result:")
    if prediction[0] == 0:
        st.write("The likelihood of having diabetes is low.")
    else:
        st.write("The likelihood of having diabetes is high.")

