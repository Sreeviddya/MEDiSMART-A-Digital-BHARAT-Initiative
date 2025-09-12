import streamlit as st
import pandas as pd
import json
from datetime import datetime
import io

def show_page():
    # Initialize session state
    if 'donors' not in st.session_state:
        st.session_state.donors = []
    if 'requests' not in st.session_state:
        st.session_state.requests = [
            {
                'organ_type': 'Kidney',
                'blood_type': 'O+',
                'location': 'AIIMS Delhi',
                'urgency': 'Critical',
                'hospital': 'All India Institute of Medical Sciences',
                'contact': '+91-9876543210',
                'patient_age': '45',
                'timestamp': '2025-09-08 10:30',
                'status': 'Active'
            },
            {
                'organ_type': 'Liver',
                'blood_type': 'A-',
                'location': 'Apollo Hospital, Chennai',
                'urgency': 'High',
                'hospital': 'Apollo Hospitals Chennai',
                'contact': '+91-9876543211',
                'patient_age': '38',
                'timestamp': '2025-09-08 11:15',
                'status': 'Active'
            },
            {
                'organ_type': 'Heart',
                'blood_type': 'B+',
                'location': 'Fortis Hospital, Mumbai',
                'urgency': 'Critical',
                'hospital': 'Fortis Hospital Mulund',
                'contact': '+91-9876543212',
                'patient_age': '52',
                'timestamp': '2025-09-08 09:45',
                'status': 'Active'
            }
        ]

    # Custom CSS
    st.markdown("""
    <style>
        .main-header {
            background: linear-gradient(135deg, #2c3e50, #34495e);
            padding: 2.5rem;
            border-radius: 12px;
            color: white;
            text-align: center;
            margin-bottom: 2rem;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }
        .donor-card {
            background: linear-gradient(135deg, #34495e 0%, #2c3e50 100%);
            padding: 2rem;
            border-radius: 15px;
            color: white;
            margin: 1rem 0;
            box-shadow: 0 8px 32px rgba(0,0,0,0.15);
            border: 1px solid rgba(255,255,255,0.1);
        }
        .urgency-critical {
            background-color: #e74c3c !important;
            color: white !important;
            padding: 6px 12px;
            border-radius: 20px;
            font-weight: 600;
            font-size: 0.85rem;
        }
        .urgency-high {
            background-color: #f39c12 !important;
            color: white !important;
            padding: 6px 12px;
            border-radius: 20px;
            font-weight: 600;
            font-size: 0.85rem;
        }
        .urgency-medium {
            background-color: #3498db !important;
            color: white !important;
            padding: 6px 12px;
            border-radius: 20px;
            font-weight: 600;
            font-size: 0.85rem;
        }
        .urgency-low {
            background-color: #27ae60 !important;
            color: white !important;
            padding: 6px 12px;
            border-radius: 20px;
            font-weight: 600;
            font-size: 0.85rem;
        }
        .organ-type {
            font-size: 1.2rem;
            font-weight: bold;
            color: #2c3e50;
            background: white;
            padding: 12px;
            border-radius: 10px;
            text-align: center;
            margin: 0 auto 15px auto;
            border: 2px solid #3498db;
            min-width: 80px;
        }
        .request-container {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            margin: 1rem 0;
            border-left: 4px solid #3498db;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            color: #2c3e50;
        }
        .request-info {
            color: #2c3e50 !important;
            font-weight: 500;
            line-height: 1.6;
        }
        .request-info strong {
            color: #34495e !important;
            font-weight: 600;
        }
        .stats-card {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            border-top: 4px solid #3498db;
        }
        .professional-text {
            color: #2c3e50;
            font-weight: 500;
        }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("""
    <div class="main-header">
        <h1>Organ Donation Network</h1>
        <p>Professional platform connecting organ donors with recipients - Transforming lives through the gift of life</p>
    </div>
    """, unsafe_allow_html=True)

    # Navigation
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Dashboard", "Register as Donor", "Upload Donor Card", "Statistics", "Information"])

    with tab1:
        st.header("Organ Donation Requests Dashboard")
        
        # Summary statistics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class="stats-card">
                <h3 style="color: #e74c3c; margin: 0; font-weight: 600;">Critical</h3>
                <h2 style="margin: 0; color: #2c3e50; font-weight: 700;">""" + str(len([r for r in st.session_state.requests if r['urgency'] == 'Critical'])) + """</h2>
                <p style="margin: 0; color: #6c757d; font-weight: 500;">Requests</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="stats-card">
                <h3 style="color: #f39c12; margin: 0; font-weight: 600;">High Priority</h3>
                <h2 style="margin: 0; color: #2c3e50; font-weight: 700;">""" + str(len([r for r in st.session_state.requests if r['urgency'] == 'High'])) + """</h2>
                <p style="margin: 0; color: #6c757d; font-weight: 500;">Requests</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="stats-card">
                <h3 style="color: #27ae60; margin: 0; font-weight: 600;">Total Donors</h3>
                <h2 style="margin: 0; color: #2c3e50; font-weight: 700;">""" + str(len(st.session_state.donors)) + """</h2>
                <p style="margin: 0; color: #6c757d; font-weight: 500;">Registered</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div class="stats-card">
                <h3 style="color: #3498db; margin: 0; font-weight: 600;">Active Requests</h3>
                <h2 style="margin: 0; color: #2c3e50; font-weight: 700;">""" + str(len(st.session_state.requests)) + """</h2>
                <p style="margin: 0; color: #6c757d; font-weight: 500;">Total</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Filters
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            organ_filter = st.selectbox("Filter by Organ Type", ["All", "Kidney", "Liver", "Heart", "Lung", "Pancreas", "Cornea", "Bone Marrow"])
        with col2:
            blood_type_filter = st.selectbox("Filter by Blood Type", ["All", "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
        with col3:
            urgency_filter = st.selectbox("Filter by Urgency", ["All", "Critical", "High", "Medium", "Low"])
        with col4:
            location_filter = st.text_input("Filter by Location", placeholder="Enter city or hospital name")
        
        # Filter data
        filtered_requests = st.session_state.requests.copy()
        
        if organ_filter != "All":
            filtered_requests = [req for req in filtered_requests if req['organ_type'] == organ_filter]
        
        if blood_type_filter != "All":
            filtered_requests = [req for req in filtered_requests if req['blood_type'] == blood_type_filter]
        
        if urgency_filter != "All":
            filtered_requests = [req for req in filtered_requests if req['urgency'] == urgency_filter]
        
        if location_filter:
            filtered_requests = [req for req in filtered_requests if location_filter.lower() in req['location'].lower()]
        
        # Display requests
        if filtered_requests:
            st.subheader(f"Organ Donation Requests ({len(filtered_requests)} found)")
            
            for idx, request in enumerate(filtered_requests):
                st.markdown(f"""
                <div class="request-container">
                    <div style="display: grid; grid-template-columns: 1fr 2fr 2fr 2fr 1fr; gap: 1rem; align-items: center;">
                        <div class="organ-type">{request["organ_type"]}</div>
                        <div class="request-info">
                            <strong>Location:</strong><br>
                            {request["location"]}<br>
                            <strong>Hospital:</strong><br>
                            {request["hospital"]}
                        </div>
                        <div class="request-info">
                            <span class="urgency-{request['urgency'].lower()}">{request["urgency"]} Priority</span><br><br>
                            <strong>Blood Type:</strong> {request["blood_type"]}<br>
                            <strong>Patient Age:</strong> {request["patient_age"]} years
                        </div>
                        <div class="request-info">
                            <strong>Contact:</strong><br>
                            {request["contact"]}<br>
                            <strong>Posted:</strong><br>
                            {request["timestamp"]}<br>
                            <strong>Status:</strong> {request["status"]}
                        </div>
                        <div style="text-align: center;">
                """, unsafe_allow_html=True)
                
                if st.button(f"Contact Hospital", key=f"contact_{idx}", type="primary"):
                    st.success(f"Initiating contact with {request['hospital']} at {request['contact']}")
                
                st.markdown("</div></div></div>", unsafe_allow_html=True)
                
        else:
            st.info("No organ donation requests match your current filters.")
        
        # Add new request section
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("Hospital: Submit New Organ Request")
        with st.expander("Add New Organ Donation Request"):
            with st.form("add_request"):
                col1, col2 = st.columns(2)
                with col1:
                    new_organ_type = st.selectbox("Organ Type Required", ["Kidney", "Liver", "Heart", "Lung", "Pancreas", "Cornea", "Bone Marrow"])
                    new_blood_type = st.selectbox("Patient Blood Type", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
                    new_location = st.text_input("Hospital Location")
                    new_hospital = st.text_input("Hospital Name")
                with col2:
                    new_urgency = st.selectbox("Urgency Level", ["Critical", "High", "Medium", "Low"])
                    new_patient_age = st.number_input("Patient Age", min_value=1, max_value=100, value=45)
                    new_contact = st.text_input("Contact Number", placeholder="+91-XXXXXXXXXX")
                    additional_notes = st.text_area("Additional Medical Notes", placeholder="Any specific requirements or medical conditions")
                
                if st.form_submit_button("Submit Organ Request", type="primary"):
                    if new_location and new_hospital and new_contact:
                        new_request = {
                            'organ_type': new_organ_type,
                            'blood_type': new_blood_type,
                            'location': new_location,
                            'urgency': new_urgency,
                            'hospital': new_hospital,
                            'contact': new_contact,
                            'patient_age': str(new_patient_age),
                            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M'),
                            'status': 'Active',
                            'notes': additional_notes
                        }
                        st.session_state.requests.append(new_request)
                        st.success("Organ donation request submitted successfully!")
                        st.rerun()
                    else:
                        st.error("Please fill in all required fields.")

    with tab2:
        st.header("Register as Organ Donor")
        st.write("Complete the registration form to become a registered organ donor")
        
        with st.form("donor_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                name = st.text_input("Full Name*", placeholder="Enter your complete legal name")
                age = st.number_input("Age*", min_value=18, max_value=75, value=30)
                blood_type = st.selectbox("Blood Type*", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
                weight = st.number_input("Weight (kg)*", min_value=45, max_value=150, value=65)
                height = st.number_input("Height (cm)*", min_value=140, max_value=220, value=170)
            
            with col2:
                phone = st.text_input("Phone Number*", placeholder="+91-XXXXXXXXXX")
                email = st.text_input("Email Address*", placeholder="your.email@example.com")
                address = st.text_area("Complete Address*", placeholder="Enter your full address")
                city = st.text_input("City*", placeholder="Enter your city")
                state = st.text_input("State*", placeholder="Enter your state")
            
            # Organ selection
            st.subheader("Organs Available for Donation")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                kidney = st.checkbox("Kidney")
                liver = st.checkbox("Liver") 
                heart = st.checkbox("Heart")
            
            with col2:
                lungs = st.checkbox("Lungs")
                pancreas = st.checkbox("Pancreas")
                cornea = st.checkbox("Corneas")
            
            with col3:
                bone_marrow = st.checkbox("Bone Marrow")
                skin = st.checkbox("Skin Tissue")
                bone = st.checkbox("Bone Tissue")
            
            # Medical information
            st.subheader("Medical Information")
            col1, col2 = st.columns(2)
            
            with col1:
                medical_conditions = st.text_area("Medical Conditions", placeholder="List any chronic conditions, surgeries, or ongoing treatments")
                medications = st.text_area("Current Medications", placeholder="List all medications you are currently taking")
            
            with col2:
                allergies = st.text_area("Known Allergies", placeholder="List any known allergies")
                lifestyle = st.selectbox("Lifestyle", ["Non-smoker, Non-drinker", "Occasional drinker", "Regular drinker", "Smoker", "Former smoker"])
            
            # Emergency contacts
            st.subheader("Emergency Contacts")
            col1, col2 = st.columns(2)
            
            with col1:
                emergency_name = st.text_input("Emergency Contact Name*", placeholder="Primary emergency contact")
                emergency_phone = st.text_input("Emergency Contact Phone*", placeholder="+91-XXXXXXXXXX")
            
            with col2:
                emergency_relation = st.text_input("Relationship*", placeholder="Spouse, Parent, Sibling, etc.")
                secondary_contact = st.text_input("Secondary Contact (Optional)", placeholder="+91-XXXXXXXXXX")
            
            # Legal declarations
            st.subheader("Legal Declarations")
            living_donor = st.checkbox("I am willing to be a living donor for compatible organs (kidney, liver lobe)")
            deceased_donor = st.checkbox("I consent to organ donation after death")
            family_informed = st.checkbox("I have informed my family about my decision to donate organs*")
            legal_consent = st.checkbox("I understand the legal implications and provide my consent*")
            terms = st.checkbox("I agree to the terms and conditions of organ donation*")
            
            submitted = st.form_submit_button("Register as Organ Donor", type="primary")
            
            if submitted:
                # Collect selected organs
                selected_organs = []
                if kidney: selected_organs.append("Kidney")
                if liver: selected_organs.append("Liver")
                if heart: selected_organs.append("Heart")
                if lungs: selected_organs.append("Lungs")
                if pancreas: selected_organs.append("Pancreas")
                if cornea: selected_organs.append("Corneas")
                if bone_marrow: selected_organs.append("Bone Marrow")
                if skin: selected_organs.append("Skin Tissue")
                if bone: selected_organs.append("Bone Tissue")
                
                if (name and age and blood_type and phone and email and address and city and state and 
                    emergency_name and emergency_phone and emergency_relation and 
                    family_informed and legal_consent and terms and selected_organs):
                    
                    donor_data = {
                        'name': name,
                        'age': age,
                        'blood_type': blood_type,
                        'weight': weight,
                        'height': height,
                        'phone': phone,
                        'email': email,
                        'address': address,
                        'city': city,
                        'state': state,
                        'organs_available': selected_organs,
                        'medical_conditions': medical_conditions,
                        'medications': medications,
                        'allergies': allergies,
                        'lifestyle': lifestyle,
                        'emergency_name': emergency_name,
                        'emergency_phone': emergency_phone,
                        'emergency_relation': emergency_relation,
                        'secondary_contact': secondary_contact,
                        'living_donor': living_donor,
                        'deceased_donor': deceased_donor,
                        'registration_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'donor_id': f"OD{len(st.session_state.donors)+1:06d}",
                        'status': 'Active'
                    }
                    
                    st.session_state.donors.append(donor_data)
                    
                    # Display donor card
                    st.success("Registration completed successfully!")
                    
                    st.markdown(f"""
                    <div class="donor-card">
                        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                            <div style="flex: 1;">
                                <h2>ORGAN DONOR REGISTRATION CARD</h2>
                                <h3>{name}</h3>
                                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1rem 0;">
                                    <div>
                                        <p><strong>Donor ID:</strong> {donor_data['donor_id']}</p>
                                        <p><strong>Blood Type:</strong> {blood_type}</p>
                                        <p><strong>Age:</strong> {age} years</p>
                                        <p><strong>Phone:</strong> {phone}</p>
                                        <p><strong>Location:</strong> {city}, {state}</p>
                                    </div>
                                    <div>
                                        <p><strong>Registration Date:</strong> {datetime.now().strftime('%d/%m/%Y')}</p>
                                        <p><strong>Emergency Contact:</strong> {emergency_name}</p>
                                        <p><strong>Emergency Phone:</strong> {emergency_phone}</p>
                                        <p><strong>Status:</strong> Active Donor</p>
                                    </div>
                                </div>
                                <p><strong>Organs Available:</strong> {', '.join(selected_organs)}</p>
                            </div>
                            <div style="text-align: center; margin-left: 2rem;">
                                <div style="background: white; color: #2c3e50; padding: 1rem; border-radius: 10px; font-weight: bold;">
                                    DONOR<br>{blood_type}
                                </div>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Download card as JSON
                    card_json = json.dumps(donor_data, indent=2)
                    st.download_button(
                        label="Download Donor Registration (JSON)",
                        data=card_json,
                        file_name=f"organ_donor_{name.replace(' ', '_').lower()}.json",
                        mime="application/json",
                        type="primary"
                    )
                else:
                    st.error("Please fill in all required fields, select at least one organ, and accept all necessary declarations.")

    with tab3:
        st.header("Upload Donor Registration")
        st.write("Upload your existing organ donor registration file")
        
        uploaded_file = st.file_uploader("Choose a donor registration file", type=['json', 'txt'])
        
        if uploaded_file is not None:
            try:
                content = uploaded_file.read()
                donor_data = json.loads(content)
                
                st.success("Donor registration file uploaded successfully!")
                
                # Display uploaded card
                organs_list = ', '.join(donor_data.get('organs_available', ['Not specified']))
                
                st.markdown(f"""
                <div class="donor-card">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                        <div style="flex: 1;">
                            <h2>UPLOADED DONOR REGISTRATION</h2>
                            <h3>{donor_data.get('name', 'N/A')}</h3>
                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1rem 0;">
                                <div>
                                    <p><strong>Donor ID:</strong> {donor_data.get('donor_id', 'N/A')}</p>
                                    <p><strong>Blood Type:</strong> {donor_data.get('blood_type', 'N/A')}</p>
                                    <p><strong>Age:</strong> {donor_data.get('age', 'N/A')} years</p>
                                    <p><strong>Phone:</strong> {donor_data.get('phone', 'N/A')}</p>
                                    <p><strong>Location:</strong> {donor_data.get('city', 'N/A')}, {donor_data.get('state', 'N/A')}</p>
                                </div>
                                <div>
                                    <p><strong>Registration:</strong> {donor_data.get('registration_date', 'N/A')}</p>
                                    <p><strong>Emergency Contact:</strong> {donor_data.get('emergency_name', 'N/A')}</p>
                                    <p><strong>Emergency Phone:</strong> {donor_data.get('emergency_phone', 'N/A')}</p>
                                    <p><strong>Status:</strong> {donor_data.get('status', 'N/A')}</p>
                                </div>
                            </div>
                            <p><strong>Organs Available:</strong> {organs_list}</p>
                        </div>
                        <div style="text-align: center; margin-left: 2rem;">
                            <div style="background: white; color: #2c3e50; padding: 1rem; border-radius: 10px; font-weight: bold;">
                                DONOR<br>{donor_data.get('blood_type', '?')}
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Add to session state if not already present
                if donor_data not in st.session_state.donors:
                    if st.button("Add to Database", type="primary"):
                        st.session_state.donors.append(donor_data)
                        st.success("Donor registration added to database!")
                
            except json.JSONDecodeError:
                st.error("Invalid JSON file. Please upload a valid donor registration file.")
            except Exception as e:
                st.error(f"Error reading file: {str(e)}")
        
        # Display current donors
        if st.session_state.donors:
            st.subheader("Registered Organ Donors")
            donors_data = []
            for donor in st.session_state.donors:
                donors_data.append({
                    'Name': donor.get('name', 'N/A'),
                    'Donor ID': donor.get('donor_id', 'N/A'),
                    'Blood Type': donor.get('blood_type', 'N/A'),
                    'City': donor.get('city', 'N/A'),
                    'Phone': donor.get('phone', 'N/A'),
                    'Organs Available': ', '.join(donor.get('organs_available', [])),
                    'Status': donor.get('status', 'N/A')
                })
            
            donors_df = pd.DataFrame(donors_data)
            st.dataframe(donors_df, use_container_width=True, hide_index=True)

    with tab4:
        st.header("Organ Donation Statistics")
        
        if st.session_state.donors or st.session_state.requests:
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Donation Requests by Urgency")
                urgency_counts = {}
                for request in st.session_state.requests:
                    urgency = request['urgency']
                    urgency_counts[urgency] = urgency_counts.get(urgency, 0) + 1
                
                if urgency_counts:
                    urgency_df = pd.DataFrame(list(urgency_counts.items()), columns=['Urgency', 'Count'])
                    st.bar_chart(urgency_df.set_index('Urgency'))
            
            with col2:
                st.subheader("Requests by Organ Type")
                organ_counts = {}
                for request in st.session_state.requests:
                    organ = request['organ_type']
                    organ_counts[organ] = organ_counts.get(organ, 0) + 1
                
                if organ_counts:
                    organ_df = pd.DataFrame(list(organ_counts.items()), columns=['Organ', 'Requests'])
                    st.bar_chart(organ_df.set_index('Organ'))
            
            if st.session_state.donors:
                st.subheader("Donor Demographics")
                col1, col2 = st.columns(2)
                
                with col1:
                    blood_type_counts = {}
                    for donor in st.session_state.donors:
                        bt = donor.get('blood_type', 'Unknown')
                        blood_type_counts[bt] = blood_type_counts.get(bt, 0) + 1
                    
                    if blood_type_counts:
                        bt_df = pd.DataFrame(list(blood_type_counts.items()), columns=['Blood Type', 'Donors'])
                        st.bar_chart(bt_df.set_index('Blood Type'))
                
                with col2:
                    age_groups = {'18-30': 0, '31-45': 0, '46-60': 0, '60+': 0}
                    for donor in st.session_state.donors:
                        age = donor.get('age', 0)
                        if 18 <= age <= 30:
                            age_groups['18-30'] += 1
                        elif 31 <= age <= 45:
                            age_groups['31-45'] += 1
                        elif 46 <= age <= 60:
                            age_groups['46-60'] += 1
                        else:
                            age_groups['60+'] += 1
                    
                    age_df = pd.DataFrame(list(age_groups.items()), columns=['Age Group', 'Donors'])
                    st.bar_chart(age_df.set_index('Age Group'))
        else:
            st.info("No data available for statistics. Register donors and add requests to view analytics.")

    with tab5:
        st.header("Organ Donation Information")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Mission Statement")
            st.write("""
            The Organ Donation Network serves as a comprehensive platform connecting registered 
            organ donors with patients in need of life-saving transplants. Our mission is to 
            facilitate organ matching, reduce waiting times, and save lives through efficient 
            coordination between donors, recipients, and healthcare institutions.
            """)
            
            st.subheader("Key Statistics")
            st.write("""
            - One organ donor can save up to 8 lives
            - Over 150,000 people in India are on organ waiting lists
            - Only 0.01% of Indians are registered organ donors
            - 95% of organ donations come from deceased donors
            - Brain death occurs in less than 2% of hospital deaths
            - Every 10 minutes, someone is added to the organ waiting list
            """)
            
            st.subheader("Types of Donation")
            st.write("""
            **Living Donation:**
            - Kidney (one of two)
            - Liver (partial)
            - Lung (partial)
            - Bone marrow
            
            **Deceased Donation:**
            - Heart, liver, lungs, kidneys, pancreas
            - Corneas, skin, bone, heart valves
            - Small intestine, face, hands
            """)
        
        with col2:
            st.subheader("Platform Features")
            st.write("""
            - **Comprehensive Registration**: Detailed donor profiles with medical history
            - **Real-time Matching**: Advanced algorithms for organ-recipient compatibility
            - **Priority Management**: Urgent requests highlighted for immediate attention  
            - **Secure Data Handling**: HIPAA-compliant data protection and privacy
            - **Multi-hospital Network**: Integration with leading medical institutions
            - **Emergency Protocols**: 24/7 coordination for critical cases
            - **Family Support**: Counseling and support services for donor families
            """)
            
            st.subheader("Eligibility Criteria")
            st.write("""
            **General Requirements:**
            - Age: 18-75 years (varies by organ)
            - Good physical and mental health
            - No active cancer or systemic infections
            - Compatible blood type and tissue matching
            - Informed consent and psychological evaluation
            
            **Living Donor Additional:**
            - Stable social support system
            - Financial independence for recovery period
            - No coercion or financial incentives
            """)
            
            st.subheader("Medical Evaluation Process")
            st.write("""
            1. **Initial Screening**: Medical history and basic compatibility
            2. **Comprehensive Testing**: Blood work, imaging, organ function
            3. **Psychological Assessment**: Mental health and decision evaluation  
            4. **Ethics Committee Review**: Independent evaluation of donation
            5. **Final Approval**: Medical team clearance for donation
            6. **Surgery Scheduling**: Coordinated timing for donor and recipient
            """)
        
        st.subheader("Emergency Contact Information")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.info("""
            **National Organ Tissue Transplant Organization (NOTTO)**
            Contact: +91-11-26588500
            Website: www.notto.gov.in
            24/7 Coordination Center
            """)
        
        with col2:
            st.info("""
            **Organ Donation Helpline**
            Toll-free: 1800-103-7100
            SMS: DONATE to 56161
            Available 24/7 for guidance
            """)
        
        with col3:
            st.info("""
            **Medical Emergency Services**
            Ambulance: 108
            Medical Emergency: 102
            Hospital Networks: Various
            """)
        
        st.subheader("Legal Framework")
        st.write("""
        Organ donation in India is governed by the Transplantation of Human Organs and Tissues Act, 1994, 
        amended in 2011. Key provisions include:
        
        - **Authorization Committee**: State-level bodies overseeing transplant activities
        - **Brain Death Declaration**: Legal framework for deceased donor identification
        - **Tissue Banking**: Regulated storage and distribution of donated tissues
        - **Registry Maintenance**: Central database of donors, recipients, and transplant centers
        - **Quality Standards**: Accreditation requirements for transplant facilities
        """)
        
        st.subheader("Ethical Guidelines")
        st.write("""
        - **Voluntary Consent**: No coercion or financial incentives permitted
        - **Informed Decision**: Full disclosure of risks, benefits, and alternatives
        - **Medical Benefit**: Transplant must provide significant benefit to recipient
        - **Fair Distribution**: Allocation based on medical criteria, not socioeconomic status
        - **Confidentiality**: Strict privacy protection for all parties involved
        - **Follow-up Care**: Comprehensive post-transplant monitoring and support
        """)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 2rem; background-color: #f8f9fa; border-radius: 10px; margin-top: 2rem;">
        <h4 style="color: #2c3e50; margin-bottom: 1rem;">Organ Donation Network</h4>
        <p style="margin: 0.5rem 0;">Professional Healthcare Platform | Transforming Lives Through Organ Donation</p>
        <p style="margin: 0.5rem 0;">Regulated by NOTTO | Compliant with Transplantation Act 1994</p>
        <p style="margin: 0.5rem 0; font-size: 0.9rem; color: #7f8c8d;">© 2025 Organ Donation Network | All Rights Reserved</p>
        <p style="margin-top: 1rem; font-weight: 600; color: #27ae60;">Register Today - Your Decision Can Save Lives</p>
    </div>
    """, unsafe_allow_html=True)

# Call the function to run the app
if __name__ == "__main__":
    show_page()