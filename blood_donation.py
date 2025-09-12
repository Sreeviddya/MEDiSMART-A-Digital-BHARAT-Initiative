import streamlit as st
import pandas as pd
import json
from datetime import datetime
import io
from PIL import Image
import base64

# Function to display the blood donation page
def show_page():
    # Initialize session state for donors and requests
    if 'donors' not in st.session_state:
        st.session_state.donors = []
    if 'requests' not in st.session_state:
        st.session_state.requests = [
            {
                'blood_type': 'O+',
                'location': 'Chennai General Hospital',
                'urgency': 'High',
                'hospital': 'Chennai General Hospital',
                'contact': '+91-9876543210',
                'timestamp': '2025-09-08 10:30'
            },
            {
                'blood_type': 'A-',
                'location': 'Apollo Hospital, Chennai',
                'urgency': 'Medium',
                'hospital': 'Apollo Hospital',
                'contact': '+91-9876543211',
                'timestamp': '2025-09-08 11:15'
            },
            {
                'blood_type': 'B+',
                'location': 'AIIMS Delhi',
                'urgency': 'High',
                'hospital': 'AIIMS Delhi',
                'contact': '+91-9876543212',
                'timestamp': '2025-09-08 09:45'
            }
        ]

    # Custom CSS for styling
    st.markdown("""
    <style>
        .main-header {
            background: linear-gradient(90deg, #ff6b6b, #ee5a52);
            padding: 2rem;
            border-radius: 10px;
            color: white;
            text-align: center;
            margin-bottom: 2rem;
        }
        .donor-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1.5rem;
            border-radius: 15px;
            color: white;
            margin: 1rem 0;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }
        .urgency-high {
            background-color: #ff4757 !important;
            color: white !important;
            padding: 5px 10px;
            border-radius: 20px;
            font-weight: bold;
        }
        .urgency-medium {
            background-color: #ffa502 !important;
            color: white !important;
            padding: 5px 10px;
            border-radius: 20px;
            font-weight: bold;
        }
        .urgency-low {
            background-color: #2ed573 !important;
            color: white !important;
            padding: 5px 10px;
            border-radius: 20px;
            font-weight: bold;
        }
        .blood-type {
            font-size: 1.5rem;
            font-weight: bold;
            color: #ff6b6b;
            background: white;
            padding: 10px;
            border-radius: 50%;
            width: 60px;
            height: 60px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 10px auto;
        }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("""
    <div class="main-header">
        <h1> Blood Donation Network</h1>
        <p>Connecting donors with those in need - Save lives, donate blood</p>
    </div>
    """, unsafe_allow_html=True)

    # Navigation
    tab1, tab2, tab3, tab4 = st.tabs([" Dashboard", "➕ Create Donor Card", " Upload Donor Card", "ℹ️ About"])

    with tab1:
        st.header("Blood Donation Requests Dashboard")
        
        # Filters
        col1, col2, col3 = st.columns(3)
        with col1:
            blood_type_filter = st.selectbox("Filter by Blood Type", ["All", "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
        with col2:
            urgency_filter = st.selectbox("Filter by Urgency", ["All", "High", "Medium", "Low"])
        with col3:
            location_filter = st.text_input("Filter by Location", placeholder="Enter city or hospital")
        
        # Filter data
        filtered_requests = st.session_state.requests.copy()
        
        if blood_type_filter != "All":
            filtered_requests = [req for req in filtered_requests if req['blood_type'] == blood_type_filter]
        
        if urgency_filter != "All":
            filtered_requests = [req for req in filtered_requests if req['urgency'] == urgency_filter]
        
        if location_filter:
            filtered_requests = [req for req in filtered_requests if location_filter.lower() in req['location'].lower()]
        
        # Display requests
        if filtered_requests:
            # Using a unique key from the request data itself to ensure stability
            for request in filtered_requests:
                # Create a unique key for each button
                button_key = f"contact_{request['hospital']}_{request['timestamp']}"
                
                with st.container():
                    col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 2])
                    
                    with col1:
                        st.markdown(f'<div class="blood-type">{request["blood_type"]}</div>', unsafe_allow_html=True)
                    
                    with col2:
                        st.write("**Location:**")
                        st.write(request["location"])
                    
                    with col3:
                        urgency_class = f"urgency-{request['urgency'].lower()}"
                        st.markdown(f'<span class="{urgency_class}">{request["urgency"]} Priority</span>', unsafe_allow_html=True)
                        st.write("**Hospital:**")
                        st.write(request["hospital"])
                    
                    with col4:
                        st.write("**Contact:**")
                        st.write(request["contact"])
                        st.write("**Time:**")
                        st.write(request["timestamp"])
                    
                    with col5:
                        if st.button(f"Contact Hospital", key=button_key):
                            st.success(f"Contacting {request['hospital']} at {request['contact']}")
                    
                    st.divider()
        else:
            st.info("No blood donation requests match your filters.")
        
        # Add new request section
        st.subheader("Add New Blood Request")
        with st.expander("Hospital: Add Blood Request"):
            with st.form("add_request"):
                col1, col2 = st.columns(2)
                with col1:
                    new_blood_type = st.selectbox("Blood Type Needed", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"], key='new_bt')
                    new_location = st.text_input("Hospital Location", key='new_loc')
                    new_hospital = st.text_input("Hospital Name", key='new_hosp')
                with col2:
                    new_urgency = st.selectbox("Urgency Level", ["High", "Medium", "Low"], key='new_urg')
                    new_contact = st.text_input("Contact Number", placeholder="+91-XXXXXXXXXX", key='new_contact')
                
                if st.form_submit_button("Add Request"):
                    if new_location and new_hospital and new_contact:
                        new_request = {
                            'blood_type': new_blood_type,
                            'location': new_location,
                            'urgency': new_urgency,
                            'hospital': new_hospital,
                            'contact': new_contact,
                            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M')
                        }
                        st.session_state.requests.append(new_request)
                        st.success("Blood request added successfully!")
                        st.rerun()
                    else:
                        st.error("Please fill in all required fields.")

    with tab2:
        st.header("Create Donor Card")
        st.write("Fill in your details to create a digital donor card")
        
        with st.form("donor_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                name = st.text_input("Full Name*", placeholder="Enter your full name", key='d_name')
                age = st.number_input("Age*", min_value=18, max_value=65, value=25, key='d_age')
                blood_type = st.selectbox("Blood Type*", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"], key='d_bt')
                weight = st.number_input("Weight (kg)*", min_value=50, max_value=150, value=60, key='d_wt')
            
            with col2:
                phone = st.text_input("Phone Number*", placeholder="+91-XXXXXXXXXX", key='d_ph')
                email = st.text_input("Email*", placeholder="your.email@example.com", key='d_email')
                city = st.text_input("City*", placeholder="Enter your city", key='d_city')
                last_donation = st.date_input("Last Donation Date", value=None, key='d_ld')
            
            medical_conditions = st.text_area("Medical Conditions (if any)", placeholder="List any medical conditions or medications", key='d_med')
            emergency_contact = st.text_input("Emergency Contact", placeholder="Emergency contact number", key='d_ec')
            
            available = st.checkbox("Available for donation", value=True, key='d_avail')
            terms = st.checkbox("I agree to the terms and conditions*", key='d_terms')
            
            submitted = st.form_submit_button("Create Donor Card")
            
            if submitted:
                if name and age and blood_type and phone and email and city and terms:
                    donor_data = {
                        'name': name,
                        'age': age,
                        'blood_type': blood_type,
                        'weight': weight,
                        'phone': phone,
                        'email': email,
                        'city': city,
                        'last_donation': str(last_donation) if last_donation else "Never",
                        'medical_conditions': medical_conditions,
                        'emergency_contact': emergency_contact,
                        'available': available,
                        'created_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }
                    
                    st.session_state.donors.append(donor_data)
                    
                    # Display donor card
                    st.success("Donor card created successfully!")
                    
                    st.markdown(f"""
                    <div class="donor-card">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <div>
                                <h2> BLOOD DONOR CARD</h2>
                                <h3>{name}</h3>
                                <p><strong>Blood Type:</strong> {blood_type} | <strong>Age:</strong> {age} | <strong>Weight:</strong> {weight}kg</p>
                                <p><strong>Phone:</strong> {phone}</p>
                                <p><strong>City:</strong> {city}</p>
                                <p><strong>Last Donation:</strong> {str(last_donation) if last_donation else "Never"}</p>
                                <p><strong>Status:</strong> {"Available" if available else "Not Available"}</p>
                            </div>
                            <div class="blood-type">
                                {blood_type}
                            </div>
                        </div>
                        <p style="margin-top: 1rem; font-size: 0.8rem; opacity: 0.8;">
                            Card ID: BD{len(st.session_state.donors):04d} | Created: {datetime.now().strftime('%d/%m/%Y')}
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Download card as JSON
                    card_json = json.dumps(donor_data, indent=2)
                    st.download_button(
                        label="Download Donor Card (JSON)",
                        data=card_json,
                        file_name=f"donor_card_{name.replace(' ', '_').lower()}.json",
                        mime="application/json"
                    )
                    st.rerun() # Add a rerun to clear the form fields
                else:
                    st.error("Please fill in all required fields and accept the terms and conditions.")

    with tab3:
        st.header("Upload Donor Card")
        st.write("Upload your existing donor card file")
        
        uploaded_file = st.file_uploader("Choose a donor card file", type=['json', 'txt'], key='uploader')
        
        if uploaded_file is not None:
            try:
                content = uploaded_file.read()
                donor_data = json.loads(content)
                
                st.success("Donor card uploaded successfully!")
                
                # Display uploaded card
                st.markdown(f"""
                <div class="donor-card">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <h2>UPLOADED DONOR CARD</h2>
                            <h3>{donor_data.get('name', 'N/A')}</h3>
                            <p><strong>Blood Type:</strong> {donor_data.get('blood_type', 'N/A')} | 
                               <strong>Age:</strong> {donor_data.get('age', 'N/A')} | 
                               <strong>Weight:</strong> {donor_data.get('weight', 'N/A')}kg</p>
                            <p><strong>Phone:</strong> {donor_data.get('phone', 'N/A')}</p>
                            <p><strong>City:</strong> {donor_data.get('city', 'N/A')}</p>
                            <p><strong>Last Donation:</strong> {donor_data.get('last_donation', 'Never')}</p>
                            <p><strong>Status:</strong> {"Available" if donor_data.get('available', False) else "Not Available"}</p>
                        </div>
                        <div class="blood-type">
                            {donor_data.get('blood_type', '?')}
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Add to session state if not already present
                if donor_data not in st.session_state.donors:
                    if st.button("Add to Database", key='add_db'):
                        st.session_state.donors.append(donor_data)
                        st.success("Donor added to database!")
                        st.rerun()
                
            except json.JSONDecodeError:
                st.error("Invalid JSON file. Please upload a valid donor card file.")
            except Exception as e:
                st.error(f"Error reading file: {str(e)}")
        
        # Display current donors
        if st.session_state.donors:
            st.subheader("Registered Donors")
            donors_df = pd.DataFrame(st.session_state.donors)
            st.dataframe(donors_df[['name', 'blood_type', 'city', 'phone', 'available']], use_container_width=True)

    with tab4:
        st.header("About Blood Donation Network")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader(" Mission")
            st.write("""
            Our mission is to bridge the gap between blood donors and those in need through 
            a seamless digital platform that saves lives by facilitating quick and efficient 
            blood donation connections.
            """)
            
            st.subheader(" Blood Donation Facts")
            st.write("""
            - One donation can save up to 3 lives
            - Every 2 seconds someone needs blood
            - Only 3% of eligible people donate blood
            - Blood cannot be manufactured - it can only come from donors
            - Type O- donors are universal red blood cell donors
            - Type AB+ recipients are universal plasma recipients
            """)
        
        with col2:
            st.subheader(" Features")
            st.write("""
            - **Create Digital Donor Cards**: Generate and store your donor information
            - **Real-time Dashboard**: View urgent blood requests from hospitals
            - **Smart Filtering**: Find requests by blood type, location, and urgency
            - **Upload/Download Cards**: Import and export donor information
            - **Contact Integration**: Direct communication with hospitals and donors
            """)
            
            st.subheader(" Eligibility Criteria")
            st.write("""
            - Age: 18-65 years
            - Weight: Minimum 50kg
            - Healthy with no major medical conditions
            - At least 3 months gap between donations
            - No recent tattoos or piercings (3 months)
            - No alcohol consumption 24 hours before donation
            """)
        
        st.subheader("🚨 Emergency Contacts")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.info("""
            **Red Cross Blood Bank**
            📞 +91-11-23711551
            🌐 www.indianredcross.org
            """)
        
        with col2:
            st.info("""
            **Blood Donation Helpline**
            📞 1910 (Toll-free)
            🕒 24/7 Available
            """)
        
        with col3:
            st.info("""
            **Emergency Services**
            📞 108 (Ambulance)
            📞 102 (Medical Emergency)
            """)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 1rem;">
        <p>Blood Donation Network | Made with love for humanity | © 2025</p>
        <p>Remember: Donate Blood, Save Lives! </p>
    </div>
    """, unsafe_allow_html=True)
