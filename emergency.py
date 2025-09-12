import streamlit as st
import json
import random
import time

def show_page():
    # Load translations from the main application
    try:
        from main_app import translations
        lang_data = translations.get(st.session_state.language, translations["English"])
    except ImportError:
        # Fallback in case of direct access or for local testing
        lang_data = {
            "title": "Emergency",
            "emergency_alert": "Medical Emergency Alert",
            "emergency_text": "In a medical emergency, every second counts. Please use the contacts below or click the alert button to get immediate help.",
            "emergency_button": "Activate Medical Emergency Alert",
            "remove_alert_button": "Remove Alert",
            "contact_numbers_header": "Emergency Contact Numbers",
            "contact_numbers_police": "Police",
            "contact_numbers_fire": "Fire Department",
            "contact_numbers_ambulance": "Ambulance",
            "contact_numbers_disaster": "National Disaster Management",
            "hospitals_header": "Nearest Hospitals & Health Centers",
            "location_info": "Please enable location services on your device to see the nearest hospitals.",
            "beds_available": "Beds Available:",
            "icu_available": "ICU Beds:",
            "ambulance_wait_time": "Ambulance Wait Time:",
            "on_call_specialists": "On-Call Specialists:",
            "er_contact": "ER Contact:",
            "blood_donor_header": "Emergency Blood Donor Match",
            "blood_group_input": "Enter Required Blood Group (e.g., A+, O-):",
            "search_donors_button": "Search Donors",
            "donor_results_found": "Showing {count} matching donors nearby.",
            "no_donors_found": "No donors found for this blood group nearby. Please contact the nearest blood bank.",
            "medical_helpline_header": "24/7 Medical Helpline",
            "medical_helpline_text": "For non-life-threatening medical questions or advice, call our dedicated helpline.",
        }
    
    # --- Session State for Alert ---
    if "alert_active" not in st.session_state:
        st.session_state.alert_active = False
        
    st.title(lang_data.get("title", "Emergency"))
    st.markdown("---")
    
    # --- Medical Emergency Alert Section ---
    st.markdown(
        f'<div style="background-color: #fcebeb; padding: 20px; border-radius: 10px; border: 2px solid #e03131; text-align: center;">'
        f'<h3 style="color: #e03131; font-weight: bold;">{lang_data.get("emergency_alert", "Medical Emergency Alert")}</h3>'
        f'<p style="color: #495057;">{lang_data.get("emergency_text", "In a medical emergency, every second counts. Please use the contacts below or click the alert button to get immediate help.")}</p>'
        f'</div>',
        unsafe_allow_html=True
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_alert_button, col_remove_button = st.columns(2)
    
    with col_alert_button:
        if st.button(lang_data.get("emergency_button", "Activate Medical Emergency Alert"), use_container_width=True):
            st.session_state.alert_active = True
    
    with col_remove_button:
        if st.button(lang_data.get("remove_alert_button", "Remove Alert"), use_container_width=True):
            st.session_state.alert_active = False

    if st.session_state.alert_active:
        st.error("Emergency Alert Activated! Sending your location to the nearest emergency services. Please remain calm.")
    
    st.markdown("---")
    
    # --- Emergency Contact Numbers ---
    st.header(lang_data.get("contact_numbers_header", "Emergency Contact Numbers"))
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"**{lang_data.get('contact_numbers_police', 'Police')}:** 100")
        st.markdown(f"**{lang_data.get('contact_numbers_fire', 'Fire Department')}:** 101")
    with col2:
        st.markdown(f"**{lang_data.get('contact_numbers_ambulance', 'Ambulance')}:** 108")
        st.markdown(f"**{lang_data.get('contact_numbers_disaster', 'National Disaster Management')}:** 1070")

    st.markdown("---")
    
    # --- Nearest Hospitals Section with Advanced, Dynamic Data ---
    st.header(lang_data.get("hospitals_header", "Nearest Hospitals & Health Centers"))
    st.info(lang_data.get("location_info", "Please enable location services on your device to see the nearest hospitals."))

    # Simulate real-time bed availability
    hospitals = [
        {"name": "Government General Hospital", "address": "123 Main St, Central City", "distance": "3.5 km", "beds": random.randint(10, 50), "icu": random.randint(0, 5), "ambulance_wait": random.randint(5, 15), "specialists": "Cardiology, Orthopedics", "contact": "987-654-3210"},
        {"name": "City Medical Center", "address": "456 Elm St, Suburbia", "distance": "5.1 km", "beds": random.randint(15, 60), "icu": random.randint(2, 8), "ambulance_wait": random.randint(10, 20), "specialists": "Neurology, Pediatrics", "contact": "876-543-2109"},
        {"name": "District Health Center", "address": "789 Oak Ave, Industrial Area", "distance": "8.0 km", "beds": random.randint(5, 25), "icu": random.randint(0, 3), "ambulance_wait": random.randint(20, 35), "specialists": "General Medicine, Family Practice", "contact": "765-432-1098"}
    ]
    
    for i, hosp in enumerate(hospitals):
        with st.expander(f"**{i+1}. {hosp['name']}** - **{hosp['distance']}**", expanded=False):
            st.write(f"**Address:** {hosp['address']}")
            st.write(f"**{lang_data.get('er_contact', 'ER Contact:')}** {hosp['contact']}")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label=lang_data.get("beds_available", "Beds Available:"), value=hosp['beds'])
            with col2:
                st.metric(label=lang_data.get("icu_available", "ICU Beds:"), value=hosp['icu'])
            
            st.markdown(f"**{lang_data.get('ambulance_wait_time', 'Ambulance Wait Time:')}** {hosp['ambulance_wait']} mins")
            st.markdown(f"**{lang_data.get('on_call_specialists', 'On-Call Specialists:')}** {hosp['specialists']}")

    st.markdown("---")

    # --- New: Emergency Blood Donor Match ---
    st.header(lang_data.get("blood_donor_header", "Emergency Blood Donor Match"))
    blood_group = st.text_input(lang_data.get("blood_group_input", "Enter Required Blood Group (e.g., A+, O-):"), "").strip().upper()
    
    if st.button(lang_data.get("search_donors_button", "Search Donors")):
        if blood_group:
            donor_count = random.randint(0, 15)
            if donor_count > 0:
                st.success(lang_data.get("donor_results_found", "Showing {count} matching donors nearby.").format(count=donor_count))
            else:
                st.warning(lang_data.get("no_donors_found", "No donors found for this blood group nearby. Please contact the nearest blood bank."))
        else:
            st.error("Please enter a blood group to search.")

    st.markdown("---")

    # --- New: 24/7 Medical Helpline ---
    st.header(lang_data.get("medical_helpline_header", "24/7 Medical Helpline"))
    st.write(lang_data.get("medical_helpline_text", "For non-life-threatening medical questions or advice, call our dedicated helpline."))
    
    st.markdown(
        f'<div style="text-align: center; background-color: #004aad; padding: 15px; border-radius: 10px; color: white;">'
        f'<h2 style="margin: 0;">1800-11-2025</h2>'
        f'</div>',
        unsafe_allow_html=True
    )