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

def show_page():
    st.header("Ambulance Tracking")
    
    # Initialize session state for ambulances
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
