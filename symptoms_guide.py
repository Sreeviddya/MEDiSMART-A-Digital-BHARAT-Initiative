import streamlit as st

def show_page():
    """
    Renders the Symptoms Guide page for the E-Hospital application.
    """
    st.title("Symptoms Guide")
    st.markdown("---")
    st.markdown(
        """
        <div style="background-color: #e6f7ff; padding: 20px; border-left: 5px solid #004aad; border-radius: 8px;">
            <p style="font-size: 1.1rem; color: #004aad;">
                <b style="font-size: 1.3rem;">Disclaimer:</b> The information provided here is for general health awareness only. 
                It is not a substitute for professional medical advice, diagnosis, or treatment. 
                Always seek the advice of your physician or other qualified health provider with any questions you may have 
                regarding a medical condition.
            </p>
        </div>
        """, unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.subheader("Common Symptoms and Their Associated Conditions")
    st.write(
        "This guide helps you understand some common symptoms. Click on a disease to view its typical symptoms."
    )
    
    # Using expanders to make the content collapsible and tidy
    with st.expander("Common Cold & Flu"):
        st.markdown(
            """
            **Common Cold:**
            - **Symptoms:** Runny or stuffy nose, sore throat, cough, congestion, sneezing, mild headache, and a general feeling of being unwell.
            - **Description:** A viral infection of the nose and throat. It is generally harmless and resolves on its own within a week or two.
            
            **Flu (Influenza):**
            - **Symptoms:** High fever, severe body aches, fatigue, dry cough, chills, and headache.
            - **Description:** A contagious respiratory illness caused by influenza viruses. Symptoms are typically more severe than those of a common cold.
            """
        )
        
    with st.expander("Respiratory Issues"):
        st.markdown(
            """
            **Bronchitis:**
            - **Symptoms:** Chronic cough, production of clear or colored mucus, fatigue, shortness of breath, mild fever, and chest discomfort.
            - **Description:** An inflammation of the lining of your bronchial tubes, which carry air to and from your lungs.
            
            **Asthma:**
            - **Symptoms:** Difficulty breathing, chest tightness or pain, wheezing, and coughing, especially at night or early in the morning.
            - **Description:** A chronic disease of the airways that causes inflammation and narrowing of the bronchial tubes.
            
            **Pneumonia:**
            - **Symptoms:** Fever, chills, cough with phlegm, shortness of breath, chest pain when breathing or coughing.
            - **Description:** An infection that inflames the air sacs in one or both lungs, which may fill with fluid or pus.
            """
        )
        
    with st.expander("Gastrointestinal Problems"):
        st.markdown(
            """
            **Gastroenteritis:**
            - **Symptoms:** Nausea, vomiting, diarrhea, abdominal cramps, and sometimes low-grade fever.
            - **Description:** Also known as a stomach bug or stomach flu, it is an inflammation of the stomach and intestines.
            
            **Irritable Bowel Syndrome (IBS):**
            - **Symptoms:** Abdominal pain, bloating, constipation, or diarrhea.
            - **Description:** A chronic disorder that affects the large intestine. Symptoms often vary widely among individuals.
            """
        )

    with st.expander("Chronic Conditions"):
        st.markdown(
            """
            **Diabetes:**
            - **Symptoms:** Frequent urination, excessive thirst, unexplained weight loss, fatigue, and blurred vision.
            - **Description:** A chronic disease that occurs either when the pancreas does not produce enough insulin or when the body cannot effectively use the insulin it produces.
            
            **Hypertension (High Blood Pressure):**
            - **Symptoms:** Often has no noticeable symptoms. Some people may experience headaches, shortness of breath, or nosebleeds.
            - **Description:** A common condition in which the force of the blood against your artery walls is high enough that it may eventually cause health problems, such as heart disease.
            """
        )

    st.markdown("---")
    st.subheader("When to Seek Emergency Medical Attention")
    st.write("Seek immediate medical help if you experience any of the following:")
    st.markdown(
        """
        - **Sudden or severe chest pain**
        - **Difficulty breathing or shortness of breath**
        - **Loss of consciousness or confusion**
        - **Severe allergic reaction with swelling of the face or throat**
        - **Sudden weakness or numbness in the face, arm, or leg**
        - **High fever that does not go down with medication**
        - **Unexplained bleeding or bruising**
        """
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center; color: #555;'>This resource is developed and maintained by the E-Hospital Portal, a government initiative.</p>",
        unsafe_allow_html=True
    )
