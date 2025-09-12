import streamlit as st

def show_page():
    st.title("Guest Access")
    st.markdown("As a guest, you can access public services and information without needing to register or log in.")

    st.warning("Please note that as a guest user, you will not have access to private features such as your health records, appointment history, or e-Prescriptions.")

    st.markdown("---")
    st.subheader("Search Public Facilities")
    
    # Example for a public-facing search feature
    col1, col2 = st.columns(2)
    with col1:
        search_query = st.text_input("Search for a hospital, clinic, or service...")
    with col2:
        pin_code_search = st.text_input("Search by Pin Code (e.g., 600001)")
    
    if st.button("Search"):
        if search_query or pin_code_search:
            st.success(f"Searching for '{search_query}' in '{pin_code_search}'...")
            # In a real app, this would query a public database of medical facilities
            # and display results.
            st.write("Displaying search results...")
            st.write("1. All India Institute of Medical Sciences (AIIMS)")
            st.write("2. Fortis Hospital, Delhi")
            st.write("3. Apollo Hospitals, Chennai")
        else:
            st.info("Please enter a search query or pin code.")

    st.markdown("---")
    st.subheader("Important Public Notices")
    st.info("This section contains public health advisories, emergency contact numbers, and information on government health schemes.")
    
    with st.expander("National Health Helpline"):
        st.write("**Emergency Ambulance:** 102")
        st.write("**Medical & Health Information:** 1075")
        st.write("**Ayushman Bharat:** 14555")

    with st.expander("Public Health Advisories"):
        st.markdown("- Seasonal flu precautions")
        st.markdown("- COVID-19 vaccination centers")
        st.markdown("- Dengue prevention guidelines")