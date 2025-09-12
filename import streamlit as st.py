import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import st_folium
import math
from datetime import datetime, timedelta
import uuid
import plotly.express as px
import plotly.graph_objects as go
from geopy.distance import geodesic
import requests
import time

def show_page():
    # Custom CSS for professional styling
    st.markdown("""
    <style>
        .main-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            border-radius: 10px;
            color: white;
            margin-bottom: 2rem;
            text-align: center;
        }
        
        .metric-card {
            background: white;
            padding: 1rem;
            border-radius: 8px;
            border-left: 4px solid #3498db;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 1rem;
        }
        
        .emergency-button {
            background: linear-gradient(135deg, #e74c3c, #c0392b) !important;
            color: white !important;
            border: none !important;
            padding: 1rem 2rem !important;
            border-radius: 8px !important;
            font-weight: bold !important;
            font-size: 1.2rem !important;
            width: 100% !important;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(231, 76, 60, 0.7); }
            70% { box-shadow: 0 0 0 10px rgba(231, 76, 60, 0); }
            100% { box-shadow: 0 0 0 0 rgba(231, 76, 60, 0); }
        }
        
        .status-available { 
            background: #d4edda; 
            color: #155724; 
            padding: 0.3rem 0.8rem; 
            border-radius: 15px; 
            font-size: 0.8rem; 
            font-weight: bold; 
        }
        
        .status-en_route { 
            background: #fff3cd; 
            color: #856404; 
            padding: 0.3rem 0.8rem; 
            border-radius: 15px; 
            font-size: 0.8rem; 
            font-weight: bold; 
        }
        
        .status-occupied { 
            background: #f8d7da; 
            color: #721c24; 
            padding: 0.3rem 0.8rem; 
            border-radius: 15px; 
            font-size: 0.8rem; 
            font-weight: bold; 
        }
        
        .priority-critical { 
            background: #fadbd8; 
            color: #e74c3c; 
            padding: 0.3rem 0.8rem; 
            border-radius: 15px; 
            font-size: 0.8rem; 
            font-weight: bold; 
        }
        
        .priority-high { 
            background: #fef5e7; 
            color: #f39c12; 
            padding: 0.3rem 0.8rem; 
            border-radius: 15px; 
            font-size: 0.8rem; 
            font-weight: bold; 
        }
        
        .priority-medium { 
            background: #d6eaf8; 
            color: #3498db; 
            padding: 0.3rem 0.8rem; 
            border-radius: 15px; 
            font-size: 0.8rem; 
            font-weight: bold; 
        }
    </style>
    """, unsafe_allow_html=True)

    # Initialize session state
    if 'ambulances' not in st.session_state:
        st.session_state.ambulances = [
            {
                "id": "AMB001",
                "location": {"lat": 11.0168, "lng": 76.9558},  # Coimbatore
                "status": "available",
                "driver": "John Doe",
                "hospital": "Coimbatore Medical College",
                "last_updated": "2025-09-09 14:30:00"
            },
            {
                "id": "AMB002", 
                "location": {"lat": 11.0240, "lng": 76.9420},
                "status": "en_route",
                "driver": "Jane Smith",
                "hospital": "KMCH Hospital",
                "last_updated": "2025-09-09 14:25:00"
            },
            {
                "id": "AMB003",
                "location": {"lat": 11.0065, "lng": 76.9500},
                "status": "occupied",
                "driver": "Mike Johnson",
                "hospital": "PSG Hospital",
                "last_updated": "2025-09-09 14:20:00"
            },
            {
                "id": "AMB004",
                "location": {"lat": 10.9900, "lng": 76.9600},
                "status": "available",
                "driver": "Sarah Wilson",
                "hospital": "Ganga Hospital",
                "last_updated": "2025-09-09 14:35:00"
            },
            {
                "id": "AMB005",
                "location": {"lat": 11.0300, "lng": 76.9700},
                "status": "maintenance",
                "driver": "David Brown",
                "hospital": "KG Hospital",
                "last_updated": "2025-09-09 13:45:00"
            }
        ]

    if 'requests' not in st.session_state:
        st.session_state.requests = []

    if 'selected_location' not in st.session_state:
        st.session_state.selected_location = None

    # Utility functions
    def calculate_distance(lat1, lon1, lat2, lon2):
        """Calculate distance using geodesic"""
        return geodesic((lat1, lon1), (lat2, lon2)).kilometers

    def get_ambulance_color(status):
        """Get color based on ambulance status"""
        colors = {
            'available': 'green',
            'en_route': 'orange',  
            'occupied': 'red',
            'maintenance': 'gray'
        }
        return colors.get(status, 'blue')

    def create_map(ambulances, center_lat=11.0168, center_lng=76.9558, zoom=12):
        """Create folium map with ambulance markers"""
        m = folium.Map(location=[center_lat, center_lng], zoom_start=zoom)
        
        for ambulance in ambulances:
            color = get_ambulance_color(ambulance['status'])
            
            # Create popup content
            popup_content = f"""
            <b>{ambulance['id']}</b><br>
            Status: {ambulance['status']}<br>
            Driver: {ambulance['driver']}<br>
            Hospital: {ambulance['hospital']}<br>
            Last Updated: {ambulance['last_updated']}
            """
            
            folium.Marker(
                location=[ambulance['location']['lat'], ambulance['location']['lng']],
                popup=folium.Popup(popup_content, max_width=300),
                tooltip=f"{ambulance['id']} - {ambulance['status']}",
                icon=folium.Icon(color=color, icon='ambulance', prefix='fa')
            ).add_to(m)
        
        return m

    def assign_nearest_ambulance(request_location):
        """Find and assign nearest available ambulance"""
        available_ambulances = [amb for amb in st.session_state.ambulances if amb['status'] == 'available']
        
        if not available_ambulances:
            return None
        
        min_distance = float('inf')
        nearest_ambulance = None
        
        for ambulance in available_ambulances:
            distance = calculate_distance(
                request_location['lat'], request_location['lng'],
                ambulance['location']['lat'], ambulance['location']['lng']
            )
            
            if distance < min_distance:
                min_distance = distance
                nearest_ambulance = ambulance
        
        if nearest_ambulance:
            # Update ambulance status
            for i, amb in enumerate(st.session_state.ambulances):
                if amb['id'] == nearest_ambulance['id']:
                    st.session_state.ambulances[i]['status'] = 'en_route'
                    break
            
            return {
                'ambulance_id': nearest_ambulance['id'],
                'distance': round(min_distance, 2),
                'eta_minutes': round((min_distance / 40) * 60)  # Assuming 40 km/h average speed
            }
        
        return None

    # Header
    st.markdown("""
    <div class="main-header">
        <h1>Emergency Ambulance Tracker</h1>
        <p>Real-time ambulance location monitoring and emergency request system</p>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar for navigation
    st.sidebar.title("Control Panel")
    page = st.sidebar.selectbox(
        "Select View",
        ["Track Ambulances", "Request Ambulance", "Manage Requests", "Analytics"]
    )

    # Track Ambulances Page
    if page == "Track Ambulances":
        st.header("Ambulance Tracking")
        
        # Filters
        col1, col2, col3 = st.columns(3)
        
        with col1:
            status_filter = st.selectbox(
                "Filter by Status",
                ["All", "available", "en_route", "occupied", "maintenance"]
            )
        
        with col2:
            search_radius = st.slider("Search Radius (km)", 1, 50, 10)
        
        with col3:
            if st.button("Use My Location"):
                st.info("Location services not available in Streamlit. Using default location.")
        
        # Filter ambulances
        filtered_ambulances = st.session_state.ambulances
        if status_filter != "All":
            filtered_ambulances = [amb for amb in filtered_ambulances if amb['status'] == status_filter]
        
        # Statistics
        st.subheader("Quick Stats")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Ambulances", len(st.session_state.ambulances))
        
        with col2:
            available_count = len([amb for amb in st.session_state.ambulances if amb['status'] == 'available'])
            st.metric("Available", available_count, delta=f"{available_count/len(st.session_state.ambulances)*100:.0f}%")
        
        with col3:
            active_count = len([amb for amb in st.session_state.ambulances if amb['status'] in ['en_route', 'occupied']])
            st.metric("Active", active_count)
        
        with col4:
            maintenance_count = len([amb for amb in st.session_state.ambulances if amb['status'] == 'maintenance'])
            st.metric("Maintenance", maintenance_count)
        
        # Map and List
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("Ambulance Locations")
            if filtered_ambulances:
                map_data = create_map(filtered_ambulances)
                st_folium(map_data, width=700, height=500)
            else:
                st.warning("No ambulances match the selected filters.")
        
        with col2:
            st.subheader("Ambulance List")
            for ambulance in filtered_ambulances:
                with st.expander(f"AMB {ambulance['id']} - {ambulance['status'].title()}"):
                    status_class = f"status-{ambulance['status']}"
                    st.markdown(f"**Status:** <span class='{status_class}'>{ambulance['status'].upper()}</span>", unsafe_allow_html=True)
                    st.write(f"**Driver:** {ambulance['driver']}")
                    st.write(f"**Hospital:** {ambulance['hospital']}")
                    st.write(f"**Location:** {ambulance['location']['lat']:.4f}, {ambulance['location']['lng']:.4f}")
                    st.write(f"**Last Updated:** {ambulance['last_updated']}")

    # Request Ambulance Page
    elif page == "Request Ambulance":
        st.header("Emergency Ambulance Request")
        
        st.markdown("""
        <div style="background: #fff3cd; padding: 1rem; border-radius: 8px; margin-bottom: 1rem; border: 1px solid #ffeaa7;">
            <h4 style="color: #856404; margin: 0;">Emergency Alert</h4>
            <p style="color: #856404; margin: 0.5rem 0 0 0;">For life-threatening emergencies, call 108 immediately while filling this form.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Request form
        with st.form("ambulance_request_form"):
            st.subheader("Patient Information")
            col1, col2 = st.columns(2)
            
            with col1:
                patient_name = st.text_input("Patient Name *", placeholder="Enter patient's full name")
                phone = st.text_input("Contact Number *", placeholder="+91 XXXXX XXXXX")
            
            with col2:
                emergency_type = st.selectbox(
                    "Emergency Type *",
                    ["", "Cardiac Emergency", "Road Accident", "Respiratory Emergency", 
                    "Stroke", "Major Trauma", "Unconscious Patient", "Other"]
                )
                priority = st.selectbox(
                    "Priority Level",
                    ["Critical (Life-threatening)", "High (Urgent)", "Medium (Standard)", "Low (Non-urgent)"],
                    index=2
                )
            
            st.subheader("Location Information")
            emergency_location = st.text_area("Emergency Address *", 
                                            placeholder="Enter complete address with landmarks",
                                            height=100)
            
            # Location selection map
            st.write("**Click on the map to select exact location:**")
            location_map = folium.Map(location=[11.0168, 76.9558], zoom_start=13)
            
            # Add current ambulances to the map for reference
            for ambulance in st.session_state.ambulances:
                color = get_ambulance_color(ambulance['status'])
                folium.Marker(
                    location=[ambulance['location']['lat'], ambulance['location']['lng']],
                    tooltip=f"{ambulance['id']} - {ambulance['status']}",
                    icon=folium.Icon(color=color, icon='ambulance', prefix='fa')
                ).add_to(location_map)
            
            map_data = st_folium(location_map, width=700, height=400, returned_objects=["last_object_clicked"])
            
            # Store selected location
            if map_data['last_object_clicked']:
                st.session_state.selected_location = {
                    'lat': map_data['last_object_clicked']['lat'],
                    'lng': map_data['last_object_clicked']['lng']
                }
            
            if st.session_state.selected_location:
                st.success(f"Selected Location: {st.session_state.selected_location['lat']:.4f}, {st.session_state.selected_location['lng']:.4f}")
            
            description = st.text_area("Additional Details", 
                                    placeholder="Describe the emergency situation, patient condition, etc.",
                                    height=100)
            
            # Submit button
            submitted = st.form_submit_button("REQUEST EMERGENCY AMBULANCE", 
                                            help="Submit emergency ambulance request")
            
            if submitted:
                # Validate form
                if not all([patient_name, phone, emergency_location, emergency_type]):
                    st.error("Please fill in all required fields marked with *")
                elif not st.session_state.selected_location:
                    st.error("Please select a location on the map")
                else:
                    # Create request
                    request_id = str(uuid.uuid4())
                    priority_level = priority.split(' ')[0].lower()
                    
                    # Try to assign ambulance
                    assignment = assign_nearest_ambulance(st.session_state.selected_location)
                    
                    new_request = {
                        'id': request_id,
                        'patient_name': patient_name,
                        'phone': phone,
                        'location': emergency_location,
                        'coordinates': st.session_state.selected_location,
                        'emergency_type': emergency_type,
                        'priority': priority_level,
                        'description': description,
                        'status': 'assigned' if assignment else 'pending',
                        'created_at': datetime.now(),
                        'assigned_ambulance': assignment['ambulance_id'] if assignment else None,
                        'estimated_arrival': datetime.now() + timedelta(minutes=assignment['eta_minutes']) if assignment else None,
                        'distance': assignment['distance'] if assignment else None
                    }
                    
                    st.session_state.requests.append(new_request)
                    st.session_state.selected_location = None  # Reset location
                    
                    # Success message
                    if assignment:
                        st.success(f"""
                        **Request Submitted Successfully!**
                        
                        **Request ID:** {request_id[:8]}...
                        
                        **Assigned Ambulance:** {assignment['ambulance_id']}
                        
                        **Distance:** {assignment['distance']} km
                        
                        **Estimated Arrival:** {assignment['eta_minutes']} minutes
                        
                        The ambulance is on its way! Keep your phone accessible for updates.
                        """)
                    else:
                        st.warning(f"""
                        **Request Submitted - Pending Assignment**
                        
                        **Request ID:** {request_id[:8]}...
                        
                        No ambulances are currently available. Your request has been queued and will be assigned as soon as an ambulance becomes available.
                        
                        Please call 108 for immediate assistance if this is a life-threatening emergency.
                        """)

    # Manage Requests Page
    elif page == "Manage Requests":
        st.header("Request Management Dashboard")
        
        if not st.session_state.requests:
            st.info("No ambulance requests have been submitted yet.")
            st.write("Requests will appear here after they are submitted through the 'Request Ambulance' page.")
        else:
            # Filters
            col1, col2, col3 = st.columns(3)
            
            with col1:
                status_filter = st.selectbox(
                    "Filter by Status",
                    ["All", "pending", "assigned", "en_route", "completed", "cancelled"]
                )
            
            with col2:
                priority_filter = st.selectbox(
                    "Filter by Priority", 
                    ["All", "critical", "high", "medium", "low"]
                )
            
            with col3:
                sort_by = st.selectbox(
                    "Sort by",
                    ["Created Time", "Priority", "Status"]
                )
            
            # Filter requests
            filtered_requests = st.session_state.requests
            
            if status_filter != "All":
                filtered_requests = [req for req in filtered_requests if req['status'] == status_filter]
            
            if priority_filter != "All":
                filtered_requests = [req for req in filtered_requests if req['priority'] == priority_filter]
            
            # Sort requests
            if sort_by == "Priority":
                priority_order = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
                filtered_requests.sort(key=lambda x: priority_order.get(x['priority'], 4))
            elif sort_by == "Created Time":
                filtered_requests.sort(key=lambda x: x['created_at'], reverse=True)
            
            # Statistics
            st.subheader("Request Statistics")
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Total Ambulances", len(st.session_state.ambulances))

            with col2:
                available_count = len([amb for amb in st.session_state.ambulances if amb['status'] == 'available'])
                st.metric("Available", available_count, delta=f"{available_count/len(st.session_state.ambulances)*100:.0f}%")
            
            with col3:
                active_count = len([amb for amb in st.session_state.ambulances if amb['status'] in ['en_route', 'occupied']])
                st.metric("Active", active_count)
            
            with col4:
                maintenance_count = len([amb for amb in st.session_state.ambulances if amb['status'] == 'maintenance'])
                st.metric("Maintenance", maintenance_count)
            
            # Request cards
            st.subheader("Request Details")
            
            for i, request in enumerate(filtered_requests):
                with st.expander(f"Request #{request['id'][:8]} - {request['patient_name']} ({request['priority'].title()})"):
                    col1, col2 = st.columns([2, 1])
                    
                    with col1:
                        st.write(f"**Patient:** {request['patient_name']}")
                        st.write(f"**Phone:** {request['phone']}")
                        st.write(f"**Emergency Type:** {request['emergency_type']}")
                        st.write(f"**Location:** {request['location']}")
                        if request['description']:
                            st.write(f"**Description:** {request['description']}")
                        st.write(f"**Created:** {request['created_at'].strftime('%Y-%m-%d %H:%M:%S')}")
                        
                        if request['assigned_ambulance']:
                            st.write(f"**Assigned Ambulance:** {request['assigned_ambulance']}")
                            st.write(f"**Distance:** {request['distance']} km")
                            if request['estimated_arrival']:
                                st.write(f"**ETA:** {request['estimated_arrival'].strftime('%H:%M:%S')}")
                    
                    with col2:
                        priority_class = f"priority-{request['priority']}"
                        st.markdown(f"**Priority:** <span class='{priority_class}'>{request['priority'].upper()}</span>", unsafe_allow_html=True)
                        
                        status_class = f"status-{request['status']}"
                        st.markdown(f"**Status:** <span class='{status_class}'>{request['status'].upper()}</span>", unsafe_allow_html=True)
                        
                        # Action buttons
                        if request['status'] == 'pending':
                            if st.button(f"Assign Ambulance", key=f"assign_{i}"):
                                assignment = assign_nearest_ambulance(request['coordinates'])
                                if assignment:
                                    st.session_state.requests[st.session_state.requests.index(request)].update({
                                        'status': 'assigned',
                                        'assigned_ambulance': assignment['ambulance_id'],
                                        'estimated_arrival': datetime.now() + timedelta(minutes=assignment['eta_minutes']),
                                        'distance': assignment['distance']
                                    })
                                    st.success(f"Assigned {assignment['ambulance_id']}")
                                    st.experimental_rerun()
                                else:
                                    st.error("No ambulances available")
                        
                        elif request['status'] == 'assigned':
                            if st.button(f"Mark En Route", key=f"enroute_{i}"):
                                st.session_state.requests[st.session_state.requests.index(request)]['status'] = 'en_route'
                                st.success("Status updated to En Route")
                                st.experimental_rerun()
                        
                        elif request['status'] == 'en_route':
                            if st.button(f"Mark Completed", key=f"complete_{i}"):
                                # Free up the ambulance
                                for j, amb in enumerate(st.session_state.ambulances):
                                    if amb['id'] == request['assigned_ambulance']:
                                        st.session_state.ambulances[j]['status'] = 'available'
                                        break
                                
                                st.session_state.requests[st.session_state.requests.index(request)]['status'] = 'completed'
                                st.success("Request completed successfully")
                                st.experimental_rerun()
                        
                        if request['status'] not in ['completed', 'cancelled']:
                            if st.button(f"Cancel Request", key=f"cancel_{i}"):
                                # Free up the ambulance if assigned
                                if request['assigned_ambulance']:
                                    for j, amb in enumerate(st.session_state.ambulances):
                                        if amb['id'] == request['assigned_ambulance']:
                                            st.session_state.ambulances[j]['status'] = 'available'
                                            break
                                
                                st.session_state.requests[st.session_state.requests.index(request)]['status'] = 'cancelled'
                                st.warning("Request cancelled")
                                st.experimental_rerun()

    # Analytics Page
    elif page == "Analytics":
        st.header("Analytics Dashboard")
        
        if not st.session_state.requests:
            st.info("Analytics will be available after some requests are submitted.")
        else:
            # Create analytics data
            requests_df = pd.DataFrame([
                {
                    'id': req['id'][:8],
                    'priority': req['priority'],
                    'status': req['status'],
                    'emergency_type': req['emergency_type'],
                    'created_date': req['created_at'].date(),
                    'created_hour': req['created_at'].hour,
                    'response_time': (req['estimated_arrival'] - req['created_at']).total_seconds() / 60 if req['estimated_arrival'] else None
                }
                for req in st.session_state.requests
            ])
            
            # Key metrics
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                avg_response = requests_df['response_time'].mean() if requests_df['response_time'].notna().any() else 0
                st.metric("Avg Response Time", f"{avg_response:.1f} min")
            
            with col2:
                completion_rate = (requests_df['status'] == 'completed').mean() * 100
                st.metric("Completion Rate", f"{completion_rate:.1f}%")
            
            with col3:
                critical_requests = (requests_df['priority'] == 'critical').sum()
                st.metric("Critical Requests", critical_requests)
            
            with col4:
                available_ambulances = len([amb for amb in st.session_state.ambulances if amb['status'] == 'available'])
                st.metric("Available Ambulances", f"{available_ambulances}/{len(st.session_state.ambulances)}")
            
            # Charts
            col1, col2 = st.columns(2)
            
            with col1:
                # Priority distribution
                st.subheader("Requests by Priority")
                priority_counts = requests_df['priority'].value_counts()
                fig_priority = px.pie(
                    values=priority_counts.values,
                    names=priority_counts.index,
                    title="Request Priority Distribution",
                    color_discrete_map={
                        'critical': '#e74c3c',
                        'high': '#f39c12',
                        'medium': '#3498db',
                        'low': '#95a5a6'
                    }
                )
                st.plotly_chart(fig_priority, use_container_width=True)
            
            with col2:
                # Status distribution
                st.subheader("Requests by Status")
                status_counts = requests_df['status'].value_counts()
                fig_status = px.bar(
                    x=status_counts.index,
                    y=status_counts.values,
                    title="Request Status Distribution",
                    labels={'x': 'Status', 'y': 'Count'},
                    color=status_counts.values,
                    color_continuous_scale='Viridis'
                )
                st.plotly_chart(fig_status, use_container_width=True)
            
            # Emergency types
            st.subheader("Emergency Types Analysis")
            emergency_counts = requests_df['emergency_type'].value_counts()
            fig_emergency = px.bar(
                x=emergency_counts.values,
                y=emergency_counts.index,
                orientation='h',
                title="Most Common Emergency Types",
                labels={'x': 'Number of Requests', 'y': 'Emergency Type'},
                color=emergency_counts.values,
                color_continuous_scale='Reds'
            )
            st.plotly_chart(fig_emergency, use_container_width=True)
            
            # Hourly pattern
            if len(requests_df) > 1:
                st.subheader("Request Pattern by Hour")
                hourly_requests = requests_df.groupby('created_hour').size()
                fig_hourly = px.line(
                    x=hourly_requests.index,
                    y=hourly_requests.values,
                    title="Emergency Requests by Hour of Day",
                    labels={'x': 'Hour of Day', 'y': 'Number of Requests'},
                    markers=True
                )
                st.plotly_chart(fig_hourly, use_container_width=True)
            
            # Raw data
            with st.expander("View Raw Data"):
                st.dataframe(requests_df, use_container_width=True)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 1rem;">
        <p>Emergency Ambulance Tracker | Built with Streamlit | For Medical Emergency Assistance</p>
        <p><strong>Emergency Hotline:</strong> 108 (India) | <a href="tel:108">Call Now</a></p>
    </div>
    """, unsafe_allow_html=True)
