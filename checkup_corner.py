import streamlit as st

def show_page():
    """
    Renders the main Check-Up Corner landing page.
    """
    st.title("Welcome to the E-Hospital Check-Up Corner")
    st.markdown("---")
    st.markdown(
        """
        <div style="background-color: #e6f7ff; padding: 20px; border-left: 5px solid #004aad; border-radius: 8px;">
            <p style="font-size: 1.1rem; color: #004aad;">
                This section of the E-Hospital portal provides you with a suite of AI-powered tools and resources to help you
                monitor your health and gain a better understanding of potential symptoms and conditions. These tools are
                designed for informational purposes and should not be considered a substitute for a professional medical
                consultation.
            </p>
        </div>
        """, unsafe_allow_html=True
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.subheader("Available Tools and Resources")
    st.write("Click on any of the options in the sidebar to access the corresponding tool.")
    
    st.markdown("---")
    
    st.subheader("General Health & Symptom Analysis")
    st.markdown(
        """
        <div style="
            border: 2px solid #e0e0e0;
            border-radius: 12px;
            padding: 20px;
            margin: 10px 0;
            background-color: #fafafa;
            box-shadow: 2px 2px 6px rgba(0,0,0,0.05);
        ">
            <h4 style="color:#004aad; font-size:1.3rem;">Smart Doctor</h4>
            <p style="color:#333;">An AI-driven diagnostic tool that predicts potential diseases based on a combination of symptoms you provide.</p>
        </div>
        <div style="
            border: 2px solid #e0e0e0;
            border-radius: 12px;
            padding: 20px;
            margin: 10px 0;
            background-color: #fafafa;
            box-shadow: 2px 2px 6px rgba(0,0,0,0.05);
        ">
            <h4 style="color:#004aad; font-size:1.3rem;">Symptoms Guide</h4>
            <p style="color:#333;">A comprehensive guide to help you understand common symptoms and their potential associations with various diseases.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.subheader("Specific Disease Predictions")
    st.markdown(
        """
        <div style="
            border: 2px solid #e0e0e0;
            border-radius: 12px;
            padding: 20px;
            margin: 10px 0;
            background-color: #fafafa;
            box-shadow: 2px 2px 6px rgba(0,0,0,0.05);
        ">
            <h4 style="color:#004aad; font-size:1.3rem;">BP Diagnosis</h4>
            <p style="color:#333;">AI-based tool to help assess your risk for hypertension based on your health data.</p>
        </div>
        <div style="
            border: 2px solid #e0e0e0;
            border-radius: 12px;
            padding: 20px;
            margin: 10px 0;
            background-color: #fafafa;
            box-shadow: 2px 2px 6px rgba(0,0,0,0.05);
        ">
            <h4 style="color:#004aad; font-size:1.3rem;">Heart Disease Prediction</h4>
            <p style="color:#333;">Predict your risk of developing heart disease using advanced predictive models.</p>
        </div>
        <div style="
            border: 2px solid #e0e0e0;
            border-radius: 12px;
            padding: 20px;
            margin: 10px 0;
            background-color: #fafafa;
            box-shadow: 2px 2px 6px rgba(0,0,0,0.05);
        ">
            <h4 style="color:#004aad; font-size:1.3rem;">Diabetes Prediction</h4>
            <p style="color:#333;">A tool to evaluate your likelihood of having diabetes based on key health indicators.</p>
        </div>
        <div style="
            border: 2px solid #e0e0e0;
            border-radius: 12px;
            padding: 20px;
            margin: 10px 0;
            background-color: #fafafa;
            box-shadow: 2px 2px 6px rgba(0,0,0,0.05);
        ">
            <h4 style="color:#004aad; font-size:1.3rem;">Parkinson's Disease Prediction</h4>
            <p style="color:#333;">An AI model that can help in the early screening for Parkinson's disease.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
