import streamlit as st

def show_page():
    """Renders the Diabetes Diagnosis tool page."""

    st.header(" Diabetes Diagnosis")
    st.markdown("---")
    st.write("Please fill out the form below to get a simulated prediction on your diabetes status.")
    st.markdown("Note: This tool is for informational purposes only. Always consult a healthcare professional for a final diagnosis.")

    # Create the form for user input
    with st.form("diagnosis_form"):
        st.subheader("Patient Information")

        # Define all form inputs
        pregnancies = st.number_input("Pregnancies", min_value=0, max_value=17, value=0, help="Number of times pregnant.")
        glucose = st.number_input("Glucose", min_value=0, max_value=200, value=120, help="Plasma glucose concentration (mg/dL).")
        blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=122, value=70, help="Diastolic blood pressure (mm Hg).")
        skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=99, value=32, help="Triceps skin fold thickness (mm).")
        insulin = st.number_input("Insulin", min_value=0, max_value=846, value=79, help="2-Hour serum insulin (mu U/ml).")
        bmi = st.number_input("BMI (Body Mass Index)", min_value=0.0, max_value=67.1, value=32.0, step=0.1, help="Body Mass Index (weight in kg / (height in m)^2).")
        dpf = st.number_input("Diabetes Pedigree Function", min_value=0.078, max_value=2.42, value=0.471, step=0.001, help="A function that scores the likelihood of diabetes based on family history.")
        age = st.number_input("Age", min_value=1, max_value=120, value=33, help="Age in years.")

        # Add a submit button to the form
        submitted = st.form_submit_button("Get Prediction")

    # This section runs only after the form is submitted
    if submitted:
        try:
            # Simulate a more complex prediction model based on a risk score heuristic
            risk_score = 0
            risk_breakdown = {}

            # Assign risk points based on key health metrics and thresholds
            if pregnancies > 2:
                risk_score += (pregnancies - 2) * 1  # More pregnancies, higher risk
                risk_breakdown["Pregnancies"] = (pregnancies - 2) * 1
            else:
                risk_breakdown["Pregnancies"] = 0

            if glucose > 140:
                risk_score += 2
                risk_breakdown["Glucose"] = 2
            elif glucose > 120:
                risk_score += 1
                risk_breakdown["Glucose"] = 1
            else:
                risk_breakdown["Glucose"] = 0

            if blood_pressure > 90:
                risk_score += 1
                risk_breakdown["Blood Pressure"] = 1
            else:
                risk_breakdown["Blood Pressure"] = 0

            if bmi > 30:
                risk_score += 2
                risk_breakdown["BMI"] = 2
            elif bmi > 25:
                risk_score += 1
                risk_breakdown["BMI"] = 1
            else:
                risk_breakdown["BMI"] = 0

            if dpf > 0.5:
                risk_score += 1
                risk_breakdown["Diabetes Pedigree Function"] = 1
            else:
                risk_breakdown["Diabetes Pedigree Function"] = 0

            if age > 45:
                risk_score += 2
                risk_breakdown["Age"] = 2
            elif age > 35:
                risk_score += 1
                risk_breakdown["Age"] = 1
            else:
                risk_breakdown["Age"] = 0

            st.markdown("---")
            
            # Determine the risk level based on the total score
            if risk_score >= 6:
                st.error("⚠️ **Prediction Result:** Based on the information provided, there is a **very high risk** of diabetes.")
            elif risk_score >= 4:
                st.warning("⚠️ **Prediction Result:** Based on the information provided, there is a **high risk** of diabetes.")
            elif risk_score >= 2:
                st.info("🟡 **Prediction Result:** Based on the information provided, there is a **moderate risk** of diabetes.")
            else:
                st.success("✅ **Prediction Result:** Based on the information provided, the risk of diabetes appears **low**.")
            
            # Display the risk breakdown for a more complex and transparent output
            with st.expander("Show Risk Breakdown"):
                st.write("Here is how each factor contributed to the final risk score:")
                total_risk_points = sum(risk_breakdown.values())
                
                # Using columns for a cleaner layout
                col1, col2, col3 = st.columns([2, 1, 3])
                
                with col1:
                    st.markdown("**Factor**")
                    for key in risk_breakdown:
                        st.markdown(f"- {key}")

                with col2:
                    st.markdown("**Points**")
                    for value in risk_breakdown.values():
                        st.markdown(f"{value}")
                
                with col3:
                    st.markdown("**Contribution**")
                    for key, value in risk_breakdown.items():
                        if total_risk_points > 0:
                            percentage = (value / total_risk_points) * 100
                            st.progress(percentage / 100)
                        else:
                            st.progress(0.0)

                st.markdown(f"**Total Risk Score: {total_risk_points}**")

            st.markdown("---")
            st.info("The prediction logic is a simple heuristic and is not a substitute for a real medical diagnosis.")
        
        except Exception as e:
            st.error("An error occurred during prediction. Please check your inputs.")
            st.exception(e)
