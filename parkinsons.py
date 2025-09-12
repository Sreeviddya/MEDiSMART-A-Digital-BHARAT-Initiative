import streamlit as st
import pandas as pd
import pickle
import os

# --- Page Content for Parkinson's Diagnosis ---
def show_page():
    st.title("Parkinson's Disease Diagnosis")
    st.markdown("---")
    st.write("Please fill out the form below with your vocal metrics to get a prediction on your Parkinson's status.")
    st.markdown("Note: This tool is for informational purposes only. Always consult a healthcare professional for a final diagnosis.")

    # Check if the required model files exist
    model_path = "parkinsons_model.pkl"
    scaler_path = "scaler.pkl"
    
    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        st.error(
            "Error: Model or scaler files not found. "
            "Please ensure `parkinsons_model.pkl` and `scaler.pkl` are in the same directory as this script."
        )
        return

    # Load the trained model and scaler
    try:
        model = pickle.load(open(model_path, "rb"))
        scaler = pickle.load(open(scaler_path, "rb"))
    except Exception as e:
        st.error(f"Error loading model files: {e}")
        return

    # Expected feature names based on the model training
    expected_features = [
        "MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", "MDVP:Jitter(%)", "MDVP:Jitter(Abs)", 
        "MDVP:RAP", "MDVP:PPQ", "Jitter:DDP", "MDVP:Shimmer", "MDVP:Shimmer(dB)", 
        "Shimmer:APQ3", "Shimmer:APQ5", "MDVP:APQ", "Shimmer:DDA", "NHR", "HNR", 
        "RPDE", "DFA", "spread1", "spread2", "D2", "PPE"
    ]
    
    # Create input fields in a multi-column form
    with st.form("parkinsons_diagnosis_form"):
        st.header("Vocal Features")
        
        # Split features into two columns for better layout
        col1, col2 = st.columns(2)
        
        input_data = {}
        with col1:
            input_data["MDVP:Fo(Hz)"] = st.number_input("MDVP:Fo(Hz)", help="Average vocal fundamental frequency.")
            input_data["MDVP:Fhi(Hz)"] = st.number_input("MDVP:Fhi(Hz)", help="Maximum vocal fundamental frequency.")
            input_data["MDVP:Flo(Hz)"] = st.number_input("MDVP:Flo(Hz)", help="Minimum vocal fundamental frequency.")
            input_data["MDVP:Jitter(%)"] = st.number_input("MDVP:Jitter(%)", format="%.6f", help="Measure of variation in fundamental frequency.")
            input_data["MDVP:Jitter(Abs)"] = st.number_input("MDVP:Jitter(Abs)", format="%.6f", help="Absolute measure of variation in fundamental frequency.")
            input_data["MDVP:RAP"] = st.number_input("MDVP:RAP", format="%.6f", help="Relative Average Perturbation.")
            input_data["MDVP:PPQ"] = st.number_input("MDVP:PPQ", format="%.6f", help="Five-point Period Perturbation Quotient.")
            input_data["Jitter:DDP"] = st.number_input("Jitter:DDP", format="%.6f", help="DDP-based Jitter.")
            input_data["MDVP:Shimmer"] = st.number_input("MDVP:Shimmer", format="%.6f", help="Local shimmer.")
            input_data["MDVP:Shimmer(dB)"] = st.number_input("MDVP:Shimmer(dB)", format="%.6f", help="Shimmer in dB.")
            input_data["Shimmer:APQ3"] = st.number_input("Shimmer:APQ3", format="%.6f", help="Three-point Amplitude Perturbation Quotient.")

        with col2:
            input_data["Shimmer:APQ5"] = st.number_input("Shimmer:APQ5", format="%.6f", help="Five-point Amplitude Perturbation Quotient.")
            input_data["MDVP:APQ"] = st.number_input("MDVP:APQ", format="%.6f", help="Amplitude Perturbation Quotient.")
            input_data["Shimmer:DDA"] = st.number_input("Shimmer:DDA", format="%.6f", help="DDA-based Shimmer.")
            input_data["NHR"] = st.number_input("NHR", help="Noise-to-Harmonics Ratio.")
            input_data["HNR"] = st.number_input("HNR", help="Harmonics-to-Noise Ratio.")
            input_data["RPDE"] = st.number_input("RPDE", help="Recurrence Period Density Entropy.")
            input_data["DFA"] = st.number_input("DFA", help="Detrended Fluctuation Analysis.")
            input_data["spread1"] = st.number_input("spread1", help="Nonlinear dynamic complexity measure.")
            input_data["spread2"] = st.number_input("spread2", help="Nonlinear dynamic complexity measure.")
            input_data["D2"] = st.number_input("D2", help="Correlation dimension.")
            input_data["PPE"] = st.number_input("PPE", help="Pitch Period Entropy.")

        submitted = st.form_submit_button("Get Prediction")

    if submitted:
        # Create a DataFrame from user inputs
        try:
            input_df = pd.DataFrame([input_data])
            # Ensure the columns are in the correct order for the scaler
            input_df = input_df[expected_features]
            
            # Scale the input data
            input_data_scaled = scaler.transform(input_df)
            
            # Make prediction
            prediction = model.predict(input_data_scaled)[0]
            
            st.markdown("---")
            if prediction == 1:
                st.warning(" **Prediction Result:** The person has Parkinson's disease.")
            else:
                st.success(" **Prediction Result:** The person does **NOT** have Parkinson's disease.")

        except Exception as e:
            st.error("An error occurred during prediction. Please ensure all fields are filled with valid numbers.")
            st.exception(e)
