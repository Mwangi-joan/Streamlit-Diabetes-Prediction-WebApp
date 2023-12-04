import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Function to preprocess data
def preprocess_data(data):
    # ... (same as before)
    def preprocess_data(data):
        # Encode categorical variables
        label_encoder = LabelEncoder()
        data['Gender'] = label_encoder.fit_transform(data['Gender'])
        data['Hypertension'] = label_encoder.fit_transform(data['Hypertension'])
        data['Heart Disease'] = label_encoder.fit_transform(data['Heart Disease'])
        data['Smoking History'] = label_encoder.fit_transform(data['Smoking History'])

        return data

# Function to make predictions
def predict_diabetes(model, input_data):
    # ... (same as before)
    def predict_diabetes(model, input_data):
        # Load additional preprocessing for input data
        input_data = preprocess_data(input_data)

        # Features and target variable
        X = input_data.drop('Diabetes', axis=1)

        # Make predictions
        prediction = model.predict(X)

        # Calculate accuracy
        accuracy = accuracy_score(X, prediction)


        return prediction, accuracy

def main():
    st.title("Diabetes Prediction App")
    st.subheader("Fill in the following information to predict the likelihood of diabetes.")

    # Input interface
    gender = st.radio("Gender", ["Male", "Female"])
    age = st.slider("Age", 1, 100, 25)
    hypertension = st.radio("Hypertension/High Blood Pressure", ["No", "Yes"])
    heart_disease = st.radio("Heart Disease", ["No", "Yes"])
    smoking_history = st.radio("Smoking History", ["Non-Smoker", "Current Smoker", "Past Smoker"])
    bmi = st.slider("BMI", 10.0, 50.0, 25.0, 0.1)
    hba1c_level = st.slider("HbA1c Level", 4.0, 10.0, 5.7, 0.1)
    blood_glucose_level = st.slider("Blood Glucose Level", 50, 200, 100)

    # Convert radio button values to binary
    hypertension = 1 if hypertension == "Yes" else 0
    heart_disease = 1 if heart_disease == "Yes" else 0

    # Create a DataFrame with the input data
    input_data = pd.DataFrame({
        'Gender': [gender],
        'Age': [age],
        'Hypertension': [hypertension],
        'Heart Disease': [heart_disease],
        'Smoking History': [smoking_history],
        'BMI': [bmi],
        'HbA1c Level': [hba1c_level],
        'Blood Glucose Level': [blood_glucose_level]
    })

    # Load the trained model
    with open('Diabetes_Prediction_Model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    # Make predictions
    prediction = predict_diabetes(model, input_data)

    # Display prediction result
    st.subheader("Prediction Result:")
    if prediction == 0:
        st.write("The likelihood of having diabetes is low.")
    else:
        st.write("The likelihood of having diabetes is high.")


if __name__ == "__main__":
    main()
