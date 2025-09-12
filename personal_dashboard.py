import streamlit as st
import datetime

def show_page():
    # --- CRITICAL: Check for login status before rendering content ---
    if not st.session_state.get("user_is_logged_in"):
        st.warning("You must be logged in to view your personal dashboard.")
        st.stop()

    st.header(" My Personal Dashboard")
    st.markdown("---")
    
    # Placeholder for a welcome message with the user's name
    st.success("Welcome back, dear! Your personalized health insights are here.")
    st.markdown("---")

    # --- Appointments Section ---
    st.subheader(" My Upcoming Appointments")
    
    # This would be real data from a database in a live app
    appointments = [
        {"date": "2025-11-15", "time": "10:30 AM", "doctor": "Dr. Kavya Sharma", "specialty": "Cardiology"},
        {"date": "2025-11-20", "time": "02:00 PM", "doctor": "Dr. Rohit Singh", "specialty": "Dermatology"},
    ]

    if appointments:
        for appt in appointments:
            st.info(f"**{appt['specialty']} Appointment** with **{appt['doctor']}** on **{appt['date']}** at **{appt['time']}**")
    else:
        st.warning("You have no upcoming appointments.")
        st.button("Book a New Appointment")
        
    st.markdown("---")

    # --- Prescription & Reports Section ---
    st.subheader(" Recent Prescriptions & Reports")
    
    # This would be real data from a database in a live app
    prescriptions = [
        {"date": "2025-10-25", "doctor": "Dr. Kavya Sharma", "medication": "Amlodipine (10mg), daily"},
        {"date": "2025-09-10", "doctor": "Dr. S. K. Gupta", "medication": "Paracetamol (500mg), as needed"},
    ]
    
    reports = [
        {"date": "2025-10-20", "type": "Blood Test Report", "status": "Ready"},
        {"date": "2025-08-01", "type": "X-Ray Scan", "status": "Ready"},
    ]
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Prescriptions**")
        if prescriptions:
            for pres in prescriptions:
                st.write(f"- **{pres['medication']}** from {pres['doctor']} ({pres['date']})")
        else:
            st.info("No recent prescriptions found.")
            
    with col2:
        st.markdown("**Lab Reports**")
        if reports:
            for report in reports:
                st.write(f"- **{report['type']}** from {report['date']} ({report['status']})")
        else:
            st.info("No recent reports found.")
    
    st.markdown("---")
    
    # --- Feedback and Quick Actions ---
    st.subheader(" Quick Actions")
    st.button("View Full Health Records")
    st.button("Request a Prescription Refill")
    st.button("Download My Reports")

    st.markdown("---")
    if st.button("Logout"):
        st.session_state.user_is_logged_in = False
        query_params = {"page": "home"}
        st.experimental_set_query_params(**query_params)
        st.rerun()
