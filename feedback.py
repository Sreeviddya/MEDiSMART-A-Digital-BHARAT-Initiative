import streamlit as st
from datetime import datetime
import json
import os

# --- Custom CSS for the feedback page ---
# This CSS is specific to the feedback page to avoid conflicts with app.py's global styles.
st.markdown("""
<style>
    .feedback-container {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        border: 1px solid #e0e0e0;
        margin-bottom: 1rem;
    }
    
    .success-message {
        background: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid #c3e6cb;
        margin: 1rem 0;
    }
    
    .stTextArea textarea {
        border-radius: 8px;
        border: 2px solid #e0e0e0;
    }
    
    .stSelectbox > div > div {
        border-radius: 8px;
    }
    
    .stButton.feedback-btn button {
        background: linear-gradient(90deg, #28a745, #20c997);
        border: none;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .stButton.feedback-btn button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    
    .footer {
        margin-top: 2rem;
        padding: 2rem;
        text-align: center;
        color: #666;
        border-top: 1px solid #e0e0e0;
        background: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

# --- Helper Functions ---
def save_feedback(feedback_data):
    """Saves feedback data to a JSON file."""
    filename = "hospital_feedback.json"
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            try:
                existing_data = json.load(f)
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []
    
    existing_data.append(feedback_data)
    
    with open(filename, 'w') as f:
        json.dump(existing_data, f, indent=2, default=str)

def generate_feedback_id():
    """Generates a unique feedback ID based on the current timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"FB{timestamp}"

# --- Main Page Function for Feedback ---
def show_page():
    """Renders the entire feedback form page."""
    # Initialize session state variables specific to this page
    if 'feedback_submitted' not in st.session_state:
        st.session_state.feedback_submitted = False
    if 'feedback_id' not in st.session_state:
        st.session_state.feedback_id = None

    # Main header
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1 style="color:#004aad;">E-Hospital Feedback System</h1>
        <p style="color:#333;">Your voice matters - Help us improve our healthcare services</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Check session state to decide which content to show
    if st.session_state.feedback_submitted:
        st.markdown(f"""
        <div class="success-message">
            <h3>Thank You for Your Feedback!</h3>
            <p>Your feedback has been successfully submitted.</p>
            <p><strong>Reference ID:</strong> {st.session_state.feedback_id}</p>
            <p>We typically respond to feedback within 2-3 business days.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Button to go back to the form
        if st.button("Submit Another Feedback", key="new_feedback_btn"):
            st.session_state.feedback_submitted = False
            st.session_state.feedback_id = None
            st.rerun()

    else:
        # Info banner
        st.info("Need Immediate Help? Call Emergency: +91-108 | Feedback Team Available: 24/7")

        # Split the layout into two columns
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown('<div class="feedback-container">', unsafe_allow_html=True)
            
            # Form title
            st.subheader("Share Your Experience")
            
            # Patient Information fields
            st.markdown("<h4>Patient Information</h4>", unsafe_allow_html=True)
            patient_name = st.text_input("Full Name*", placeholder="Enter your full name")
            patient_id = st.text_input("Patient ID (Optional)", placeholder="Enter your patient ID")
            contact_number = st.text_input("Contact Number*", placeholder="Enter your phone number")
            email = st.text_input("Email Address", placeholder="Enter your email (optional)")
            is_anonymous = st.checkbox("Submit as Anonymous Feedback")

            # Visit Information
            st.markdown("<h4>Visit Information</h4>", unsafe_allow_html=True)
            visit_info = st.text_area(
                "Please provide details about your visit (date, time, etc.):",
                height=100,
                placeholder="E.g., Visited on 2025-09-10 for a general check-up..."
            )
            
            st.subheader("Feedback Category")
            feedback_categories = {
                "General Experience": "Overall experience with hospital services",
                "Medical Care": "Quality of medical treatment and care received", 
                "Staff Behavior": "Interaction with doctors, nurses, and support staff",
                "Facilities & Infrastructure": "Hospital facilities, cleanliness, equipment",
            }
            selected_category = st.selectbox(
                "Select the category that best describes your feedback:",
                options=list(feedback_categories.keys())
            )
            st.info(f"{feedback_categories[selected_category]}")

            st.subheader("Priority Level")
            priority_level = st.selectbox(
                "Select priority level:",
                options=["Low", "Medium", "High"],
                index=0  # Default to "Low"
            )
            
            st.subheader("⭐ Overall Rating")
            overall_rating = st.select_slider(
                "Rate your overall experience:",
                options=[1, 2, 3, 4, 5],
                value=3
            )
            st.markdown("⭐" * overall_rating)

            st.subheader("Detailed Feedback")
            feedback_text = st.text_area(
                "Please provide detailed feedback:",
                height=150,
                placeholder="Describe your experience, concerns, or suggestions in detail..."
            )

            st.subheader("Department/Service")
            department = st.text_input(
                "Specific Department/Service (Optional):",
                placeholder="e.g., Cardiology, Emergency, Radiology"
            )
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown("### Feedback Guidelines")
            st.markdown("""
            **Please ensure to:**
            - Be specific and constructive
            - Provide factual information
            - Mention date and time if relevant
            - Include staff names if applicable
            """)
            
            st.markdown("---")
            st.markdown("### Response Time")
            st.markdown("""
            - **General feedback:** 3-5 days
            - **High priority:** 1-2 days
            - **Urgent issues:** Within 24 hours
            """)
            
            st.markdown("---")
            st.markdown("### Contact Information")
            st.markdown("""
            **Email:** feedback@ehospital.com
            **Phone:** +91-XXXX-XXXXXX
            **Address:** [Hospital Address]
            """)

            st.markdown("---")
            st.markdown("### Feedback Statistics")
            st.markdown("""
            **Total Feedback Received:** 1,247
            **This Month:** 89
            **Average Rating:** 4.2/5
            **Response Rate:** 98%
            """)

            st.markdown("---")
            st.markdown("### Privacy Notice")
            st.markdown("Your personal information is secure and will only be used for feedback processing and response purposes.")

        # Submit Button
        st.markdown("---")
        col_submit1, col_submit2, col_submit3 = st.columns([1, 2, 1])
        with col_submit2:
            if st.button("Submit Feedback", key="submit_feedback_btn", use_container_width=True):
                # Validation
                errors = []
                if not is_anonymous and not patient_name.strip():
                    errors.append("Patient name is required")
                if not is_anonymous and not contact_number.strip():
                    errors.append("Contact number is required")
                if not feedback_text.strip():
                    errors.append("Feedback text is required")
                
                if errors:
                    for error in errors:
                        st.error(error)
                else:
                    # Generate feedback ID
                    feedback_id = generate_feedback_id()
                    
                    # Prepare feedback data
                    feedback_data = {
                        "feedback_id": feedback_id,
                        "timestamp": datetime.now(),
                        "patient_name": patient_name if not is_anonymous else "Anonymous",
                        "patient_id": patient_id,
                        "contact_number": contact_number if not is_anonymous else "Anonymous",
                        "email": email if not is_anonymous else "Anonymous",
                        "is_anonymous": is_anonymous,
                        "category": selected_category,
                        "priority_level": priority_level,
                        "overall_rating": overall_rating,
                        "feedback_text": feedback_text,
                        "department": department,
                        "visit_info": visit_info,
                    }
                    
                    # Save feedback
                    save_feedback(feedback_data)
                    
                    # Update session state
                    st.session_state.feedback_submitted = True
                    st.session_state.feedback_id = feedback_id
                    
                    # Rerun to show success message
                    st.rerun()

    # Footer
    st.markdown("""
    <div class="footer">
        <p>© 2024 E-Hospital Feedback System | Committed to Better Healthcare</p>
        <p>For technical support, contact: support@ehospital.com</p>
    </div>
    """, unsafe_allow_html=True)
