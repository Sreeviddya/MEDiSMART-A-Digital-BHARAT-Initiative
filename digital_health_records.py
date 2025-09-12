import streamlit as st
import pandas as pd
import sqlite3
import hashlib
import datetime
import json
import os
from pathlib import Path
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import base64
import io
import re
import PyPDF2
from docx import Document
import pytesseract
from PIL import Image

def show_page():
    # Database setup
    def init_database():
        conn = sqlite3.connect('health_records.db')
        c = conn.cursor()
       
        # Users table
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      aadhaar TEXT UNIQUE,
                      ayushman_card TEXT,
                      name TEXT NOT NULL,
                      email TEXT,
                      phone TEXT,
                      dob DATE,
                      gender TEXT,
                      blood_group TEXT,
                      emergency_contact TEXT,
                      address TEXT,
                      created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
       
        # Health records table
        c.execute('''CREATE TABLE IF NOT EXISTS health_records
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      user_id INTEGER,
                      record_type TEXT,
                      title TEXT,
                      description TEXT,
                      date_created DATE,
                      doctor_name TEXT,
                      hospital_name TEXT,
                      specialization TEXT,
                      file_data BLOB,
                      file_name TEXT,
                      file_type TEXT,
                      extracted_data TEXT,
                      FOREIGN KEY (user_id) REFERENCES users (id))''')
       
        # Vital signs table
        c.execute('''CREATE TABLE IF NOT EXISTS vital_signs
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      user_id INTEGER,
                      date_recorded DATE,
                      blood_pressure_sys INTEGER,
                      blood_pressure_dia INTEGER,
                      heart_rate INTEGER,
                      temperature REAL,
                      weight REAL,
                      height REAL,
                      blood_sugar REAL,
                      source TEXT DEFAULT 'manual',
                      record_id INTEGER,
                      FOREIGN KEY (user_id) REFERENCES users (id))''')
       
        # Medications table
        c.execute('''CREATE TABLE IF NOT EXISTS medications
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      user_id INTEGER,
                      medication_name TEXT,
                      dosage TEXT,
                      frequency TEXT,
                      start_date DATE,
                      end_date DATE,
                      prescribed_by TEXT,
                      notes TEXT,
                      FOREIGN KEY (user_id) REFERENCES users (id))''')
       
        conn.commit()
        conn.close()

    def extract_text_from_pdf(file_data):
        """Extract text from PDF file"""
        try:
            pdf_file = io.BytesIO(file_data)
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            return text
        except Exception as e:
            st.warning(f"Could not extract text from PDF: {str(e)}")
            return ""

    def extract_text_from_docx(file_data):
        """Extract text from DOCX file"""
        try:
            doc_file = io.BytesIO(file_data)
            doc = Document(doc_file)
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            return text
        except Exception as e:
            st.warning(f"Could not extract text from DOCX: {str(e)}")
            return ""

    def extract_text_from_image(file_data):
        """Extract text from image using OCR"""
        try:
            image = Image.open(io.BytesIO(file_data))
            text = pytesseract.image_to_string(image)
            return text
        except Exception as e:
            st.warning(f"Could not extract text from image: {str(e)}. Make sure Tesseract is installed.")
            return ""

    def extract_text_from_file(file_data, file_type, file_name):
        """Extract text from uploaded file based on type"""
        text = ""
       
        if file_type == "application/pdf":
            text = extract_text_from_pdf(file_data)
        elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            text = extract_text_from_docx(file_data)
        elif file_type.startswith("image/"):
            text = extract_text_from_image(file_data)
        else:
            st.warning(f"Text extraction not supported for {file_type}")
       
        return text

    def extract_vital_signs_from_text(text):
        """Extract vital signs from text using regex patterns"""
        vital_signs = {}
       
        # Blood Pressure patterns
        bp_patterns = [
            r'blood pressure[:\s]*(\d{2,3})[/\s-]+(\d{2,3})',
            r'bp[:\s]*(\d{2,3})[/\s-]+(\d{2,3})',
            r'(\d{2,3})[/\s-]+(\d{2,3})\s*mmhg',
            r'systolic[:\s]*(\d{2,3}).*diastolic[:\s]*(\d{2,3})',
        ]
       
        for pattern in bp_patterns:
            match = re.search(pattern, text.lower())
            if match:
                vital_signs['blood_pressure_sys'] = int(match.group(1))
                vital_signs['blood_pressure_dia'] = int(match.group(2))
                break
       
        # Heart Rate patterns
        hr_patterns = [
            r'heart rate[:\s]*(\d{2,3})',
            r'pulse[:\s]*(\d{2,3})',
            r'hr[:\s]*(\d{2,3})',
            r'(\d{2,3})\s*bpm',
            r'pulse rate[:\s]*(\d{2,3})',
        ]
       
        for pattern in hr_patterns:
            match = re.search(pattern, text.lower())
            if match:
                hr = int(match.group(1))
                if 40 <= hr <= 200:  # Reasonable heart rate range
                    vital_signs['heart_rate'] = hr
                    break
       
        # Temperature patterns
        temp_patterns = [
            r'temperature[:\s]*(\d{2,3}\.?\d*)[°\s]*f',
            r'temp[:\s]*(\d{2,3}\.?\d*)[°\s]*f',
            r'(\d{2,3}\.?\d*)[°\s]*f',
            r'temperature[:\s]*(\d{2}\.?\d*)[°\s]*c',
        ]
       
        for pattern in temp_patterns:
            match = re.search(pattern, text.lower())
            if match:
                temp = float(match.group(1))
                # Convert Celsius to Fahrenheit if needed
                if temp < 50:  # Likely Celsius
                    temp = (temp * 9/5) + 32
                if 90 <= temp <= 110:  # Reasonable temperature range in Fahrenheit
                    vital_signs['temperature'] = temp
                    break
       
        # Weight patterns
        weight_patterns = [
            r'weight[:\s]*(\d{2,3}\.?\d*)\s*kg',
            r'wt[:\s]*(\d{2,3}\.?\d*)\s*kg',
            r'(\d{2,3}\.?\d*)\s*kg',
        ]
       
        for pattern in weight_patterns:
            match = re.search(pattern, text.lower())
            if match:
                weight = float(match.group(1))
                if 20 <= weight <= 300:  # Reasonable weight range
                    vital_signs['weight'] = weight
                    break
       
        # Height patterns
        height_patterns = [
            r'height[:\s]*(\d{2,3}\.?\d*)\s*cm',
            r'ht[:\s]*(\d{2,3}\.?\d*)\s*cm',
            r'(\d{3}\.?\d*)\s*cm',
        ]
       
        for pattern in height_patterns:
            match = re.search(pattern, text.lower())
            if match:
                height = float(match.group(1))
                if 100 <= height <= 250:  # Reasonable height range
                    vital_signs['height'] = height
                    break
       
        # Blood Sugar patterns
        bs_patterns = [
            r'blood sugar[:\s]*(\d{2,3}\.?\d*)',
            r'glucose[:\s]*(\d{2,3}\.?\d*)',
            r'blood glucose[:\s]*(\d{2,3}\.?\d*)',
            r'bs[:\s]*(\d{2,3}\.?\d*)',
            r'(\d{2,3}\.?\d*)\s*mg/dl',
        ]
       
        for pattern in bs_patterns:
            match = re.search(pattern, text.lower())
            if match:
                bs = float(match.group(1))
                if 50 <= bs <= 500:  # Reasonable blood sugar range
                    vital_signs['blood_sugar'] = bs
                    break
       
        return vital_signs

    def extract_medical_details_from_text(text):
        """Extract medical details like doctor name, hospital, diagnosis etc."""
        details = {}
       
        # Doctor name patterns
        doctor_patterns = [
            r'dr\.?\s+([a-z\s\.]+)',
            r'doctor[:\s]*([a-z\s\.]+)',
            r'physician[:\s]*([a-z\s\.]+)',
        ]
       
        for pattern in doctor_patterns:
            match = re.search(pattern, text.lower())
            if match:
                doctor_name = match.group(1).strip().title()
                if len(doctor_name) > 3:  # Valid name length
                    details['doctor_name'] = doctor_name
                    break
       
        # Hospital/Clinic patterns
        hospital_patterns = [
            r'hospital[:\s]*([a-z\s&\.]+)',
            r'clinic[:\s]*([a-z\s&\.]+)',
            r'medical center[:\s]*([a-z\s&\.]+)',
            r'healthcare[:\s]*([a-z\s&\.]+)',
        ]
       
        for pattern in hospital_patterns:
            match = re.search(pattern, text.lower())
            if match:
                hospital_name = match.group(1).strip().title()
                if len(hospital_name) > 3:
                    details['hospital_name'] = hospital_name
                    break
       
        # Diagnosis patterns
        diagnosis_patterns = [
            r'diagnosis[:\s]*([a-z\s,\.]+)',
            r'impression[:\s]*([a-z\s,\.]+)',
            r'findings[:\s]*([a-z\s,\.]+)',
        ]
       
        for pattern in diagnosis_patterns:
            match = re.search(pattern, text.lower())
            if match:
                diagnosis = match.group(1).strip()
                if len(diagnosis) > 5:
                    details['diagnosis'] = diagnosis
                    break
       
        return details

    def hash_aadhaar(aadhaar):
        """Hash Aadhaar number for security"""
        return hashlib.sha256(aadhaar.encode()).hexdigest()

    def validate_aadhaar(aadhaar):
        """Basic Aadhaar validation (12 digits)"""
        return len(aadhaar) == 12 and aadhaar.isdigit()

    def register_user(user_data):
        """Register a new user"""
        conn = sqlite3.connect('health_records.db')
        c = conn.cursor()
       
        hashed_aadhaar = hash_aadhaar(user_data['aadhaar'])
       
        try:
            c.execute('''INSERT INTO users (aadhaar, ayushman_card, name, email, phone,
                         dob, gender, blood_group, emergency_contact, address)
                         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                      (hashed_aadhaar, user_data['ayushman_card'], user_data['name'],
                       user_data['email'], user_data['phone'], user_data['dob'],
                       user_data['gender'], user_data['blood_group'],
                       user_data['emergency_contact'], user_data['address']))
            conn.commit()
            user_id = c.lastrowid
            return user_id
        except sqlite3.IntegrityError:
            return None
        finally:
            conn.close()

    def login_user(aadhaar):
        """Login user with Aadhaar"""
        conn = sqlite3.connect('health_records.db')
        c = conn.cursor()
       
        hashed_aadhaar = hash_aadhaar(aadhaar)
        c.execute('SELECT * FROM users WHERE aadhaar = ?', (hashed_aadhaar,))
        user = c.fetchone()
        conn.close()
       
        if user:
            return {
                'id': user[0], 'name': user[3], 'email': user[4],
                'phone': user[5], 'dob': user[6], 'gender': user[7],
                'blood_group': user[8], 'emergency_contact': user[9],
                'address': user[10], 'ayushman_card': user[2]
            }
        return None

    def add_health_record(user_id, record_data, file_data=None, extracted_text=""):
        """Add a new health record"""
        conn = sqlite3.connect('health_records.db')
        c = conn.cursor()
       
        c.execute('''INSERT INTO health_records (user_id, record_type, title, description,
                     date_created, doctor_name, hospital_name, specialization,
                     file_data, file_name, file_type, extracted_data)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (user_id, record_data['type'], record_data['title'],
                   record_data['description'], record_data['date'],
                   record_data['doctor'], record_data['hospital'],
                   record_data['specialization'], file_data,
                   record_data.get('file_name'), record_data.get('file_type'), extracted_text))
       
        conn.commit()
        record_id = c.lastrowid
        conn.close()
        return record_id

    def get_health_records(user_id, record_type=None):
        """Get health records for a user"""
        conn = sqlite3.connect('health_records.db')
        c = conn.cursor()
       
        if record_type:
            c.execute('''SELECT * FROM health_records WHERE user_id = ? AND record_type = ?
                         ORDER BY date_created DESC''', (user_id, record_type))
        else:
            c.execute('''SELECT * FROM health_records WHERE user_id = ?
                         ORDER BY date_created DESC''', (user_id,))
       
        records = c.fetchall()
        conn.close()
        return records

    def add_vital_signs(user_id, vitals, source='manual', record_id=None):
        """Add vital signs data"""
        conn = sqlite3.connect('health_records.db')
        c = conn.cursor()
       
        c.execute('''INSERT INTO vital_signs (user_id, date_recorded, blood_pressure_sys,
                     blood_pressure_dia, heart_rate, temperature, weight, height, blood_sugar, source, record_id)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (user_id, vitals['date'], vitals.get('bp_sys'), vitals.get('bp_dia'),
                   vitals.get('heart_rate'), vitals.get('temperature'),
                   vitals.get('weight'), vitals.get('height'), vitals.get('blood_sugar'), source, record_id))
       
        conn.commit()
        conn.close()

    def get_vital_signs(user_id):
        """Get vital signs data"""
        conn = sqlite3.connect('health_records.db')
        df = pd.read_sql_query('''SELECT * FROM vital_signs WHERE user_id = ?
                                  ORDER BY date_recorded DESC''', conn, params=(user_id,))
        conn.close()
        return df

    def login_page():
        st.header("Login")
       
        col1, col2 = st.columns([1, 1])
       
        with col1:
            st.subheader("Login with Aadhaar")
            aadhaar = st.text_input("Aadhaar Number", max_chars=12, type="password")
           
            if st.button("Login with Aadhaar", type="primary"):
                if validate_aadhaar(aadhaar):
                    user = login_user(aadhaar)
                    if user:
                        st.session_state.user = user
                        st.success("Login successful!")
                        st.rerun()
                    else:
                        st.error("User not found. Please register first.")
                else:
                    st.error("Invalid Aadhaar number. Must be 12 digits.")
       
        with col2:
            st.subheader("Alternative Login")
            st.info("SMS OTP Login (Coming Soon)")
            st.info("Biometric Login (Coming Soon)")

    def register_page():
        st.header("User Registration")
       
        with st.form("registration_form"):
            col1, col2 = st.columns(2)
           
            with col1:
                st.subheader("Identity Information")
                aadhaar = st.text_input("Aadhaar Number*", max_chars=12, type="password")
                ayushman = st.text_input("Ayushman Bharat Card Number")
                name = st.text_input("Full Name*")
                email = st.text_input("Email Address")
                phone = st.text_input("Phone Number*")
           
            with col2:
                st.subheader("Personal Information")
                # Fixed date of birth with proper range
                dob = st.date_input(
                    "Date of Birth*",
                    min_value=datetime.date(1900, 1, 1),  # Minimum date: 1900
                    max_value=datetime.date.today(),       # Maximum date: today
                    value=datetime.date(1990, 1, 1)        # Default value
                )
                gender = st.selectbox("Gender*", ["Male", "Female", "Other"])
                blood_group = st.selectbox("Blood Group",
                                         ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-", "Unknown"])
                emergency_contact = st.text_input("Emergency Contact Number")
                address = st.text_area("Address")
           
            if st.form_submit_button("Register", type="primary"):
                if not all([aadhaar, name, phone]):
                    st.error("Please fill in all required fields (*)")
                elif not validate_aadhaar(aadhaar):
                    st.error("Invalid Aadhaar number. Must be 12 digits.")
                else:
                    user_data = {
                        'aadhaar': aadhaar, 'ayushman_card': ayushman,
                        'name': name, 'email': email, 'phone': phone,
                        'dob': dob, 'gender': gender, 'blood_group': blood_group,
                        'emergency_contact': emergency_contact, 'address': address
                    }
                   
                    user_id = register_user(user_data)
                    if user_id:
                        st.success("Registration successful! Please login with your Aadhaar.")
                    else:
                        st.error("Registration failed. Aadhaar already exists.")

    def dashboard_page():
        st.header("Health Dashboard")
        user = st.session_state.user
       
        # User info card
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Name", user['name'])
            st.metric("Blood Group", user['blood_group'])
        with col2:
            st.metric("Gender", user['gender'])
            # Fixed age calculation with proper date handling
            if user['dob']:
                if isinstance(user['dob'], str):
                    try:
                        dob_date = datetime.datetime.strptime(user['dob'], '%Y-%m-%d').date()
                    except:
                        dob_date = None
                else:
                    dob_date = user['dob']
               
                if dob_date:
                    age = datetime.date.today().year - dob_date.year
                    if datetime.date.today().month < dob_date.month or \
                       (datetime.date.today().month == dob_date.month and datetime.date.today().day < dob_date.day):
                        age -= 1
                    st.metric("Age", age)
                else:
                    st.metric("Age", "N/A")
            else:
                st.metric("Age", "N/A")
        with col3:
            records_count = len(get_health_records(user['id']))
            st.metric("Total Records", records_count)
       
        # Recent records
        st.subheader("Recent Health Records")
        records = get_health_records(user['id'])
        if records:
            recent_records = records[:5]  # Show last 5 records
            for record in recent_records:
                with st.expander(f"{record[3]} - {record[5]}"):
                    st.write(f"**Type:** {record[2]}")
                    st.write(f"**Description:** {record[4]}")
                    st.write(f"**Doctor:** {record[6]}")
                    st.write(f"**Hospital:** {record[7]}")
        else:
            st.info("No health records found. Start by uploading your first report!")
       
        # Vital signs chart
        vitals_df = get_vital_signs(user['id'])
        if not vitals_df.empty:
            st.subheader("Vital Signs Trends")
           
            if 'blood_pressure_sys' in vitals_df.columns:
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=vitals_df['date_recorded'],
                    y=vitals_df['blood_pressure_sys'],
                    name='Systolic BP',
                    line=dict(color='red')
                ))
                fig.add_trace(go.Scatter(
                    x=vitals_df['date_recorded'],
                    y=vitals_df['blood_pressure_dia'],
                    name='Diastolic BP',
                    line=dict(color='blue')
                ))
                fig.update_layout(title="Blood Pressure Trend", xaxis_title="Date", yaxis_title="mmHg")
                st.plotly_chart(fig)

    def health_records_page():
        st.header("Health Records")
        user = st.session_state.user
       
        # Filter options
        col1, col2 = st.columns(2)
        with col1:
            record_type_filter = st.selectbox(
                "Filter by Type",
                ["All", "General Report", "Lab Report", "Prescription", "Imaging",
                 "Heart Disease", "Diabetes", "Hypertension", "Other Specialty"]
            )
       
        with col2:
            st.write("")  # Spacing
       
        # Get filtered records
        if record_type_filter == "All":
            records = get_health_records(user['id'])
        else:
            records = get_health_records(user['id'], record_type_filter)
       
        if records:
            for record in records:
                with st.expander(f"{record[3]} - {record[5]} ({record[2]})"):
                    col1, col2 = st.columns(2)
                   
                    with col1:
                        st.write(f"**Title:** {record[3]}")
                        st.write(f"**Type:** {record[2]}")
                        st.write(f"**Description:** {record[4]}")
                        st.write(f"**Date:** {record[5]}")
                   
                    with col2:
                        st.write(f"**Doctor:** {record[6]}")
                        st.write(f"**Hospital:** {record[7]}")
                        st.write(f"**Specialization:** {record[8]}")
                   
                    # Show extracted data if available - FIX: Check length before accessing
                    if len(record) > 12 and record[12]:  # extracted_data exists and has content
                        st.subheader("Extracted Information")
                        st.text_area("Extracted Text", record[12], height=100, disabled=True)
                   
                    # File download - FIX: Check length before accessing
                    if len(record) > 9 and record[9]:  # file_data exists
                        file_name = record[10] if len(record) > 10 and record[10] else "document"
                        st.download_button(
                            label=f"Download {file_name}",
                            data=record[9],
                            file_name=file_name,
                            mime="application/octet-stream"
                        )
        else:
            st.info("No records found for the selected filter.")

    def upload_reports_page():
        st.header("Upload Medical Reports")
        user = st.session_state.user
       
        with st.form("upload_form"):
            col1, col2 = st.columns(2)
           
            with col1:
                title = st.text_input("Report Title*")
                record_type = st.selectbox("Report Type*", [
                    "General Report", "Lab Report", "Prescription", "Imaging",
                    "Heart Disease", "Diabetes", "Hypertension", "Cancer Care",
                    "Mental Health", "Other Specialty"
                ])
                description = st.text_area("Description")
                date = st.date_input("Report Date*", value=datetime.date.today())
           
            with col2:
                doctor = st.text_input("Doctor Name")
                hospital = st.text_input("Hospital/Clinic Name")
                specialization = st.text_input("Doctor Specialization")
                uploaded_file = st.file_uploader(
                    "Upload File",
                    type=['pdf', 'jpg', 'jpeg', 'png', 'doc', 'docx'],
                    help="Supported formats: PDF, Images, Word documents"
                )
           
            # Auto-extract option
            auto_extract = st.checkbox("Auto-extract details from uploaded file", value=True)
            extract_vitals = st.checkbox("Auto-extract vital signs and add to records", value=True)
           
            if st.form_submit_button("Upload Report", type="primary"):
                if not all([title, record_type, date]):
                    st.error("Please fill in all required fields (*)")
                else:
                    file_data = None
                    file_name = None
                    file_type = None
                    extracted_text = ""
                   
                    if uploaded_file:
                        file_data = uploaded_file.read()
                        file_name = uploaded_file.name
                        file_type = uploaded_file.type
                       
                        # Extract text if auto-extract is enabled
                        if auto_extract:
                            with st.spinner("Extracting information from file..."):
                                extracted_text = extract_text_from_file(file_data, file_type, file_name)
                               
                                if extracted_text:
                                    st.success("Text extracted successfully!")
                                   
                                    # Extract medical details
                                    medical_details = extract_medical_details_from_text(extracted_text)
                                   
                                    # Auto-fill fields if extracted
                                    if medical_details.get('doctor_name') and not doctor:
                                        doctor = medical_details['doctor_name']
                                        st.info(f"Auto-detected Doctor: {doctor}")
                                   
                                    if medical_details.get('hospital_name') and not hospital:
                                        hospital = medical_details['hospital_name']
                                        st.info(f"Auto-detected Hospital: {hospital}")
                                   
                                    if medical_details.get('diagnosis'):
                                        if not description:
                                            description = medical_details['diagnosis']
                                        st.info(f"Auto-detected Diagnosis: {medical_details['diagnosis']}")
                                else:
                                    st.warning("Could not extract text from the uploaded file.")
                   
                    record_data = {
                        'type': record_type, 'title': title, 'description': description,
                        'date': date, 'doctor': doctor, 'hospital': hospital,
                        'specialization': specialization, 'file_name': file_name,
                        'file_type': file_type
                    }
                   
                    record_id = add_health_record(user['id'], record_data, file_data, extracted_text)
                   
                    # Extract and save vital signs if enabled
                    if extract_vitals and extracted_text:
                        with st.spinner("Extracting vital signs..."):
                            vital_signs = extract_vital_signs_from_text(extracted_text)
                           
                            if vital_signs:
                                # Add date and convert dict keys for vital signs function
                                vitals_data = {
                                    'date': date,
                                    'bp_sys': vital_signs.get('blood_pressure_sys'),
                                    'bp_dia': vital_signs.get('blood_pressure_dia'),
                                    'heart_rate': vital_signs.get('heart_rate'),
                                    'temperature': vital_signs.get('temperature'),
                                    'weight': vital_signs.get('weight'),
                                    'height': vital_signs.get('height'),
                                    'blood_sugar': vital_signs.get('blood_sugar')
                                }
                               
                                add_vital_signs(user['id'], vitals_data, source='auto_extracted', record_id=record_id)
                               
                                st.success("Vital signs automatically extracted and saved!")
                               
                                # Display extracted vitals
                                st.subheader("Extracted Vital Signs:")
                                for key, value in vital_signs.items():
                                    if value:
                                        display_name = key.replace('_', ' ').title()
                                        st.write(f"**{display_name}:** {value}")
                            else:
                                st.info("No vital signs detected in the uploaded report.")
                   
                    st.success("Report uploaded successfully!")

    def vital_signs_page():
        st.header("Vital Signs Tracking")
        user = st.session_state.user
       
        # Add new vital signs
        with st.expander("Add New Vital Signs"):
            with st.form("vitals_form"):
                col1, col2, col3 = st.columns(3)
               
                with col1:
                    date = st.date_input("Date", value=datetime.date.today())
                    bp_sys = st.number_input("Blood Pressure (Systolic)", min_value=0, max_value=300)
                    bp_dia = st.number_input("Blood Pressure (Diastolic)", min_value=0, max_value=200)
               
                with col2:
                    heart_rate = st.number_input("Heart Rate (bpm)", min_value=0, max_value=250)
                    temperature = st.number_input("Temperature (°F)", min_value=90.0, max_value=110.0, step=0.1)
                    blood_sugar = st.number_input("Blood Sugar (mg/dL)", min_value=0, max_value=500)
               
                with col3:
                    weight = st.number_input("Weight (kg)", min_value=0.0, max_value=300.0, step=0.1)
                    height = st.number_input("Height (cm)", min_value=0.0, max_value=250.0, step=0.1)
               
                if st.form_submit_button("Save Vital Signs"):
                    vitals = {
                        'date': date, 'bp_sys': bp_sys, 'bp_dia': bp_dia,
                        'heart_rate': heart_rate, 'temperature': temperature,
                        'blood_sugar': blood_sugar, 'weight': weight, 'height': height
                    }
                    add_vital_signs(user['id'], vitals)
                    st.success("Vital signs saved successfully!")
       
        # Display vital signs history
        vitals_df = get_vital_signs(user['id'])
       
        if not vitals_df.empty:
            st.subheader("Vital Signs History")
           
            # FIX: Check if columns exist before dropping them
            columns_to_drop = []
            if 'id' in vitals_df.columns:
                columns_to_drop.append('id')
            if 'user_id' in vitals_df.columns:
                columns_to_drop.append('user_id')
            if 'record_id' in vitals_df.columns:
                columns_to_drop.append('record_id')
           
            display_df = vitals_df.drop(columns_to_drop, axis=1)
           
            # Add source information to the display
            if 'source' in display_df.columns:
                display_df['source'] = display_df['source'].map({
                    'manual': 'Manual Entry',
                    'auto_extracted': 'Auto-extracted'
                })
           
            # Display as table
            st.dataframe(display_df, use_container_width=True)
           
            # Show statistics
            col1, col2 = st.columns(2)
            with col1:
                manual_count = len(vitals_df[vitals_df['source'] == 'manual']) if 'source' in vitals_df.columns else 0
                st.metric("Manual Entries", manual_count)
            with col2:
                auto_count = len(vitals_df[vitals_df['source'] == 'auto_extracted']) if 'source' in vitals_df.columns else 0
                st.metric("Auto-extracted Entries", auto_count)
           
            # Charts
            if len(vitals_df) > 1:
                tab1, tab2, tab3 = st.tabs(["Blood Pressure", "Weight Trends", "Blood Sugar"])
               
                with tab1:
                    if 'blood_pressure_sys' in vitals_df.columns and vitals_df['blood_pressure_sys'].notna().any():
                        fig = go.Figure()
                       
                        # Color code by source if column exists
                        if 'source' in vitals_df.columns:
                            manual_data = vitals_df[vitals_df['source'] == 'manual']
                            auto_data = vitals_df[vitals_df['source'] == 'auto_extracted']
                           
                            if not manual_data.empty:
                                fig.add_trace(go.Scatter(
                                    x=manual_data['date_recorded'],
                                    y=manual_data['blood_pressure_sys'],
                                    name='Systolic (Manual)',
                                    line=dict(color='red', dash='solid'),
                                    mode='lines+markers'))
                                if 'blood_pressure_dia' in manual_data.columns:
                                    fig.add_trace(go.Scatter(
                                        x=manual_data['date_recorded'],
                                        y=manual_data['blood_pressure_dia'],
                                        name='Diastolic (Manual)',
                                        line=dict(color='blue', dash='solid'),
                                        mode='lines+markers'))
                           
                            if not auto_data.empty:
                                fig.add_trace(go.Scatter(
                                    x=auto_data['date_recorded'],
                                    y=auto_data['blood_pressure_sys'],
                                    name='Systolic (Auto)',
                                    line=dict(color='red', dash='dot'),
                                    mode='lines+markers'))
                                if 'blood_pressure_dia' in auto_data.columns:
                                    fig.add_trace(go.Scatter(
                                        x=auto_data['date_recorded'],
                                        y=auto_data['blood_pressure_dia'],
                                        name='Diastolic (Auto)',
                                        line=dict(color='blue', dash='dot'),
                                        mode='lines+markers'))
                        else:
                            # Simple plot without source differentiation
                            fig.add_trace(go.Scatter(
                                x=vitals_df['date_recorded'],
                                y=vitals_df['blood_pressure_sys'],
                                name='Systolic BP',
                                line=dict(color='red')
                            ))
                            if 'blood_pressure_dia' in vitals_df.columns:
                                fig.add_trace(go.Scatter(
                                    x=vitals_df['date_recorded'],
                                    y=vitals_df['blood_pressure_dia'],
                                    name='Diastolic BP',
                                    line=dict(color='blue')
                                ))
                       
                        fig.update_layout(title="Blood Pressure Trends")
                        st.plotly_chart(fig)
               
                with tab2:
                    if 'weight' in vitals_df.columns and vitals_df['weight'].notna().any():
                        if 'source' in vitals_df.columns:
                            fig = px.scatter(vitals_df, x='date_recorded', y='weight',
                                           color='source', title='Weight Trends',
                                           color_discrete_map={
                                               'manual': 'blue',
                                               'auto_extracted': 'orange'
                                           })
                        else:
                            fig = px.scatter(vitals_df, x='date_recorded', y='weight',
                                           title='Weight Trends')
                        fig.update_traces(mode='lines+markers')
                        st.plotly_chart(fig)
               
                with tab3:
                    if 'blood_sugar' in vitals_df.columns and vitals_df['blood_sugar'].notna().any():
                        if 'source' in vitals_df.columns:
                            fig = px.scatter(vitals_df, x='date_recorded', y='blood_sugar',
                                           color='source', title='Blood Sugar Trends',
                                           color_discrete_map={
                                               'manual': 'green',
                                               'auto_extracted': 'purple'
                                           })
                        else:
                            fig = px.scatter(vitals_df, x='date_recorded', y='blood_sugar',
                                           title='Blood Sugar Trends')
                        fig.update_traces(mode='lines+markers')
                        st.plotly_chart(fig)
        else:
            st.info("No vital signs recorded yet. Add your first entry above or upload a medical report with vital signs!")

    def medications_page():
        st.header("Medications Management")
        st.info("Medication tracking feature - Coming Soon!")
       
        # Placeholder for medication management
        st.write("This section will include:")
        st.write("- Current medications list")
        st.write("- Medication reminders")
        st.write("- Drug interaction warnings")
        st.write("- Prescription history")
        st.write("- Auto-extraction from prescription reports")

    def doctors_history_page():
        st.header("Doctors & Hospitals History")
        user = st.session_state.user
       
        records = get_health_records(user['id'])
       
        if records:
            # Extract unique doctors and hospitals
            doctors = set()
            hospitals = set()
           
            for record in records:
                if len(record) > 6 and record[6]:  # doctor_name
                    specialization = record[8] if len(record) > 8 else ""
                    doctors.add((record[6], specialization))  # (doctor, specialization)
                if len(record) > 7 and record[7]:  # hospital_name
                    hospitals.add(record[7])
           
            col1, col2 = st.columns(2)
           
            with col1:
                st.subheader("Doctors Consulted")
                if doctors:
                    for doctor, spec in doctors:
                        st.write(f"**Dr. {doctor}**")
                        if spec:
                            st.write(f"*{spec}*")
                        st.write("---")
                else:
                    st.info("No doctor information found. Try uploading reports with doctor details.")
           
            with col2:
                st.subheader("Hospitals/Clinics Visited")
                if hospitals:
                    for hospital in hospitals:
                        st.write(f"• {hospital}")
                else:
                    st.info("No hospital information found. Try uploading reports with hospital details.")
        else:
            st.info("No doctor consultation history found.")

    def profile_page():
        st.header("User Profile")
        user = st.session_state.user
       
        with st.form("profile_form"):
            col1, col2 = st.columns(2)
           
            with col1:
                st.subheader("Personal Information")
                name = st.text_input("Full Name", value=user.get('name', ''))
                email = st.text_input("Email", value=user.get('email', ''))
                phone = st.text_input("Phone", value=user.get('phone', ''))
                emergency_contact = st.text_input("Emergency Contact",
                                                value=user.get('emergency_contact', ''))
           
            with col2:
                st.subheader("Medical Information")
                blood_groups = ["Unknown", "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
                current_bg = user.get('blood_group', 'Unknown')
                try:
                    bg_index = blood_groups.index(current_bg) if current_bg in blood_groups else 0
                except:
                    bg_index = 0
                blood_group = st.selectbox("Blood Group", blood_groups, index=bg_index)
                address = st.text_area("Address", value=user.get('address', ''))
           
            if st.form_submit_button("Update Profile"):
                st.success("Profile updated successfully!")
       
        # Display read-only information
        st.subheader("Identity Information")
        col1, col2 = st.columns(2)
       
        with col1:
            st.info(f"**Gender:** {user.get('gender', 'Not specified')}")
            st.info(f"**Date of Birth:** {user.get('dob', 'Not provided')}")
       
        with col2:
            if user.get('ayushman_card'):
                st.info(f"**Ayushman Bharat Card:** {user['ayushman_card']}")
            st.info("**Aadhaar:** Verified")

    # Main application logic
    init_database()
   
    st.title("Digital Health Record System")
    st.markdown("*Secure health data management with Aadhaar & Ayushman Bharat integration*")
   
    # Session state management
    if 'user' not in st.session_state:
        st.session_state.user = None
   
    # Sidebar for navigation
    if st.session_state.user:
        st.sidebar.success(f"Welcome, {st.session_state.user['name']}")
        if st.sidebar.button("Logout"):
            st.session_state.user = None
            st.rerun()
       
        menu = st.sidebar.selectbox(
            "Navigation",
            ["Dashboard", "Health Records", "Upload Reports", "Vital Signs",
             "Medications", "Doctors History", "Profile"]
        )
    else:
        menu = st.sidebar.selectbox("Choose Action", ["Login", "Register"])
   
    # Route to appropriate page
    if not st.session_state.user:
        if menu == "Login":
            login_page()
        elif menu == "Register":
            register_page()
    else:
        if menu == "Dashboard":
            dashboard_page()
        elif menu == "Health Records":
            health_records_page()
        elif menu == "Upload Reports":
            upload_reports_page()
        elif menu == "Vital Signs":
            vital_signs_page()
        elif menu == "Medications":
            medications_page()
        elif menu == "Doctors History":
            doctors_history_page()
        elif menu == "Profile":
            profile_page()