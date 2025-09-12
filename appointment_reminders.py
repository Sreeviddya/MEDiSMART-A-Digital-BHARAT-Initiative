import streamlit as st
import pandas as pd
import json
from datetime import datetime, timedelta, date
import time

def show_page():
    """
    This function contains all the core logic and UI for the Appointment Reminders System.
    It is designed to be called from a main Streamlit app after a user has authenticated.
    """
    
    # Initialize session state for this module
    if 'user_accounts' not in st.session_state:
        st.session_state.user_accounts = {
            # Admin users
            'admin': {
                'password': 'admin123',
                'role': 'admin',
                'name': 'System Administrator',
                'email': 'admin@hospital.com',
                'phone': '+91-9999999999',
                'department': 'IT Administration'
            },
            'doctor1': {
                'password': 'doc123',
                'role': 'doctor',
                'name': 'Dr. Sarah Wilson',
                'email': 'sarah.wilson@hospital.com',
                'phone': '+91-9876543201',
                'department': 'Cardiology'
            },
            # Staff users
            'staff1': {
                'password': 'staff123',
                'role': 'staff',
                'name': 'Reception Staff',
                'email': 'reception@hospital.com',
                'phone': '+91-9876543202',
                'department': 'Front Desk'
            },
            # Patient users
            'patient1': {
                'password': 'pat123',
                'role': 'patient',
                'name': 'John Doe',
                'email': 'john.doe@example.com',
                'phone': '+91-9876543210',
                'department': 'Patient'
            }
        }

    if 'appointments' not in st.session_state:
        st.session_state.appointments = [
            {
                'id': 'APT001',
                'patient_name': 'John Doe',
                'phone': '+91-9876543210',
                'email': 'john.doe@example.com',
                'appointment_type': 'Consultation',
                'doctor': 'Dr. Sarah Wilson',
                'date': '2025-09-12',
                'time': '10:00 AM',
                'hospital': 'City General Hospital',
                'department': 'Cardiology',
                'status': 'Scheduled',
                'reminder_sent': False,
                'sms_reminder': True,
                'app_reminder': True,
                'notes': 'Follow-up consultation for heart condition',
                'created_date': '2025-09-08'
            },
            {
                'id': 'APT002',
                'patient_name': 'Jane Smith',
                'phone': '+91-9876543211',
                'email': 'jane.smith@example.com',
                'appointment_type': 'Blood Test',
                'doctor': 'Dr. Michael Brown',
                'date': '2025-09-10',
                'time': '02:30 PM',
                'hospital': 'Metro Medical Center',
                'department': 'Laboratory',
                'status': 'Scheduled',
                'reminder_sent': True,
                'sms_reminder': True,
                'app_reminder': True,
                'notes': 'Routine blood work - fasting required',
                'created_date': '2025-09-07'
            },
            {
                'id': 'APT003',
                'patient_name': 'Mike Wilson',
                'phone': '+91-9876543212',
                'email': 'mike.wilson@example.com',
                'appointment_type': 'X-Ray',
                'doctor': 'Dr. Emily Davis',
                'date': '2025-09-15',
                'time': '11:30 AM',
                'hospital': 'Advanced Imaging Center',
                'department': 'Radiology',
                'status': 'Scheduled',
                'reminder_sent': False,
                'sms_reminder': True,
                'app_reminder': False,
                'notes': 'Chest X-ray for annual checkup',
                'created_date': '2025-09-08'
            },
            {
                'id': 'APT004',
                'patient_name': 'Lisa Johnson',
                'phone': '+91-9876543213',
                'email': 'lisa.johnson@example.com',
                'appointment_type': 'MRI Scan',
                'doctor': 'Dr. Robert Lee',
                'date': '2025-09-14',
                'time': '09:15 AM',
                'hospital': 'Diagnostic Excellence Center',
                'department': 'Radiology',
                'status': 'Scheduled',
                'reminder_sent': True,
                'sms_reminder': True,
                'app_reminder': True,
                'notes': 'Brain MRI - remove all metal objects',
                'created_date': '2025-09-06'
            }
        ]

    if 'registered_users' not in st.session_state:
        st.session_state.registered_users = [
            {
                'name': 'John Doe',
                'phone': '+91-9876543210',
                'email': 'john.doe@example.com',
                'preferred_reminder': 'Both',
                'timezone': 'Asia/Kolkata'
            },
            {
                'name': 'Jane Smith',
                'phone': '+91-9876543211',
                'email': 'jane.smith@example.com',
                'preferred_reminder': 'SMS',
                'timezone': 'Asia/Kolkata'
            },
            {
                'name': 'Mike Wilson',
                'phone': '+91-9876543212',
                'email': 'mike.wilson@example.com',
                'preferred_reminder': 'App',
                'timezone': 'Asia/Kolkata'
            },
            {
                'name': 'Lisa Johnson',
                'phone': '+91-9876543213',
                'email': 'lisa.johnson@example.com',
                'preferred_reminder': 'Both',
                'timezone': 'Asia/Kolkata'
            }
        ]
    
    # FIX: Initialize these session state variables to prevent AttributeError
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'current_user' not in st.session_state:
        st.session_state.current_user = None
    if 'user_role' not in st.session_state:
        st.session_state.user_role = None

    # Custom CSS
    st.markdown("""
    <style>
        .login-container {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 3rem;
            border-radius: 20px;
            color: white;
            max-width: 400px;
            margin: 2rem auto;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        }
        .welcome-header {
            background: linear-gradient(90deg, #00b894, #00cec9);
            padding: 1rem 2rem;
            border-radius: 10px;
            color: white;
            margin-bottom: 1rem;
        }
        .role-badge-admin {
            background-color: #e74c3c !important;
            color: white !important;
            padding: 5px 15px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 0.8rem;
        }
        .role-badge-doctor {
            background-color: #3498db !important;
            color: white !important;
            padding: 5px 15px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 0.8rem;
        }
        .role-badge-staff {
            background-color: #f39c12 !important;
            color: white !important;
            padding: 5px 15px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 0.8rem;
        }
        .role-badge-patient {
            background-color: #27ae60 !important;
            color: white !important;
            padding: 5px 15px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 0.8rem;
        }
        .appointment-card {
            background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%);
            padding: 1.5rem;
            border-radius: 15px;
            color: white;
            margin: 1rem 0;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            border-left: 5px solid #00b894;
        }
        .reminder-sent {
            background-color: #00b894 !important;
            color: white !important;
            padding: 5px 15px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 0.8rem;
        }
        .reminder-pending {
            background-color: #fdcb6e !important;
            color: #2d3436 !important;
            padding: 5px 15px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 0.8rem;
        }
        .status-scheduled {
            background-color: #74b9ff !important;
            color: white !important;
            padding: 5px 15px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 0.8rem;
        }
        .status-completed {
            background-color: #00b894 !important;
            color: white !important;
            padding: 5px 15px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 0.8rem;
        }
        .status-cancelled {
            background-color: #e17055 !important;
            color: white !important;
            padding: 5px 15px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 0.8rem;
        }
        .metric-card {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-left: 4px solid #667eea;
        }
        .user-card {
            background: linear-gradient(135deg, #a29bfe 0%, #6c5ce7 100%);
            padding: 1rem;
            border-radius: 10px;
            color: white;
            margin: 0.5rem 0;
        }
        .reminder-type {
            display: inline-block;
            background-color: rgba(255, 255, 255, 0.2);
            padding: 3px 8px;
            border-radius: 12px;
            font-size: 0.7rem;
            margin: 2px;
        }
    </style>
    """, unsafe_allow_html=True)

    # Authentication Functions (assumes st.session_state is available)
    def logout_user():
        st.session_state.logged_in = False
        st.session_state.current_user = None
        st.session_state.user_role = None

    def register_new_user(username, password, role, name, email, phone, department):
        if username not in st.session_state.user_accounts:
            st.session_state.user_accounts[username] = {
                'password': password,
                'role': role,
                'name': name,
                'email': email,
                'phone': phone,
                'department': department
            }
            return True
        return False

    def get_current_user_info():
        if st.session_state.current_user:
            return st.session_state.user_accounts[st.session_state.current_user]
        return None

    def has_permission(required_role):
        if not st.session_state.logged_in:
            return False
        
        user_role = st.session_state.user_role
        
        # Permission hierarchy: admin > doctor > staff > patient
        role_hierarchy = {'admin': 4, 'doctor': 3, 'staff': 2, 'patient': 1}
        
        return role_hierarchy.get(user_role, 0) >= role_hierarchy.get(required_role, 0)

    # Authentication logic
    if not st.session_state.logged_in:
        st.markdown("""
        <div class="login-container">
            <h2 style="text-align: center;">Login to Appointment System</h2>
            <p style="text-align: center;">Use one of the following accounts:</p>
            <ul style="list-style-type: none; padding-left: 0; text-align: center;">
                <li>Admin: admin / admin123</li>
                <li>Doctor: doctor1 / doc123</li>
                <li>Staff: staff1 / staff123</li>
                <li>Patient: patient1 / pat123</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("login_form"):
            username = st.text_input("Username", placeholder="Enter username")
            password = st.text_input("Password", type="password", placeholder="Enter password")
            
            if st.form_submit_button("Login"):
                if username in st.session_state.user_accounts and st.session_state.user_accounts[username]['password'] == password:
                    st.session_state.logged_in = True
                    st.session_state.current_user = username
                    st.session_state.user_role = st.session_state.user_accounts[username]['role']
                    st.success(f"Welcome, {st.session_state.user_accounts[username]['name']}!")
                    time.sleep(1) # Add a small delay for the user to see the success message
                    st.rerun()
                else:
                    st.error("Invalid username or password")
    
    # Main app content only shows after successful login
    if st.session_state.logged_in:
        # Get current user info
        user_info = get_current_user_info()
        
        # Welcome header with user info
        st.markdown(f"""
        <div class="welcome-header">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <h2 style="margin: 0;">Welcome, {user_info['name']}!</h2>
                    <p style="margin: 5px 0;">🏥 {user_info['department']}</p>
                </div>
                <div style="text-align: right;">
                    <span class="role-badge-{user_info['role']}">{user_info['role'].upper()}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Logout button in sidebar
        with st.sidebar:
            st.markdown("### User Profile")
            st.write(f"**Name:** {user_info['name']}")
            st.write(f"**Role:** {user_info['role'].title()}")
            st.write(f"**Email:** {user_info['email']}")
            st.write(f"**Phone:** {user_info['phone']}")
            st.write(f"**Department:** {user_info['department']}")
            
            if st.button("🚪 Logout", use_container_width=True):
                logout_user()
                st.rerun()
        
        # Header
        st.markdown("""
        <div style="background: linear-gradient(90deg, #667eea, #764ba2); padding: 1.5rem; border-radius: 10px; color: white; text-align: center; margin-bottom: 2rem;">
            <h1>🔔 Appointment Reminders System</h1>
            <p>SMS and App-based reminders for scheduled consultations and tests</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Navigation - Role-based access
        if st.session_state.user_role == 'admin':
            selected_tab = st.selectbox("Navigation", [
                "📊 Dashboard", "📅 Schedule Appointment", "👥 Manage Users", 
                "📱 Reminder Settings", "📈 Analytics", "🔐 User Management"
            ])
        elif st.session_state.user_role == 'doctor':
            selected_tab = st.selectbox("Navigation", [
                "📊 Dashboard", "📅 Schedule Appointment", "👥 Manage Users", "📈 Analytics"
            ])
        elif st.session_state.user_role == 'staff':
            selected_tab = st.selectbox("Navigation", [
                "📊 Dashboard", "📅 Schedule Appointment"
            ])
        else:  # patient
            selected_tab = st.selectbox("Navigation", [
                "📋 My Appointments"
            ])
        
        # Display selected tab content
        if selected_tab == "📊 Dashboard" or selected_tab == "📋 My Appointments":
            st.header("Appointment Dashboard")
            
            # Filter appointments based on user role
            if st.session_state.user_role == 'patient':
                user_appointments = [apt for apt in st.session_state.appointments if apt['phone'] == user_info['phone']]
                filtered_appointments = user_appointments
            else:
                filtered_appointments = st.session_state.appointments
            
            # Metrics
            total_appointments = len(filtered_appointments)
            pending_reminders = len([apt for apt in filtered_appointments if not apt['reminder_sent']])
            today_appointments = len([apt for apt in filtered_appointments if apt['date'] == str(date.today())])
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.markdown(f"""
                <div class="metric-card">
                    <h3 style="color: #667eea; margin: 0;">Total Appointments</h3>
                    <h2 style="margin: 5px 0;">{total_appointments}</h2>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="metric-card">
                    <h3 style="color: #e17055; margin: 0;">Pending Reminders</h3>
                    <h2 style="margin: 5px 0;">{pending_reminders}</h2>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown(f"""
                <div class="metric-card">
                    <h3 style="color: #00b894; margin: 0;">Today's Appointments</h3>
                    <h2 style="margin: 5px 0;">{today_appointments}</h2>
                </div>
                """, unsafe_allow_html=True)
            
            with col4:
                st.markdown(f"""
                <div class="metric-card">
                    <h3 style="color: #fdcb6e; margin: 0;">Registered Users</h3>
                    <h2 style="margin: 5px 0;">{len(st.session_state.registered_users)}</h2>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Filters (only for staff and above)
            if has_permission('staff'):
                col1, col2, col3 = st.columns(3)
                with col1:
                    appointment_filter = st.selectbox("Filter by Type", ["All", "Consultation", "Blood Test", "X-Ray", "MRI Scan", "CT Scan"])
                with col2:
                    status_filter = st.selectbox("Filter by Status", ["All", "Scheduled", "Completed", "Cancelled"])
                with col3:
                    reminder_filter = st.selectbox("Reminder Status", ["All", "Sent", "Pending"])
                
                # Apply filters
                if appointment_filter != "All":
                    filtered_appointments = [apt for apt in filtered_appointments if apt['appointment_type'] == appointment_filter]
                
                if status_filter != "All":
                    filtered_appointments = [apt for apt in filtered_appointments if apt['status'] == status_filter]
                
                if reminder_filter == "Sent":
                    filtered_appointments = [apt for apt in filtered_appointments if apt['reminder_sent']]
                elif reminder_filter == "Pending":
                    filtered_appointments = [apt for apt in filtered_appointments if not apt['reminder_sent']]
            
            # Display appointments
            st.subheader("Appointments" if st.session_state.user_role != 'patient' else "My Appointments")
            
            for appointment in filtered_appointments:
                with st.container():
                    col1, col2, col3, col4 = st.columns([3, 2, 2, 2])
                    
                    with col1:
                        st.write(f"**{appointment['patient_name']}**")
                        st.write(f"📞 {appointment['phone']}")
                        st.write(f"📧 {appointment['email']}")
                    
                    with col2:
                        st.write(f"**{appointment['appointment_type']}**")
                        st.write(f"🏥 {appointment['hospital']}")
                        st.write(f"👨‍⚕️ {appointment['doctor']}")
                        st.write(f"🏢 {appointment['department']}")
                    
                    with col3:
                        st.write(f"📅 {appointment['date']}")
                        st.write(f"🕐 {appointment['time']}")
                        
                        status_class = f"status-{appointment['status'].lower()}"
                        st.markdown(f'<span class="{status_class}">{appointment["status"]}</span>', unsafe_allow_html=True)
                    
                    with col4:
                        reminder_class = "reminder-sent" if appointment['reminder_sent'] else "reminder-pending"
                        reminder_text = "Sent ✓" if appointment['reminder_sent'] else "Pending ⏳"
                        st.markdown(f'<span class="{reminder_class}">{reminder_text}</span>', unsafe_allow_html=True)
                        
                        if appointment['sms_reminder']:
                            st.markdown('<span class="reminder-type">📱 SMS</span>', unsafe_allow_html=True)
                        if appointment['app_reminder']:
                            st.markdown('<span class="reminder-type">📲 App</span>', unsafe_allow_html=True)
                        
                        # Only staff and above can send reminders
                        if has_permission('staff') and not appointment['reminder_sent']:
                            if st.button(f"Send Reminder", key=f"remind_{appointment['id']}", type="primary"):
                                appointment['reminder_sent'] = True
                                st.success(f"Reminder sent to {appointment['patient_name']}!")
                                st.rerun()
                    
                    if appointment['notes']:
                        st.write(f"📝 **Notes:** {appointment['notes']}")
                    
                    st.divider()
        
        elif selected_tab == "📅 Schedule Appointment":
            st.header("Schedule New Appointment")
            
            with st.form("schedule_appointment"):
                col1, col2 = st.columns(2)
                
                with col1:
                    patient_name = st.text_input("Patient Name*", placeholder="Enter patient's full name")
                    phone = st.text_input("Phone Number*", placeholder="+91-XXXXXXXXXX")
                    email = st.text_input("Email*", placeholder="patient@example.com")
                    appointment_type = st.selectbox("Appointment Type*", [
                        "Consultation", "Blood Test", "X-Ray", "MRI Scan", 
                        "CT Scan", "Ultrasound", "ECG", "Endoscopy"
                    ])
                    doctor = st.text_input("Doctor*", placeholder="Dr. John Smith")
                
                with col2:
                    appointment_date = st.date_input("Appointment Date*", min_value=date.today())
                    appointment_time = st.time_input("Appointment Time*")
                    hospital = st.text_input("Hospital/Clinic*", placeholder="City General Hospital")
                    department = st.text_input("Department*", placeholder="Cardiology")
                
                col3, col4 = st.columns(2)
                with col3:
                    sms_reminder = st.checkbox("Send SMS Reminder", value=True)
                with col4:
                    app_reminder = st.checkbox("Send App Notification", value=True)
                
                notes = st.text_area("Additional Notes", placeholder="Any special instructions or preparation required")
                
                if st.form_submit_button("Schedule Appointment"):
                    if all([patient_name, phone, email, appointment_type, doctor, hospital, department]):
                        new_appointment = {
                            'id': f'APT{len(st.session_state.appointments) + 1:03d}',
                            'patient_name': patient_name,
                            'phone': phone,
                            'email': email,
                            'appointment_type': appointment_type,
                            'doctor': doctor,
                            'date': str(appointment_date),
                            'time': str(appointment_time.strftime('%I:%M %p')),
                            'hospital': hospital,
                            'department': department,
                            'status': 'Scheduled',
                            'reminder_sent': False,
                            'sms_reminder': sms_reminder,
                            'app_reminder': app_reminder,
                            'notes': notes,
                            'created_date': str(date.today())
                        }
                        
                        st.session_state.appointments.append(new_appointment)
                        st.success("Appointment scheduled successfully!")
                        st.info(f"Appointment ID: {new_appointment['id']}")
                        
                        # Auto-add user if not exists
                        existing_user = next((user for user in st.session_state.registered_users 
                                            if user['phone'] == phone), None)
                        if not existing_user:
                            new_user = {
                                'name': patient_name,
                                'phone': phone,
                                'email': email,
                                'preferred_reminder': 'Both' if (sms_reminder and app_reminder) else 'SMS' if sms_reminder else 'App',
                                'timezone': 'Asia/Kolkata'
                            }
                            st.session_state.registered_users.append(new_user)
                            st.info("User automatically registered for reminders!")
                        
                        st.rerun()
                    else:
                        st.error("Please fill in all required fields.")
        
        elif selected_tab == "👥 Manage Users":
            st.header("Registered Users Management")
            
            # Add new user
            with st.expander("Register New User"):
                with st.form("register_user"):
                    col1, col2 = st.columns(2)
                    with col1:
                        user_name = st.text_input("Full Name", placeholder="Enter full name")
                        user_phone = st.text_input("Phone Number", placeholder="+91-XXXXXXXXXX")
                    with col2:
                        user_email = st.text_input("Email", placeholder="user@example.com")
                        preferred_reminder = st.selectbox("Preferred Reminder Type", ["SMS", "App", "Both"])
                    
                    if st.form_submit_button("Register User"):
                        if all([user_name, user_phone, user_email]):
                            new_user = {
                                'name': user_name,
                                'phone': user_phone,
                                'email': user_email,
                                'preferred_reminder': preferred_reminder,
                                'timezone': 'Asia/Kolkata'
                            }
                            st.session_state.registered_users.append(new_user)
                            st.success("User registered successfully!")
                            st.rerun()
                        else:
                            st.error("Please fill in all fields.")
            
            # Display registered users
            st.subheader("Registered Users")
            
            for idx, user in enumerate(st.session_state.registered_users):
                st.markdown(f"""
                <div class="user-card">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <h4 style="margin: 0;">{user['name']}</h4>
                            <p style="margin: 5px 0;">📞 {user['phone']} | 📧 {user['email']}</p>
                            <span class="reminder-type">Prefers: {user['preferred_reminder']}</span>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Show user's appointments
                user_appointments = [apt for apt in st.session_state.appointments if apt['phone'] == user['phone']]
                if user_appointments:
                    with st.expander(f"Appointments for {user['name']} ({len(user_appointments)})"):
                        for apt in user_appointments:
                            st.write(f"• {apt['appointment_type']} - {apt['date']} at {apt['time']} ({apt['status']})")
        
        elif selected_tab == "📱 Reminder Settings":
            st.header("Reminder Settings & Management")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("📱 SMS Settings")
                sms_enabled = st.checkbox("Enable SMS Reminders", value=True)
                sms_provider = st.selectbox("SMS Provider", ["Twilio", "AWS SNS", "MSG91", "TextLocal"])
                sms_template = st.text_area("SMS Template", value="""Dear {patient_name},
This is a reminder for your {appointment_type} appointment scheduled for {date} at {time} with {doctor} at {hospital}.
Please arrive 15 minutes early.
Contact: {hospital_contact}""")
            
            with col2:
                st.subheader("📲 App Notification Settings")
                app_enabled = st.checkbox("Enable App Notifications", value=True)
                notification_service = st.selectbox("Notification Service", ["Firebase", "OneSignal", "Pusher", "AWS SNS"])
                reminder_timing = st.multiselect("Send Reminders", 
                                               ["24 hours before", "4 hours before", "1 hour before", "30 minutes before"],
                                               default=["24 hours before", "1 hour before"])
            
            st.markdown("---")
            
            st.subheader("🔄 Bulk Reminder Actions")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("Send All Pending SMS", type="primary"):
                    pending_sms = [apt for apt in st.session_state.appointments 
                                  if not apt['reminder_sent'] and apt['sms_reminder']]
                    for apt in pending_sms:
                        apt['reminder_sent'] = True
                    st.success(f"Sent SMS reminders to {len(pending_sms)} patients!")
                    time.sleep(1)
                    st.rerun()
            
            with col2:
                if st.button("Send All App Notifications", type="primary"):
                    pending_app = [apt for apt in st.session_state.appointments 
                                  if not apt['reminder_sent'] and apt['app_reminder']]
                    for apt in pending_app:
                        apt['reminder_sent'] = True
                    st.success(f"Sent app notifications to {len(pending_app)} patients!")
                    time.sleep(1)
                    st.rerun()
            
            with col3:
                if st.button("Test Reminder System"):
                    st.info("Testing reminder system...")
                    time.sleep(2)
                    st.success("✅ SMS Service: Connected\n✅ App Notification: Connected\n✅ Database: Connected")
        
        elif selected_tab == "📈 Analytics":
            st.header("📈 Reminder Analytics")
            
            # Analytics metrics
            total_reminders_sent = len([apt for apt in st.session_state.appointments if apt['reminder_sent']])
            total_sms_reminders = len([apt for apt in st.session_state.appointments if apt['sms_reminder']])
            total_app_reminders = len([apt for apt in st.session_state.appointments if apt['app_reminder']])
            
            st.markdown(f"**Total Reminders Sent:** {total_reminders_sent}")
            st.markdown(f"**Total SMS Reminders:** {total_sms_reminders}")
            st.markdown(f"**Total App Reminders:** {total_app_reminders}")

            # Pie chart of reminder types
            reminder_types = {
                'SMS Only': len([apt for apt in st.session_state.appointments if apt['sms_reminder'] and not apt['app_reminder']]),
                'App Only': len([apt for apt in st.session_state.appointments if apt['app_reminder'] and not apt['sms_reminder']]),
                'Both': len([apt for apt in st.session_state.appointments if apt['sms_reminder'] and apt['app_reminder']]),
                'None': len([apt for apt in st.session_state.appointments if not apt['sms_reminder'] and not apt['app_reminder']])
            }
            
            df_reminder_types = pd.DataFrame(reminder_types.items(), columns=['Type', 'Count'])
            st.subheader("Reminder Type Distribution")
            st.bar_chart(df_reminder_types.set_index('Type'))

            # Chart of appointment status
            status_counts = pd.Series([apt['status'] for apt in st.session_state.appointments]).value_counts()
            df_status = pd.DataFrame({'Status': status_counts.index, 'Count': status_counts.values})
            st.subheader("Appointment Status Distribution")
            st.bar_chart(df_status.set_index('Status'))

        elif selected_tab == "🔐 User Management":
            st.header("🔐 User Management (Admin Only)")
            
            if st.session_state.user_role == 'admin':
                st.write("View and manage all user accounts.")
                
                # Display user accounts in a dataframe
                accounts_list = []
                for username, data in st.session_state.user_accounts.items():
                    accounts_list.append({
                        'Username': username,
                        'Name': data['name'],
                        'Role': data['role'],
                        'Department': data['department'],
                        'Email': data['email']
                    })
                
                df_accounts = pd.DataFrame(accounts_list)
                st.dataframe(df_accounts, use_container_width=True)
                
                # Form to add or remove users
                st.subheader("Add/Remove Users")
                with st.form("manage_user_form"):
                    action = st.radio("Action", ["Add User", "Remove User"])
                    target_username = st.text_input("Username", placeholder="Enter username")
                    
                    if action == "Add User":
                        st.write("Please fill out the details below to add a new user.")
                        add_name = st.text_input("Name")
                        add_password = st.text_input("Password", type="password")
                        add_role = st.selectbox("Role", ["patient", "staff", "doctor", "admin"])
                        add_email = st.text_input("Email")
                        add_phone = st.text_input("Phone")
                        add_department = st.text_input("Department")
                        
                        if st.form_submit_button("Add User", type="primary"):
                            if register_new_user(target_username, add_password, add_role, add_name, add_email, add_phone, add_department):
                                st.success(f"User {target_username} added successfully.")
                                st.rerun()
                            else:
                                st.error("Username already exists.")

                    elif action == "Remove User":
                        if st.form_submit_button("Remove User", type="primary"):
                            if target_username in st.session_state.user_accounts and target_username != 'admin':
                                del st.session_state.user_accounts[target_username]
                                st.success(f"User {target_username} removed successfully.")
                                st.rerun()
                            else:
                                st.error("User not found or cannot remove 'admin' account.")
            else:
                st.warning("You do not have permission to view this page.")
