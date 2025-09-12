import streamlit as st
import time

def show_page():
    """
    Creates a comprehensive user interface for a simulated telemedicine video consultation
    that looks and feels exactly like a Google Meet video call, but with a clean, professional
    light theme.
    """
    # Custom CSS for a modern, professional look with responsive design
    st.markdown(
        """
        <style>
            /* Main app styling for a light, professional theme */
            .stApp {
                background-color: #f0f2f6;
                font-family: 'Inter', sans-serif;
                color: #333333;
            }

            /* Container for the main layout */
            .main-container {
                display: flex;
                flex-direction: column;
                gap: 20px;
                padding: 20px;
                height: 100vh;
            }

            /* Doctor profile card styling */
            .doctor-profile-card {
                background-color: #ffffff;
                border-radius: 16px;
                padding: 24px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                display: flex;
                gap: 24px;
                align-items: center;
                flex-wrap: wrap;
            }

            /* Profile image container for circular shape */
            .profile-image-container {
                width: 150px;
                height: 150px;
                border-radius: 50%;
                overflow: hidden;
                flex-shrink: 0;
            }

            .profile-image {
                width: 100%;
                height: 100%;
                object-fit: cover;
            }

            .profile-details {
                flex-grow: 1;
            }

            /* Video call layout with main and chat panels */
            .video-call-layout {
                display: flex;
                flex-direction: row;
                gap: 20px;
                flex-wrap: wrap;
            }
            .video-call-panel {
                flex: 2;
                background-color: #ffffff;
                border-radius: 16px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                padding: 20px;
                color: #333333;
                position: relative;
                min-width: 400px;
            }
            .chat-panel {
                flex: 1;
                background-color: #ffffff;
                border-radius: 16px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                padding: 20px;
                display: flex;
                flex-direction: column;
                min-width: 300px;
            }

            /* Video feed styling */
            .video-placeholder {
                flex: 1;
                border-radius: 12px;
                overflow: hidden;
                background-color: #e0e0e0;
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
                height: 400px;
                position: relative;
            }
            
            /* Your camera feed container (small overlay) */
            .your-camera-feed {
                position: absolute;
                bottom: 24px;
                right: 24px;
                width: 220px;
                height: 140px;
                border-radius: 12px;
                border: 2px solid #fff;
                overflow: hidden;
                background-color: #e0e0e0;
                display: flex;
                justify-content: center;
                align-items: center;
                z-index: 10;
            }
            .camera-off-message {
                color: #666;
                font-size: 1rem;
                text-align: center;
            }
            .video-overlay-text {
                position: absolute; 
                bottom: 12px; 
                left: 12px; 
                background-color: rgba(255,255,255,0.8); 
                padding: 4px 8px; 
                border-radius: 8px; 
                font-weight: 500; 
                color: #333;
            }
            .your-video-overlay-text {
                position: absolute; 
                bottom: 12px; 
                left: 12px; 
                background-color: rgba(0,0,0,0.5); 
                padding: 4px 8px; 
                border-radius: 8px; 
                font-weight: 500; 
                color: #fff;
            }

            /* Call control buttons */
            .control-buttons-container {
                display: flex;
                justify-content: center;
                gap: 20px;
                margin-top: 20px;
                flex-wrap: wrap;
                position: absolute;
                bottom: 16px;
                left: 50%;
                transform: translateX(-50%);
                z-index: 20;
            }
            .control-button {
                background-color: #d1d9e6;
                color: #333333;
                border: none;
                border-radius: 50%;
                width: 56px;
                height: 56px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 24px;
                cursor: pointer;
                transition: background-color 0.3s;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
            .control-button:hover {
                background-color: #c0c8d4;
            }
            .stButton>button {
                background-color: #d1d9e6 !important;
                color: #333333 !important;
                border: none !important;
                border-radius: 50% !important;
                width: 56px !important;
                height: 56px !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
                font-size: 24px !important;
                cursor: pointer !important;
                transition: background-color 0.3s !important;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1) !important;
                padding: 0px !important;
            }
            .stButton>button:hover {
                background-color: #c0c8d4 !important;
            }

            .stButton>button.end {
                background-color: #ea4335 !important;
                color: white !important;
            }
            .stButton>button.end:hover {
                background-color: #d93025 !important;
            }

            .stButton>button.mic-off-bg {
                background-color: #ea4335 !important;
                color: white !important;
            }
            .stButton>button.mic-off-bg:hover {
                background-color: #d93025 !important;
            }

            .stButton>button.cam-off-bg {
                background-color: #ea4335 !important;
                color: white !important;
            }
            .stButton>button.cam-off-bg:hover {
                background-color: #d93025 !important;
            }

            /* Streamlit specific adjustments */
            .st-emotion-cache-1kyx5xt {
                padding: 0;
            }
            .chat-messages {
                flex-grow: 1;
                overflow-y: auto;
                padding-right: 10px;
                border-bottom: 1px solid #ccc;
                padding-bottom: 12px;
                margin-bottom: 12px;
            }
            .chat-message {
                margin-bottom: 8px;
            }
            .chat-sender {
                font-weight: 600;
                color: #1a73e8;
                margin-right: 8px;
            }
            .st-emotion-cache-1kyx5xt {
                padding: 0;
            }
            .st-emotion-cache-1kyx5xt .stButton>button {
                width: 56px;
                height: 56px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 24px;
            }
            .st-emotion-cache-1kyx5xt .stButton>button svg {
                width: 24px;
                height: 24px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Telemedicine Support")
    st.markdown("---")

    # Define detailed doctor data
    doctors = {
        "Dr. N. Varma (General Physician)": {
            "name": "Dr. N. Varma",
            "specialty": "General Physician",
            "bio": "Dr. Varma is a highly-respected general physician dedicated to providing comprehensive care for patients of all ages. He focuses on diagnosing and treating a wide range of conditions.",
            "education": "M.B.B.S, Grant Medical College",
            "experience": "10+ years",
            "image_url": "https://placehold.co/800x600/C4D7F2/333333?text=Dr.+Varma",
            "initial_chat": "Hello, how can I assist you today?"
        },
        "Dr. Priya Sharma (Cardiologist)": {
            "name": "Dr. Priya Sharma",
            "specialty": "Cardiologist",
            "bio": "Dr. Sharma specializes in the diagnosis and treatment of heart and blood vessel disorders. She is dedicated to patient education and preventative care.",
            "education": "M.B.B.S, M.D. (Cardiology), AIIMS Delhi",
            "experience": "15+ years",
            "image_url": "https://placehold.co/800x600/F2C4D7/333333?text=Dr.+Sharma",
            "initial_chat": "Hi, I'm Dr. Sharma. Let's discuss your heart health."
        },
        "Dr. Rahul Gupta (Pediatrician)": {
            "name": "Dr. Rahul Gupta",
            "specialty": "Pediatrician",
            "bio": "Dr. Gupta is a compassionate pediatrician with a passion for helping children and their families. He provides a full range of pediatric services, from routine check-ups to managing acute illnesses.",
            "education": "M.D. (Pediatrics), CMC Vellore",
            "experience": "8 years",
            "image_url": "https://placehold.co/800x600/D7F2C4/333333?text=Dr.+Gupta",
            "initial_chat": "Hello there! What seems to be the trouble today?"
        },
        "Dr. Alok Singh (Orthopedic Surgeon)": {
            "name": "Dr. Alok Singh",
            "specialty": "Orthopedic Surgeon",
            "bio": "Dr. Singh is a skilled orthopedic surgeon specializing in musculoskeletal conditions. He provides expert care for bone, joint, and muscle problems, from diagnosis to rehabilitation.",
            "education": "M.S. (Orthopedics), PGIMER",
            "experience": "12 years",
            "image_url": "https://placehold.co/800x600/A3E4D7/333333?text=Dr.+Singh",
            "initial_chat": "Hello, how can I assist you with your orthopedic concerns?"
        },
        "Dr. Maya Patel (Gastroenterologist)": {
            "name": "Dr. Maya Patel",
            "specialty": "Gastroenterologist",
            "bio": "Dr. Patel is a specialist in digestive system disorders. She is committed to providing compassionate care for patients with conditions affecting the stomach, intestines, and liver.",
            "education": "M.D. (Gastroenterology), AIIMS Delhi",
            "experience": "10 years",
            "image_url": "https://placehold.co/800x600/D1B1D7/333333?text=Dr.+Patel",
            "initial_chat": "Hi, I'm Dr. Patel. Please tell me about your symptoms."
        }
    }

    # Initialize session state for the call status and selected doctor
    if 'call_active' not in st.session_state:
        st.session_state.call_active = False
    if 'selected_doctor_key' not in st.session_state:
        st.session_state.selected_doctor_key = None
    if 'chat_messages' not in st.session_state:
        st.session_state.chat_messages = []
    if 'mic_muted' not in st.session_state:
        st.session_state.mic_muted = False
    if 'camera_off' not in st.session_state:
        st.session_state.camera_off = False
    
    # UI for doctor selection
    if not st.session_state.call_active:
        st.markdown("### Choose a Doctor")
        selected_key = st.selectbox(
            "Select a doctor to begin your consultation.",
            options=list(doctors.keys()),
            index=None,
            key="doctor_selector"
        )
        if selected_key:
            st.session_state.selected_doctor_key = selected_key
            selected_doctor_info = doctors[selected_key]
            
            # Display doctor details card
            st.markdown(f"""
            <div class="doctor-profile-card">
                <div class="profile-image-container">
                    <img src="{selected_doctor_info['image_url']}" class="profile-image" alt="Doctor Photo">
                </div>
                <div class="profile-details">
                    <h3>{selected_doctor_info['name']}</h3>
                    <p><strong>Specialty:</strong> {selected_doctor_info['specialty']}</p>
                    <p><strong>Experience:</strong> {selected_doctor_info['experience']}</p>
                    <p><strong>Education:</strong> {selected_doctor_info['education']}</p>
                    <p>{selected_doctor_info['bio']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("---")
            if st.button("Start Call", use_container_width=True):
                st.session_state.call_active = True
                st.session_state.chat_messages = [
                    {"role": "doctor", "content": selected_doctor_info['initial_chat']}
                ]
                st.session_state.mic_muted = False
                st.session_state.camera_off = False
                st.rerun()
    else:
        # UI for the active video call
        selected_doctor_info = doctors[st.session_state.selected_doctor_key]
        st.success(f"You are now connected with {selected_doctor_info['name']} for your consultation.")

        video_col, chat_col = st.columns([3, 1])

        with video_col:
            st.markdown('<div class="video-call-panel">', unsafe_allow_html=True)
            
            # Doctor's feed (main feed)
            st.markdown(f"""
                <div class="video-placeholder">
                    <img src="{selected_doctor_info['image_url']}" style="width:100%; height:100%; object-fit:cover; border-radius:12px;" />
                    <div class="video-overlay-text">
                        {selected_doctor_info['name']}
                    </div>
                </div>
            """, unsafe_allow_html=True)

            # Your feed (small overlay)
            st.markdown('<div class="your-camera-feed">', unsafe_allow_html=True)
            if not st.session_state.camera_off:
                user_video = st.camera_input(" ", key="user_camera", label_visibility="collapsed")
                if user_video is None:
                    st.markdown('<div class="camera-off-message">Camera is off</div>', unsafe_allow_html=True)
                else:
                    st.image(user_video, use_column_width=True)
            else:
                st.markdown('<div class="camera-off-message">Camera is off</div>', unsafe_allow_html=True)

            st.markdown('<div class="your-video-overlay-text">You</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            # Call controls
            control_col1, control_col2, control_col3 = st.columns([1,1,1])
            with control_col1:
                mic_icon = """<svg id="mic-on" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-mic"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" x2="12" y1="19" y2="22"/></svg>"""
                mic_off_icon = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-mic-off"><line x1="2" x2="22" y1="2" y2="22"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" x2="12" y1="19" y2="22"/><path d="M10 9v3a2 2 0 0 0 4 0V9"/></svg>"""
                mic_button_label = mic_off_icon if st.session_state.mic_muted else mic_icon
                st.form_submit_button(label=mic_button_label, on_click=lambda: st.session_state.update(mic_muted=not st.session_state.mic_muted), use_container_width=True)
                if st.session_state.mic_muted:
                    st.markdown("<style> .st-emotion-cache-1kyx5xt > button {background-color: #ea4335 !important; color: white !important;} </style>", unsafe_allow_html=True)

            with control_col2:
                cam_icon = """<svg id="camera-on" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-video"><path d="m22 8-6 4 6 4V8Z"/><rect width="14" height="12" x="2" y="6" rx="2" ry="2"/></svg>"""
                cam_off_icon = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-video-off"><path d="M16 16v1a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2h2m4 0h1a2 2 0 0 1 2 2v1m-7 8 9-9"/><path d="m22 8-6 4 6 4V8Z"/></svg>"""
                cam_button_label = cam_off_icon if st.session_state.camera_off else cam_icon
                st.form_submit_button(label=cam_button_label, on_click=lambda: st.session_state.update(camera_off=not st.session_state.camera_off), use_container_width=True)
                if st.session_state.camera_off:
                    st.markdown("<style> .st-emotion-cache-1kyx5xt > button {background-color: #ea4335 !important; color: white !important;} </style>", unsafe_allow_html=True)


            with control_col3:
                end_call_icon = """<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-phone-off"><path d="M10.68 13.31a16 16 0 0 0 5.81 5.81l2.07-2.07a2 2 0 0 1 2.75 2.75L17.8 20.73a1.99 1.99 0 0 1-4.22.48l-1.6-1.6A16 16 0 0 0 3.27 6.22l-2.07 2.07a2 2 0 0 1-2.75-2.75L6.2 1.27a1.99 1.99 0 0 1 .48-4.22l1.6 1.6A16 16 0 0 0 17.8 17.8L20.73 20.73a2 2 0 0 1 2.75 2.75L21.27 23.73a1.99 1.99 0 0 1-.48-4.22l-1.6-1.6Z"/></svg>"""
                if st.form_submit_button(label=end_call_icon, key="end_call_button", use_container_width=True):
                    st.session_state.call_active = False
                    st.session_state.mic_muted = False
                    st.session_state.camera_off = False
                    st.session_state.chat_messages = []
                    st.rerun()
                st.markdown("<style> .st-emotion-cache-1kyx5xt > button {background-color: #ea4335 !important; color: white !important;} </style>", unsafe_allow_html=True)


        with chat_col:
            st.markdown('<div class="chat-panel">', unsafe_allow_html=True)
            st.markdown("### Chat with Doctor")
            st.markdown("---")
            
            # Display chat messages
            chat_container = st.container(height=400)
            with chat_container:
                for message in st.session_state.chat_messages:
                    st.markdown(f'<div class="chat-message"><span class="chat-sender">{message["role"]}</span><span class="chat-content">{message["content"]}</span></div>', unsafe_allow_html=True)

            # Chat input
            user_message = st.chat_input("Send a message to everyone", key="chat_input")
            if user_message:
                st.session_state.chat_messages.append({"role": "You", "content": user_message})
                
                # Simple bot-like response from the doctor
                if "headache" in user_message.lower() or "pain" in user_message.lower():
                    doctor_response = "Okay, can you describe the nature of the pain and any other symptoms?"
                elif "prescription" in user_message.lower() or "medicine" in user_message.lower():
                    doctor_response = "I can send an e-prescription to your registered email address. Is that okay?"
                else:
                    doctor_response = "I understand. Can you tell me a little more about that?"
                
                with st.spinner('Doctor is typing...'):
                    time.sleep(2) # Simulate typing delay
                
                st.session_state.chat_messages.append({"role": selected_doctor_info['name'], "content": doctor_response})
                st.rerun()
                
            st.markdown('</div>', unsafe_allow_html=True)

# The following line is for direct execution of this script
if __name__ == '__main__':
    show_page()
