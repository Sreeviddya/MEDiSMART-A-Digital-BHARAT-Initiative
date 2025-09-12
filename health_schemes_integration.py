import streamlit as st
from datetime import date

def show_page():
    """
    This Streamlit application provides detailed information on various government
    health schemes and insurance policies. It includes a simulated UI for
    users to "apply" for these schemes.
    """
    
    st.markdown(
        """
        <style>
            .main { background-color: #f0f2f6; }
            .stButton>button { width: 100%; border-radius: 12px; }
            .stExpander { 
                border-radius: 12px; 
                overflow: hidden;
                border: 1px solid #e2e8f0; /* Light border for all expanders */
            }
            /* Subtle color accents for each expander */
            .stExpander:nth-of-type(1) { background-color: #f0f8ff; border-left: 5px solid #3b82f6; } /* Light blue */
            .stExpander:nth-of-type(2) { background-color: #fffaf0; border-left: 5px solid #f97316; } /* Light orange */
            .stExpander:nth-of-type(3) { background-color: #f0fff4; border-left: 5px solid #22c55e; } /* Light green */
            .stExpander:nth-of-type(4) { background-color: #f5f5f5; border-left: 5px solid #6b7280; } /* Gray */

            .stExpanderContent { padding-top: 1rem; }
            .stForm { background-color: #ffffff; padding: 1.5rem; border-radius: 12px; border: 1px solid #e2e8f0; }
            .stTextInput, .stDateInput, .stTextArea, .stSelectbox { border-radius: 8px; }
            h1, h2, h3 { color: #1a202c; }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title(" Secure Your Health: Government Schemes & Policies")
    st.markdown("---")

    st.markdown(
        """
        <p style='font-size:1.1rem;'>
            Explore comprehensive information on key government health schemes and insurance policies.
            Find out about benefits, eligibility, and a step-by-step guide on how to apply (simulated).
        </p>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("---")

    # --- Scheme Details Section ---
    schemes = [
        {
            "name": "Pradhan Mantri Jan Arogya Yojana (PM-JAY)",
            "description": "Also known as Ayushman Bharat, this is the world's largest government-funded health assurance scheme. It provides a health cover of up to ₹5 lakh per family per year for secondary and tertiary care hospitalization to over 12 crore families.",
            "benefits": [
                "Health cover up to ₹5 lakh per family per year.",
                "Covers pre-hospitalization (3 days) and post-hospitalization (15 days) expenses.",
                "Cashless and paperless access to services at empaneled public and private hospitals."
            ],
            "eligibility": "Families identified based on the socio-economic caste census (SECC) data.",
        },
        {
            "name": "Central Government Health Scheme (CGHS)",
            "description": "A health scheme for Central Government employees, pensioners, and their dependents. It provides comprehensive medical facilities covering various systems of medicine.",
            "benefits": [
                "Medical care through wellness centers and dispensaries.",
                "Cashless facility at empaneled hospitals.",
                "Coverage for hospitalization, specialized treatments, and diagnostic tests."
            ],
            "eligibility": "Serving and retired Central Government employees and their family members.",
        },
        {
            "name": "Rashtriya Swasthya Bima Yojana (RSBY)",
            "description": "A health insurance scheme providing health coverage to unorganized sector workers and their families living below the poverty line (BPL).",
            "benefits": [
                "Smart card-based cashless health insurance up to ₹30,000 per family per year.",
                "Covers hospitalization charges, maternity benefits, and pre-existing conditions.",
                "Transport allowance of ₹100 per visit, up to ₹1,000 per year."
            ],
            "eligibility": "Families identified by the State Governments as BPL.",
        },
        {
            "name": "Employees' State Insurance (ESI)",
            "description": "A self-financing social security and health insurance scheme for Indian workers. It provides medical benefits, sickness benefits, maternity benefits, and dependent benefits to covered employees and their families.",
            "benefits": [
                "Full medical care for the employee and their family from the first day of insurable employment.",
                "Monetary benefits in case of sickness, maternity, or temporary/permanent disablement.",
                "Unemployment allowance under certain conditions."
            ],
            "eligibility": "Employees with a monthly salary up to ₹21,000 (₹25,000 for persons with disabilities).",
        },
    ]

    for scheme in schemes:
        with st.expander(f"**{scheme['name']}**", expanded=True):
            st.markdown(f"**About the Scheme:** {scheme['description']}")
            st.markdown("---")
            
            st.markdown("### Key Benefits")
            for benefit in scheme['benefits']:
                st.markdown(f"- {benefit}")
            
            st.markdown("---")

            st.markdown("### Eligibility")
            st.markdown(f"**Who can apply:** {scheme['eligibility']}")
            
            st.markdown("---")

            # --- Simulated Application Form ---
            st.markdown("### Apply for this Scheme")
            st.markdown(
                """
                <p class='text-sm text-gray-500'>
                    Fill out this form to initiate your application process. This is a simulated application for demonstration purposes only.
                </p>
                """,
                unsafe_allow_html=True
            )
            
            with st.form(key=f"application_form_{scheme['name']}"):
                col1, col2 = st.columns(2)
                
                with col1:
                    name = st.text_input("Full Name", placeholder="e.g., Jane Doe")
                
                with col2:
                    dob = st.date_input("Date of Birth", value=date(1990, 1, 1), max_value=date.today())

                aadhaar = st.text_input("Aadhaar Number", max_chars=12, help="Enter your 12-digit Aadhaar number")
                
                address = st.text_area("Residential Address", placeholder="Street, City, State, ZIP Code")
                
                income_group = st.selectbox(
                    "Annual Income Group",
                    ["Below ₹1,00,000", "₹1,00,000 - ₹5,00,000", "₹5,00,000 - ₹10,00,000", "Above ₹10,00,000"]
                )

                # Every form needs a submit button.
                submitted = st.form_submit_button("Submit Application")
                
                if submitted:
                    if name and aadhaar and address:
                        st.balloons()
                        st.success("🎉 Your application has been successfully submitted! A representative will contact you shortly.")
                        st.markdown("---")
                        st.subheader("Submitted Details (For Demonstration):")
                        st.write(f"**Name:** {name}")
                        st.write(f"**Date of Birth:** {dob}")
                        st.write(f"**Aadhaar Number:** {aadhaar}")
                        st.write(f"**Address:** {address}")
                        st.write(f"**Income Group:** {income_group}")
                    else:
                        st.error("Please fill in all required fields (Name, Aadhaar, Address) to submit.")

# Call the function to display the page when the script is run
if __name__ == "__main__":
    show_page()
