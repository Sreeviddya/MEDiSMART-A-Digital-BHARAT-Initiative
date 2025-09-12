import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import itertools
from typing import List, Dict, Optional

def show_page():
    # Custom CSS to match the original design
    st.markdown(
        """
        <style>
        /* Card styling */
        .card {
            background-color: #f0f4f8; /* soft gray-blue */
            color: #1a1a1a; /* strong dark text */
            border-radius: 15px;
            padding: 20px;
            margin: 10px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        }
    
        /* Doctor card styling */
        .doctor-card {
            background-color: #ffffff;
            border: 1px solid #e0e7ff;
            border-radius: 12px;
            padding: 20px;
            margin: 10px 0;
            box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
        }
    
        /* Stats box styling */
        .stats-box {
            background-color: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 15px;
        }
    
        /* Hospital info styling */
        .hospital-info {
            background-color: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 15px;
        }
    
        /* Slot styling */
        .slot-booked {
            background-color: #fef2f2;
            color: #991b1b;
            padding: 8px;
            border-radius: 6px;
            text-align: center;
            margin: 5px 0;
            font-size: 0.9rem;
        }
    
        /* Main header styling */
        .main-header {
            margin-bottom: 30px;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 12px;
            color: white;
        }
    
        /* Department heading */
        .card h3 {
            color: #0a3d62; /* deep navy */
            font-weight: 600;
            margin-bottom: 8px;
        }
    
        /* Details */
        .card p {
            color: #2d3436; /* dark gray */
            font-size: 15px;
            margin: 3px 0;
        }
    
        /* Buttons */
        .stButton button {
            border-radius: 8px;
            font-weight: bold;
            padding: 8px 16px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Initialize session state for data persistence
    if 'bookings' not in st.session_state:
        st.session_state.bookings = []
        st.session_state.booking_id_counter = itertools.count(1)
    
    # Sample data (same as original Flask app)
    @st.cache_data
    def load_hospitals():
        return [
            {'id': 1, 'name': 'Green Valley Hospital', 'city': 'Bengaluru', 'lat': 12.9716, 'lon': 77.5946, 'address': '12 Healing Road'},
            {'id': 2, 'name': 'Sunrise Medical Center', 'city': 'Chennai', 'lat': 13.0827, 'lon': 80.2707, 'address': '99 Wellness Ave'},
            {'id': 3, 'name': 'HarborCare Clinic', 'city': 'Kochi', 'lat': 9.9312, 'lon': 76.2673, 'address': '7 Ocean View'},
            {'id': 4, 'name': 'City Care Hospital', 'city': 'Hyderabad', 'lat': 17.3850, 'lon': 78.4867, 'address': '45 Midtown Blvd'},
        ]
    
    @st.cache_data
    def load_doctors():
        return [
            {'id': 1, 'name': 'Dr. Asha R.', 'specialty': 'Cardiology', 'rating': 4.7, 'phone': '080-123456', 'hospital_id': 1},
            {'id': 2, 'name': 'Dr. Rahul K.', 'specialty': 'Orthopedics', 'rating': 4.5, 'phone': '080-234567', 'hospital_id': 1},
            {'id': 3, 'name': 'Dr. Priya M.', 'specialty': 'Neurology', 'rating': 4.8, 'phone': '080-345678', 'hospital_id': 1},
            {'id': 4, 'name': 'Dr. Arvind S.', 'specialty': 'Pediatrics', 'rating': 4.6, 'phone': '080-456789', 'hospital_id': 1},
            {'id': 5, 'name': 'Dr. Meera S.', 'specialty': 'Dermatology', 'rating': 4.6, 'phone': '044-345678', 'hospital_id': 2},
            {'id': 6, 'name': 'Dr. Nikhil T.', 'specialty': 'General Medicine', 'rating': 4.4, 'phone': '044-456789', 'hospital_id': 2},
            {'id': 7, 'name': 'Dr. Kavya L.', 'specialty': 'Gynecology', 'rating': 4.7, 'phone': '044-567890', 'hospital_id': 2},
            {'id': 8, 'name': 'Dr. Ramesh P.', 'specialty': 'ENT', 'rating': 4.5, 'phone': '044-678901', 'hospital_id': 2},
            {'id': 9, 'name': 'Dr. Sanjay R.', 'specialty': 'Orthopedics', 'rating': 4.3, 'phone': '0484-234567', 'hospital_id': 3},
            {'id': 10, 'name': 'Dr. Leela K.', 'specialty': 'Cardiology', 'rating': 4.6, 'phone': '0484-345678', 'hospital_id': 3},
            {'id': 11, 'name': 'Dr. Manoj V.', 'specialty': 'Urology', 'rating': 4.2, 'phone': '0484-456789', 'hospital_id': 3},
            {'id': 12, 'name': 'Dr. Anitha P.', 'specialty': 'Endocrinology', 'rating': 4.4, 'phone': '0484-567890', 'hospital_id': 3},
            {'id': 13, 'name': 'Dr. Priya L.', 'specialty': 'Pediatrics', 'rating': 4.9, 'phone': '040-111222', 'hospital_id': 4},
            {'id': 14, 'name': 'Dr. Kiran V.', 'specialty': 'General Medicine', 'rating': 4.4, 'phone': '040-333444', 'hospital_id': 4},
            {'id': 15, 'name': 'Dr. Sneha M.', 'specialty': 'Dermatology', 'rating': 4.6, 'phone': '040-555666', 'hospital_id': 4},
        ]
    
    # Load data
    hospitals = load_hospitals()
    doctors = load_doctors()
    
    # Helper functions
    def get_hospital(hospital_id: int) -> Optional[Dict]:
        return next((h for h in hospitals if h['id'] == hospital_id), None)
    
    def get_doctor(doctor_id: int) -> Optional[Dict]:
        return next((d for d in doctors if d['id'] == doctor_id), None)
    
    def get_specialties() -> List[str]:
        return sorted(set(d['specialty'] for d in doctors))
    
    def generate_slots_for_doctor(doctor_id: int) -> List[Dict]:
        base = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)
        slots = []
        hours = [9, 10, 11, 14, 15, 16]
        
        for day in range(0, 7):
            day_dt = base + timedelta(days=day)
            for h in hours:
                dt = day_dt.replace(hour=h)
                date_str = dt.strftime('%Y-%m-%d')
                time_str = dt.strftime('%H:%M')
                display = dt.strftime('%a, %d %b %Y %I:%M %p')
                
                # Check if booked
                is_booked = any(
                    b['doctor_id'] == doctor_id and 
                    b['date'] == date_str and 
                    b['time'] == time_str 
                    for b in st.session_state.bookings
                )
                
                slots.append({
                    'date': date_str,
                    'time': time_str,
                    'display': display,
                    'booked': is_booked
                })
        
        return slots
    
    # Initialize session state for navigation
    if 'page' not in st.session_state:
        st.session_state.page = 'search'
    
    if 'selected_doctor' not in st.session_state:
        st.session_state.selected_doctor = None
    
    # Sidebar navigation
    st.sidebar.title("🏥 Appointment Booking")
    
    # Create dropdown for navigation
    nav_options = ["Search Doctors", "View Doctor Profile", "Book Appointment", "My Bookings"]
    page_mapping = {
        "Search Doctors": "search",
        "View Doctor Profile": "doctor_profile", 
        "Book Appointment": "book",
        "My Bookings": "bookings"
    }
    
    # Set default index based on current page
    if st.session_state.page == 'search':
        default_index = 0
    elif st.session_state.page == 'doctor_profile':
        default_index = 1
    elif st.session_state.page == 'book':
        default_index = 2
    elif st.session_state.page == 'bookings':
        default_index = 3
    else:
        default_index = 0
    
    # Dropdown navigation
    selected_nav = st.sidebar.selectbox(
        "Navigate to:",
        nav_options,
        index=default_index,
        key="nav_dropdown"
    )
    
    # Update page if navigation changed
    new_page = page_mapping[selected_nav]
    if new_page != st.session_state.page:
        st.session_state.page = new_page
    
    # Main content based on page
    if st.session_state.page == 'search':
        # Header
        st.markdown("""
        <div class="main-header">
            <h2 style="margin-bottom: 5px;">Find doctors & book appointments</h2>
            <p style="margin-bottom: 0; color: #ffffff;">Select a hospital, filter by specialty or name. Click on a doctor to view profile and book appointments.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Filters
        col1, col2, col3 = st.columns(3)
        
        with col1:
            hospital_options = ['All hospitals'] + [f"{h['name']} — {h['city']}" for h in hospitals]
            selected_hospital_idx = st.selectbox("Select Hospital", range(len(hospital_options)), format_func=lambda x: hospital_options[x])
            selected_hospital = hospitals[selected_hospital_idx - 1] if selected_hospital_idx > 0 else None
        
        with col2:
            specialty_options = ['All specialties'] + get_specialties()
            selected_specialty = st.selectbox("Select Specialty", specialty_options)
        
        with col3:
            doctor_name_search = st.text_input("Search Doctor Name", placeholder="Enter doctor name...")
        
        # Filter doctors
        filtered_doctors = doctors.copy()
        
        if selected_hospital:
            filtered_doctors = [d for d in filtered_doctors if d['hospital_id'] == selected_hospital['id']]
        
        if selected_specialty != 'All specialties':
            filtered_doctors = [d for d in filtered_doctors if selected_specialty.lower() in d['specialty'].lower()]
        
        if doctor_name_search:
            filtered_doctors = [d for d in filtered_doctors if doctor_name_search.lower() in d['name'].lower()]
        
        # Display results
        main_col, sidebar_col = st.columns([2, 1])
        
        with main_col:
            if not filtered_doctors:
                st.info("No doctors found matching your criteria.")
            else:
                # Display doctors in a grid
                for i in range(0, len(filtered_doctors), 2):
                    cols = st.columns(2)
                    for j, col in enumerate(cols):
                        if i + j < len(filtered_doctors):
                            doctor = filtered_doctors[i + j]
                            hospital = get_hospital(doctor['hospital_id'])
                            
                            with col:
                                st.markdown(f"""
                                <div class="doctor-card">
                                    <div style="display: flex; align-items: center; margin-bottom: 15px;">
                                        <div style="width: 56px; height: 56px; border-radius: 50%; background: #eef2ff; display: flex; align-items: center; justify-content: center; font-weight: 600; margin-right: 15px;">
                                            {doctor['name'].split(' ')[1][0] if len(doctor['name'].split(' ')) > 1 else doctor['name'][0]}
                                        </div>
                                        <div style="flex-grow: 1;">
                                            <h5 style="margin-bottom: 5px;">{doctor['name']}</h5>
                                            <div style="color: #6b7280; font-size: 0.9rem;">{doctor['specialty']}</div>
                                            <div style="color: #6b7280; font-size: 0.9rem;">Rating: {doctor['rating']:.1f}</div>
                                            <div style="color: #6b7280; font-size: 0.9rem;">Hospital: {hospital['name'] if hospital else 'N/A'}</div>
                                        </div>
                                    </div>
                                </div>
                                """, unsafe_allow_html=True)
                                
                                # Removed the nested st.columns and placed buttons directly
                                if st.button(f"View Profile", key=f"view_{doctor['id']}", use_container_width=True):
                                    st.session_state.selected_doctor = doctor['id']
                                    st.session_state.page = 'doctor_profile'
                                    st.rerun()
                                if st.button(f"Book Now", key=f"book_{doctor['id']}", use_container_width=True):
                                    st.session_state.selected_doctor = doctor['id']
                                    st.session_state.page = 'book'
                                    st.rerun()
        
        with sidebar_col:
            # Quick stats
            st.markdown(f"""
            <div class="stats-box">
                <h6>Quick Stats</h6>
                <p style="margin-bottom: 5px;"><strong>Hospitals:</strong> {len(hospitals)}</p>
                <p style="margin-bottom: 5px;"><strong>Doctors:</strong> {len(doctors)}</p>
                <p style="margin-bottom: 0;"><strong>Filtered Results:</strong> {len(filtered_doctors)}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Search tips
            st.markdown("""
            <div class="stats-box">
                <h6>Search Tips</h6>
                <ul style="margin-bottom: 0;">
                    <li>Pick hospital to narrow results</li>
                    <li>Use specialties dropdown to filter quickly</li>
                    <li>Click doctor to see availability and book</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            # Map section
            if selected_hospital:
                st.markdown("### Hospital Location")
                df_map = pd.DataFrame([{
                    'lat': selected_hospital['lat'],
                    'lon': selected_hospital['lon'],
                    'name': selected_hospital['name']
                }])
                st.map(df_map)
    
    elif st.session_state.page == 'doctor_profile':
        if st.session_state.selected_doctor is None:
            st.warning("Please select a doctor first.")
            if st.button("Go back to search"):
                st.session_state.page = 'search'
                st.rerun()
        else:
            doctor = get_doctor(st.session_state.selected_doctor)
            hospital = get_hospital(doctor['hospital_id'])
            slots = generate_slots_for_doctor(st.session_state.selected_doctor)
            
            # Back button
            if st.button("← Back to Search"):
                st.session_state.page = 'search'
                st.rerun()
            
            # Doctor info
            st.title(f"{doctor['name']}")
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"""
                <div class="doctor-card">
                    <div style="display: flex; justify-content: space-between; align-items: start;">
                        <div>
                            <h4 style="margin-bottom: 5px;">{doctor['name']}</h4>
                            <div style="color: #6b7280; margin-bottom: 5px;">{doctor['specialty']} • {doctor['phone']}</div>
                            <div style="color: #6b7280;">{hospital['name']} — {hospital['address']}</div>
                        </div>
                        <div style="text-align: right;">
                            <div style="background: #28a745; color: white; padding: 4px 8px; border-radius: 4px; font-size: 0.8rem;">
                                Rating: {doctor['rating']:.1f}
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Available slots
                st.markdown("### Available Slots (Next 7 Days)")
                
                # Group slots by date
                slots_by_date = {}
                for slot in slots:
                    date = slot['date']
                    if date not in slots_by_date:
                        slots_by_date[date] = []
                    slots_by_date[date].append(slot)
                
                for date, day_slots in slots_by_date.items():
                    date_obj = datetime.strptime(date, '%Y-%m-%d')
                    st.markdown(f"**{date_obj.strftime('%A, %B %d, %Y')}**")
                    
                    cols = st.columns(3)
                    for i, slot in enumerate(day_slots):
                        with cols[i % 3]:
                            if slot['booked']:
                                st.markdown(f'<div class="slot-booked">⏰ {slot["time"]} - Booked</div>', unsafe_allow_html=True)
                            else:
                                if st.button(f"📅 {slot['time']}", key=f"slot_{slot['date']}_{slot['time']}", use_container_width=True):
                                    st.session_state.selected_slot = slot
                                    st.session_state.page = 'book'
                                    st.rerun()
                    st.markdown("---")
            
            with col2:
                st.markdown(f"""
                <div class="hospital-info">
                    <h6>Doctor Info</h6>
                    <p><strong>Hospital</strong><br>{hospital['name']}<br>{hospital['address']}</p>
                    <p><strong>Contact</strong><br>{doctor['phone']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Hospital map
                st.markdown("### Hospital Location")
                df_map = pd.DataFrame([{
                    'lat': hospital['lat'],
                    'lon': hospital['lon'],
                    'name': hospital['name']
                }])
                st.map(df_map)
    
    elif st.session_state.page == 'book':
        if st.session_state.selected_doctor is None:
            st.warning("Please select a doctor first.")
            if st.button("Go back to search"):
                st.session_state.page = 'search'
                st.rerun()
        else:
            doctor = get_doctor(st.session_state.selected_doctor)
            slots = generate_slots_for_doctor(st.session_state.selected_doctor)
            available_slots = [s for s in slots if not s['booked']]
            
            # Back button
            if st.button("← Back to Doctor Profile"):
                st.session_state.page = 'doctor_profile'
                st.rerun()
            
            st.title(f"Book Appointment with {doctor['name']}")
            
            with st.form("booking_form"):
                st.subheader("Patient Information")
                
                patient_name = st.text_input("Patient Name*", placeholder="Enter patient name")
                patient_email = st.text_input("Patient Email (optional)", placeholder="Enter email address")
                
                st.subheader("Select Appointment Slot")
                
                if not available_slots:
                    st.error("No available slots for this doctor.")
                else:
                    # Pre-select slot if coming from doctor profile
                    default_index = 0
                    if 'selected_slot' in st.session_state:
                        for i, slot in enumerate(available_slots):
                            if (slot['date'] == st.session_state.selected_slot['date'] and 
                                slot['time'] == st.session_state.selected_slot['time']):
                                default_index = i
                                break
                    
                    slot_options = [f"{slot['display']}" for slot in available_slots]
                    selected_slot_idx = st.selectbox("Available Slots", range(len(slot_options)), 
                                                     format_func=lambda x: slot_options[x], 
                                                     index=default_index)
                    
                    selected_slot = available_slots[selected_slot_idx]
                
                submitted = st.form_submit_button("Confirm Booking", type="primary")
                
                if submitted:
                    if not patient_name.strip():
                        st.error("Patient name is required!")
                    elif not available_slots:
                        st.error("No available slots!")
                    else:
                        # Check if slot is still available
                        is_still_available = not any(
                            b['doctor_id'] == st.session_state.selected_doctor and 
                            b['date'] == selected_slot['date'] and 
                            b['time'] == selected_slot['time'] 
                            for b in st.session_state.bookings
                        )
                        
                        if not is_still_available:
                            st.error("Sorry, this slot has just been booked by someone else. Please select another slot.")
                        else:
                            # Create booking
                            booking_id = next(st.session_state.booking_id_counter)
                            booking = {
                                'id': booking_id,
                                'doctor_id': st.session_state.selected_doctor,
                                'patient_name': patient_name.strip(),
                                'patient_email': patient_email.strip(),
                                'date': selected_slot['date'],
                                'time': selected_slot['time'],
                                'created_at': datetime.now().isoformat()
                            }
                            
                            st.session_state.bookings.append(booking)
                            st.session_state.current_booking = booking_id
                            
                            # Clear selected slot
                            if 'selected_slot' in st.session_state:
                                del st.session_state.selected_slot
                            
                            # Show confirmation
                            st.success("✅ Appointment booked successfully!")
                            
                            hospital = get_hospital(doctor['hospital_id'])
                            
                            st.markdown(f"""
                            <div class="doctor-card" style="text-align: center;">
                                <h4>✅ Appointment Confirmed</h4>
                                <p><strong>Doctor:</strong> {doctor['name']}</p>
                                <p><strong>Hospital:</strong> {hospital['name']}</p>
                                <p><strong>Date:</strong> {selected_slot['date']}</p>
                                <p><strong>Time:</strong> {selected_slot['time']}</p>
                                <p><strong>Patient:</strong> {patient_name}</p>
                                {f'<p><strong>Email:</strong> {patient_email}</p>' if patient_email else ''}
                                <p><strong>Booking ID:</strong> #{booking_id}</p>
                            </div>
                            """, unsafe_allow_html=True)
                            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Book Another Appointment"):
                    st.session_state.page = 'search'
                    st.rerun()
            
            with col2:
                if st.button("View My Bookings"):
                    st.session_state.page = 'bookings'
                    st.rerun()
    
    
    elif st.session_state.page == 'bookings':
        st.title("My Bookings")
        
        if not st.session_state.bookings:
            st.info("You haven't made any bookings yet.")
            if st.button("Search for Doctors"):
                st.session_state.page = 'search'
                st.rerun()
        else:
            st.markdown(f"**Total Bookings:** {len(st.session_state.bookings)}")
            
            for booking in reversed(st.session_state.bookings):  # Show most recent first
                doctor = get_doctor(booking['doctor_id'])
                hospital = get_hospital(doctor['hospital_id']) if doctor else None
                
                # Convert date and time for display
                booking_datetime = datetime.strptime(f"{booking['date']} {booking['time']}", "%Y-%m-%d %H:%M")
                is_past = booking_datetime < datetime.now()
                
                status_color = "#dc3545" if is_past else "#28a745"
                status_text = "Past" if is_past else "Upcoming"
                
                st.markdown(f"""
                <div class="doctor-card">
                    <div style="display: flex; justify-content: space-between; align-items: start;">
                        <div style="flex-grow: 1;">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                                <h5 style="margin: 0;">Booking #{booking['id']}</h5>
                                <span style="background: {status_color}; color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.8rem;">
                                    {status_text}
                                </span>
                            </div>
                            <p style="margin: 5px 0;"><strong>Doctor:</strong> {doctor['name'] if doctor else 'N/A'}</p>
                            <p style="margin: 5px 0;"><strong>Specialty:</strong> {doctor['specialty'] if doctor else 'N/A'}</p>
                            <p style="margin: 5px 0;"><strong>Hospital:</strong> {hospital['name'] if hospital else 'N/A'}</p>
                            <p style="margin: 5px 0;"><strong>Date & Time:</strong> {booking_datetime.strftime('%A, %B %d, %Y at %I:%M %p')}</p>
                            <p style="margin: 5px 0;"><strong>Patient:</strong> {booking['patient_name']}</p>
                            {f"<p style='margin: 5px 0;'><strong>Email:</strong> {booking['patient_email']}</p>" if booking['patient_email'] else ''}
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            if st.button("Book New Appointment"):
                st.session_state.page = 'search'
                st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #6b7280; padding: 20px;'>© 2025 MediSearch — Streamlit Demo</div>",
        unsafe_allow_html=True
    )

if __name__ == '__main__':
    st.set_page_config(
        page_title="Find doctors & book appointments",
        page_icon="🏥",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    show_page()
