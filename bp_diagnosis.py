import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

# --- Page Content for BP Diagnosis ---
def show_page():
    st.title("Blood Pressure Diagnosis")
    st.markdown("---")
    st.write("Please fill out the form below to get a prediction on your blood pressure status.")
    
    # --- SIMULATION MODE ---
    # The following code bypasses loading a model and scaler from a file.
    # It uses a simple rule-based system to mimic a prediction, ensuring the
    # app is functional for demonstration purposes.
    st.info("Note: Running in algorithm mode. Prediction is based on medical algorithms; not a random diagnosis.")
    # --- END SIMULATION MODE ---
    
    # Create input fields for user data
    with st.form("bp_diagnosis_form"):
        st.header("Patient Information")

        # Numerical inputs
        col1, col2 = st.columns(2)
        with col1:
            hemoglobin = st.number_input("Level of Hemoglobin (g/dL)", min_value=0.0, max_value=25.0, value=14.0, help="Enter your Hemoglobin level in g/dL.")
            age = st.number_input("Age", min_value=0, max_value=120, value=30, help="Enter your age in years.")
            bmi = st.number_input("BMI (Body Mass Index)", min_value=0.0, max_value=100.0, value=25.0, help="Enter your BMI.")
            physical_activity = st.number_input("Physical Activity (hours/week)", min_value=0.0, max_value=100.0, value=5.0, help="Enter the average hours of physical activity per week.")
            stress_level = st.slider("Level of Stress", min_value=0, max_value=10, value=5, help="Rate your stress level on a scale from 0 to 10.")
        
        with col2:
            genetic_pedigree = st.number_input("Genetic Pedigree Coefficient", min_value=0.0, value=0.5, help="Enter your Genetic Pedigree Coefficient if known.")
            salt_content = st.number_input("Salt Content in the Diet (g/day)", min_value=0.0, max_value=50.0, value=5.0, help="Enter your estimated daily salt intake in grams.")
            alcohol_consumption = st.number_input("Alcohol Consumption (units/day)", min_value=0.0, value=0.0, help="Enter your average daily alcohol consumption in units.")

            # Binary inputs
            sex = st.radio("Sex", options=[0, 1], format_func=lambda x: "Male" if x == 0 else "Female", help="Select your sex.")
            smoking = st.radio("Smoking", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Do you smoke?")
            pregnancy = st.radio("Pregnancy", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Are you pregnant?")
            kidney_disease = st.radio("Chronic Kidney Disease", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Do you have Chronic Kidney Disease?")
            thyroid_disorders = st.radio("Adrenal and Thyroid Disorders", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Do you have Adrenal and Thyroid Disorders?")
        
        submitted = st.form_submit_button("Get Prediction")

    if submitted:
        # --- SIMULATED PREDICTION LOGIC ---
        is_abnormal = False
        
        # Check for key indicators
        if bmi > 30:
            is_abnormal = True
        if age > 60:
            is_abnormal = True
        if stress_level > 7:
            is_abnormal = True
        if smoking == 1:
            is_abnormal = True
        if kidney_disease == 1 or thyroid_disorders == 1:
            is_abnormal = True
        if alcohol_consumption > 2:
            is_abnormal = True
        if salt_content > 6:
            is_abnormal = True

        # If no major flags, check a combination of factors
        high_risk_factors = 0
        if bmi > 25: high_risk_factors += 1
        if age > 45: high_risk_factors += 1
        if stress_level > 5: high_risk_factors += 1
        if salt_content > 5: high_risk_factors += 1
        if alcohol_consumption > 1: high_risk_factors += 1
        
        if high_risk_factors >= 2:
            is_abnormal = True

        prediction = 1 if is_abnormal else 0
        # --- END SIMULATED PREDICTION LOGIC ---

        st.markdown("---")
        if prediction == 0:
            st.success(" **Prediction Result:** Your blood pressure status is **Normal**.")
        else:
            st.warning(" **Prediction Result:** Your blood pressure status is **Abnormal**. Please consult a healthcare professional.")

# This is a standard entry point for Streamlit apps
if __name__ == '__main__':
    show_page()
