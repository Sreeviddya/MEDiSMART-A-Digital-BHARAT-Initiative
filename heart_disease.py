import streamlit as st
import pandas as pd
import numpy as np

def show_page():
    """Renders the Heart Disease Diagnosis tool page."""

    st.header(" Heart Disease Diagnosis")
    st.markdown("---")
    st.write("Please fill out the form below to get a simulated prediction on your heart disease status.")
    st.markdown("Note: This tool is for informational purposes only. Always consult a healthcare professional for a final diagnosis.")

    # Create the form for user input
    with st.form("diagnosis_form"):
        st.subheader("Patient Information")

        # Define all form inputs
        age = st.number_input("Age", min_value=1, max_value=120, value=50, help="Age in years.")
        sex = st.radio("Sex", ["Male", "Female"], help="Biological sex.")
        cp = st.selectbox("Chest Pain Type", [
            "Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"
        ], help="Type of chest pain experienced.")
        trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=70, max_value=200, value=120, help="Resting blood pressure.")
        chol = st.number_input("Serum Cholestoral (mg/dl)", min_value=100, max_value=600, value=200, help="Serum cholesterol level.")
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl?", ["No", "Yes"], help="Is fasting blood sugar greater than 120 mg/dl?")
        restecg = st.selectbox("Resting Electrocardiographic Results", [
            "Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"
        ], help="Results from the resting ECG.")
        thalach = st.number_input("Maximum Heart Rate Achieved", min_value=70, max_value=220, value=150, help="Maximum heart rate achieved during exercise.")
        exang = st.radio("Exercise Induced Angina", ["No", "Yes"], help="Does exercise induce angina?")
        oldpeak = st.number_input("ST Depression", min_value=0.0, max_value=7.0, value=1.0, step=0.1, help="ST depression induced by exercise relative to rest.")
        slope = st.selectbox("Slope of the Peak Exercise ST Segment", [
            "Upsloping", "Flat", "Downsloping"
        ], help="The slope of the peak exercise ST segment.")
        ca = st.selectbox("Number of Major Vessels", [0, 1, 2, 3], help="Number of major vessels colored by fluoroscopy.")
        thal = st.selectbox("Thalium Stress Test Result", [
            "Normal", "Fixed Defect", "Reversible Defect"
        ], help="Results of the thallium stress test.")

        # Add a submit button to the form
        submitted = st.form_submit_button("Get Prediction")

    # This section runs only after the form is submitted
    if submitted:
        try:
            # Simulate a simple prediction model based on heuristics
            risk_score = 0
            # Higher risk for older age
            if age > 60: risk_score += 1
            # Higher risk for male sex
            if sex == "Male": risk_score += 1
            # Higher risk for certain chest pain types
            if cp in ["Atypical Angina", "Non-anginal Pain", "Asymptomatic"]: risk_score += 1
            # Higher risk for high blood pressure or cholesterol
            if trestbps > 140 or chol > 240: risk_score += 1
            # Higher risk for exercise-induced angina
            if exang == "Yes": risk_score += 2
            # Higher risk for ST depression
            if oldpeak > 1.5: risk_score += 1
            # Higher risk for certain thallium test results
            if thal in ["Fixed Defect", "Reversible Defect"]: risk_score += 2
            # Higher risk for multiple major vessels
            if ca > 0: risk_score += 1

            st.markdown("---")
            if risk_score >= 5:
                st.warning("⚠️ **Prediction Result:** Based on the information provided, there is a **moderate to high risk** of heart disease.")
            else:
                st.success("✅ **Prediction Result:** Based on the information provided, the risk of heart disease appears **low**.")
            
            st.markdown("---")
            st.info("The prediction logic is a simple heuristic and is not a substitute for a real medical diagnosis.")
        
        except Exception as e:
            st.error("An error occurred during prediction. Please check your inputs.")
            st.exception(e)
