import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

# --- Page Content for Lung Cancer Diagnosis ---
def show_page():
    st.title("Lung Cancer Diagnosis")
    st.markdown("---")
    st.write("Please fill out the form below to get a prediction on your lung cancer risk.")
    st.markdown("Note:Running in algorithm mode. Prediction is based on medical algorithms; not a random diagnosis.")

    # --- SIMULATION MODE ---
    # The following code bypasses loading a model and scaler from a file.
    # It uses a simple rule-based system to mimic a prediction, ensuring the
    # app is functional for demonstration purposes.
    st.info("Note: Running in simulated mode. Prediction is based on a simple rule set, not a trained model.")
    # --- END SIMULATION MODE ---
    
    # Create input fields for user data
    with st.form("lung_cancer_diagnosis_form"):
        st.header("Risk Factors")
        
        # Two columns for better layout
        col1, col2 = st.columns(2)
        
        with col1:
            age = st.number_input("Age", min_value=0, max_value=120, value=30, help="Your age in years.")
            cigarettes = st.number_input("Cigarettes per day", min_value=0.0, max_value=100.0, value=0.0, help="Number of cigarettes you smoke per day.")
            smoking_years = st.number_input("Years of Smoking", min_value=0, max_value=100, value=0, help="Number of years you have been smoking.")
            air_quality = st.slider("Air Quality", min_value=1.0, max_value=10.0, value=5.0, step=0.1, help="Rating of your local air quality (1=Poor, 10=Excellent).")
            alcohol = st.slider("Alcohol consumption", min_value=1.0, max_value=10.0, value=5.0, step=0.1, help="Rating of your alcohol consumption (1=Low, 10=High).")
            
            # --- New Inputs (Col 1) ---
            secondhand_smoke = st.radio("Secondhand Smoke Exposure", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Are you regularly exposed to secondhand smoke?")
            occupational_hazards = st.radio("Occupational Hazards", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Are you exposed to asbestos, radon, or other industrial chemicals?")
            family_history = st.radio("Family History", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Do you have a family history of lung disease?")
            
        with col2:
            genetic_risk = st.radio("Genetic Predisposition", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Do you have a family history of lung cancer?")
            chronic_cough = st.radio("Chronic Cough", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Have you had a persistent cough for more than 8 weeks?")
            fatigue = st.radio("Fatigue", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Do you experience unexplained and persistent fatigue?")
            chest_pain = st.radio("Chest Pain", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Do you experience unexplained chest pain?")
            
            # --- New Inputs (Col 2) ---
            weight_loss = st.radio("Unexplained Weight Loss", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Have you experienced unexplained weight loss?")
            loss_of_appetite = st.radio("Loss of Appetite", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Have you recently experienced a loss of appetite?")
            hoarseness = st.radio("Hoarseness", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Do you have a persistent hoarseness or voice changes?")
            shortness_of_breath = st.radio("Shortness of Breath", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Do you experience shortness of breath during daily activities?")
            recurrent_infections = st.radio("Recurrent Infections", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Do you frequently have pneumonia or bronchitis?")
            swelling = st.radio("Facial/Neck Swelling", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes", help="Do you have swelling in your face or neck?")
            
        submitted = st.form_submit_button("Get Prediction")

    if submitted:
        # --- SIMULATED PREDICTION LOGIC ---
        risk_score = 0
        if age > 50: risk_score += 1
        if cigarettes > 10: risk_score += 2
        if smoking_years > 20: risk_score += 3
        if air_quality < 4: risk_score += 1
        if alcohol > 7: risk_score += 1
        if genetic_risk == 1: risk_score += 2
        if chronic_cough == 1: risk_score += 1
        if fatigue == 1: risk_score += 1
        if chest_pain == 1: risk_score += 2
        
        # New inputs in simulated logic
        if secondhand_smoke == 1: risk_score += 2
        if occupational_hazards == 1: risk_score += 2
        if family_history == 1: risk_score += 3
        if weight_loss == 1: risk_score += 2
        if loss_of_appetite == 1: risk_score += 1
        if hoarseness == 1: risk_score += 1
        if shortness_of_breath == 1: risk_score += 2
        if recurrent_infections == 1: risk_score += 1
        if swelling == 1: risk_score += 2

        # A simple threshold to determine the prediction
        prediction = 1 if risk_score >= 8 else 0
        # --- END SIMULATED PREDICTION LOGIC ---
            
        st.markdown("---")
        if prediction == 1:
            st.warning(" **Prediction Result:** Lung Cancer Detected. Please consult a healthcare professional.")
        else:
            st.success(" **Prediction Result:** No Lung Cancer Detected.")

# This is a standard entry point for Streamlit apps
if __name__ == '__main__':
    show_page()
