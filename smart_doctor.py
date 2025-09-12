import streamlit as st
import pickle
import numpy as np
import os

# --- Helper functions and data loading ---

# Check if the required model file exists before loading
model_path = "svc.pkl"
if not os.path.exists(model_path):
    st.error(
        "Error: The required model file 'svc.pkl' was not found. "
        "Please make sure it is in the same directory as this script."
    )
    st.stop()

# Load the trained model
try:
    model = pickle.load(open(model_path, "rb"))
except Exception as e:
    st.error(f"Error loading the model file: {e}")
    st.stop()

# Symptom and Disease Mapping
# Corrected Symptom List with 132 features to match the model's expectation
symptom_list = [
    "Fever", "Cough", "Fatigue", "Headache", "Sore Throat", "Runny Nose", "Body Aches", "Shortness of Breath",
    "Chest Pain", "Chills", "Nausea", "Vomiting", "Diarrhea", "Dizziness", "Sweating", "Loss of Appetite",
    "Joint Pain", "Skin Rash", "Blurred Vision", "Frequent Urination", "Weight Loss", "Insomnia", "Chest Tightness",
    "Palpitations", "Weakness", "Irritability", "Anxiety", "Depression", "Hair Loss", "Dry Skin", "Hearing Loss",
    "Loss of Smell", "Loss of Taste", "Sensitivity to Light", "Numbness", "Tingling", "Difficulty Swallowing",
    "Hoarseness", "Swollen Lymph Nodes", "Chronic Pain", "Seizures", "Memory Loss", "Confusion", "Hallucinations",
    "Swollen Joints", "Cold Hands and Feet", "Excessive Sweating", "Difficulty Breathing", "Nasal Congestion",
    "Chronic Cough", "Wheezing", "Blood in Urine", "Dark Urine", "Pale Stools", "Jaundice", "Bloating",
    "Constipation", "Heartburn", "Difficulty Walking", "Muscle Weakness", "Balance Problems", "Coordination Issues",
    "Tremors", "Slurred Speech", "Chronic Fatigue", "Night Sweats", "Mouth Ulcers", "Bruising Easily",
    "Slow Healing Wounds", "Excessive Thirst", "Cold Intolerance", "Heat Intolerance", "Rapid Heartbeat",
    "Unexplained Weight Gain", "Frequent Infections", "Increased Hunger", "Difficulty Concentrating",
    "Loss of Consciousness", "Sudden Mood Changes", "Bleeding Gums", "Excessive Gas", "Acid Reflux",
    "Dry Eyes", "Ear Pain", "Frequent Headaches", "Vision Changes", "Neck Stiffness", "Leg Cramps",
    "Unexplained Swelling", "Abdominal Pain", "Blood in Stool", "Nail Changes", "Itchy Skin", "Hives",
    "Chronic Sinus Infections", "Frequent Sneezing", "Lightheadedness", "Cold Sensitivity",
    # Added 34 new symptoms to match the 132 features
    "Painful Urination", "Discolored Urine", "Pain on one side of back", "Fever and Chills",
    "Foul-smelling urine", "Itching", "Burning sensation", "Skin discoloration", "Redness", "Swelling",
    "Pus-filled blisters", "Blisters", "Sores", "Rashes", "Sores in mouth", "Sores in throat",
    "Stomach pain", "Upper abdominal pain", "Lower abdominal pain", "Pain in left side",
    "Pain in right side", "Shoulder pain", "Knee pain", "Back pain", "Neck pain", "Shoulder stiffness",
    "Unstable gait", "Loss of balance", "Difficulty speaking", "Drooling", "Muscle cramps",
    "Muscle spasms", "Muscle rigidity", "Tingling and numbness in hands and feet"
]

disease_list = [
    "Common Cold", "Flu", "COVID-19", "Pneumonia", "Bronchitis", "Asthma", "Gastroenteritis", "Migraine",
    "Hypertension", "Diabetes", "Tuberculosis", "Malaria", "Typhoid", "Sinusitis", "Dengue", "Anemia",
    "Hepatitis", "Chronic Kidney Disease", "Lupus", "Parkinson's", "Alzheimer's", "Epilepsy", "Multiple Sclerosis",
    "Stroke", "Heart Disease", "COPD", "Liver Cirrhosis", "Irritable Bowel Syndrome", "Celiac Disease",
    "Thyroid Disorders", "Anxiety Disorder", "Depression", "Schizophrenia", "Psoriasis", "Eczema", "Osteoarthritis",
    "Rheumatoid Arthritis", "Gout", "Pancreatitis", "Glaucoma", "Macular Degeneration", "Sleep Apnea",
    "HIV/AIDS", "Polycystic Ovary Syndrome", "Endometriosis", "Prostate Cancer", "Breast Cancer", "Leukemia",
    "Lymphoma", "Skin Cancer", "Colon Cancer", "Esophageal Cancer", "Parkinson's Disease", "Huntington's Disease",
    "Pylonephritis", "Infections of the skin and subcutaneous tissue", "Genital herpes", "Kidney stones",
    "Urinary tract infections", "Laryngitis", "Appendicitis", "Gallbladder inflammation", "Scoliosis",
    "Carpal tunnel syndrome", "Gingivitis", "Tonsillitis"
]

# Function to make predictions based on selected symptoms
def predict_disease(selected_symptoms):
    """
    Creates a symptom vector and predicts the disease using the loaded model.
    """
    # Create a vector of zeros with the length of the full symptom list
    symptoms_vector = np.zeros(len(symptom_list))
    
    # Set the value to 1 for each symptom present in the user's selection
    for i, symptom in enumerate(symptom_list):
        if symptom in selected_symptoms:
            symptoms_vector[i] = 1
    
    # Reshape for the model
    input_vector = symptoms_vector.reshape(1, -1)
    
    # Make prediction
    try:
        prediction_index = model.predict(input_vector)[0]
        # Return the corresponding disease name or "Unknown" if index is out of bounds
        return disease_list[prediction_index] if 0 <= prediction_index < len(disease_list) else "Unknown Disease"
    except Exception as e:
        st.error(f"Prediction failed: {e}")
        return "Prediction Error"


# --- Main page content function ---
def show_page():
    """
    This function renders the UI for the Smart Doctor page.
    """
    st.title("SMART MEDICL DIAGNOSIS AI")
    st.subheader("Enter your symptoms below to get a diagnosis.")

    # Symptom Selection and Input
    selected_symptoms = st.multiselect("Choose your symptoms", symptom_list)
    typed_symptoms = st.text_input("Or type your symptoms, separated by commas (e.g., Headache, Fever)")
    
    if st.button("Predict Disease", key="predict_smart_doctor"):
        # Combine selected and typed symptoms, filtering out empty strings
        all_symptoms = selected_symptoms + [sym.strip() for sym in typed_symptoms.split(",") if sym.strip()]
        
        if len(all_symptoms) >= 2:
            # Get the prediction
            prediction = predict_disease(all_symptoms)
            # Display the result
            st.success(f"🩺 Predicted Disease: **{prediction}**")
        else:
            st.error("Please enter at least 2 symptoms to get a more accurate prediction.")

# This is a standard entry point for Streamlit apps
if __name__ == '__main__':
    show_page()