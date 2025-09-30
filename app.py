import streamlit as st
import json

# --- Page config ---
# st.set_page_config() MUST be the very first Streamlit command.
st.set_page_config(page_title="E-Hospital", page_icon="🏥", layout="wide")

# --- Custom CSS for professional design ---
st.markdown(
    """
    <style>
    /* Main container and content area styling */
    .stApp {
        background-color: #ffffff;
    }

    /* Sidebar styling */
    .css-1d391kg, .css-1y4p85o {
        background-color: #ffffff !important;
        border-right: 1px solid #e0e0e0;
    }
    .css-1y4p85o {
        padding-top: 0rem !important;
    }

    /* General button styling */
    .stButton > button {
        width: 100%;
        padding: 8px 15px; /* Adjusted padding */
        border: none;
        border-radius: 8px;
        background-color: #004aad; /* Darker blue color for all sidebar buttons */
        color: white; /* White text for all sidebar buttons */
        font-size: 20px; /* Reduced font size */
        font-weight: 600;
        text-align: left;
        transition: background-color 0.2s, color 0.2s, box-shadow 0.2s;
        margin-bottom: 8px; /* Small gap between buttons */
    }
    .stButton > button:hover {
        background-color: #003a80; /* Slightly darker blue on hover */
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Custom style for the active button based on session state */
    .stButton[data-testid="stButton-home"] > button[aria-selected="true"],
    .stButton[data-testid="stButton-dashboard"] > button[aria-selected="true"],
    .stButton[data-testid="stButton-checkup_corner"] > button[aria-selected="true"],
    .stButton[data-testid="stButton-about"] > button[aria-selected="true"],
    .stButton[data-testid="stButton-contact"] > button[aria-selected="true"],
    .stButton[data-testid="stButton-faq"] > button[aria-selected="true"],
    .stButton[data-testid="stButton-health_tips"] > button[aria-selected="true"],
    .stButton[data-testid="stButton-emergency"] > button[aria-selected="true"],
    .stButton[data-testid="stButton-smart_doctor"] > button[aria-selected="true"],
    .stButton[data-testid="stButton-symptoms_guide"] > button[aria-selected="true"],
    .stButton[data-testid="stButton-bp_diagnosis"] > button[aria-selected="true"],
    .stButton[data-testid="stButton-lung_cancer"] > button[aria-selected="true"],
    .stButton[data-testid="stButton-heart_disease"] > button[aria-selected="true"],
    .stButton[data-testid="stButton-diabetes"] > button[aria-selected="true"],
    .stButton[data-testid="stButton-parkinsons_disease"] > button[aria-selected="true"] {
        background-color: #004aad;
        color: white;
        font-weight: 600;
    }

    /* Top navigation button styling (overrides general button style) */
    .stButton[data-testid*="top_"] > button {
        width: auto; /* Allow width to be determined by content */
        padding: 8px 15px; /* Adjusted padding for a smaller button */
        border-radius: 20px; /* Enhanced rounded corners */
        font-size: 13px; /* Reduced font size */
        font-weight: bold;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Added a box shadow */
        margin: 0;
        transition: all 0.2s ease-in-out; /* Smooth transition */
    }

    /* Specific colors for each top button */
    .stButton[data-testid="stButton-top_login"] > button {
        background-color: #004aad !important; /* Blue color */
        color: white !important;
    }
    .stButton[data-testid="stButton-top_register"] > button {
        background-color: #ff7b00 !important; /* Orange color */
        color: white !important;
    }
    .stButton[data-testid="stButton-top_guest"] > button {
        background-color: #00796b !important; /* Green color */
        color: white !important;
    }

    /* Hover effects for top buttons - now more dynamic */
    .stButton[data-testid="stButton-top_login"] > button:hover {
        background-color: #003a80 !important;
        transform: translateY(-2px);
        box-shadow: 6px 12px rgba(0, 0, 0, 0.3);
    }
    .stButton[data-testid="stButton-top_register"] > button:hover {
        background-color: #cc6200 !important;
        transform: translateY(-2px);
        box-shadow: 6px 12px rgba(0, 0, 0, 0.3);
    }
    .stButton[data-testid="stButton-top_guest"] > button:hover {
        background-color: #005f54 !important;
        transform: translateY(-2px);
        box-shadow: 6px 12px rgba(0, 0, 0, 0.3);
    }
    /* Vertical button stacking for better layout, right-aligned */
    .top-right-buttons {
        display: flex;
        flex-direction: column;
        gap: 8px; /* Space between buttons */
        align-items: flex-end; /* Align buttons to the right */
    }

    /* Sub-section titles in the sidebar */
    .sidebar h3, .sidebar h4 {
        color: #004aad;
        font-weight: bold;
    }

    /* Main content styling */
    .main-content {
        padding: 2rem;
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 4px 8px rgba(0,0,0,0.1);
    }
    .main-title {
        color: #004aad;
        font-weight: bold;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    .main-tagline {
        color: #ff7b00;
        font-size: 1.25rem;
    }
    
    /* Flash News Section - Updated */
    .flash-news-container {
        background-color: #fce803; /* Bright yellow background */
        color: #d11a1a; /* Bold red text */
        padding: 15px 0; /* Add vertical padding */
        overflow: hidden;
        white-space: nowrap;
        border-radius: 0; /* Remove rounded corners */
        margin: 0; /* No margin to touch ends */
    }
    .flash-news-marquee {
        display: inline-block;
        padding-left: 100%;
        animation: marquee 60s linear infinite; /* Slower speed */
        font-size: 18px;
        font-weight: bold; /* Make the text bold */
    }
    @keyframes marquee {
        0% { transform: translate(0, 0); }
        100% { transform: translate(-100%, 0); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Import other pages AFTER the set_page_config call ---
import login
import register
import guest
import dashboard
import personal_dashboard
import bp_diagnosis
import diabetes
import heart_disease
import parkinsons
import lung_cancer
import smart_doctor
import symptoms_guide
import checkup_corner
import about
import contact
import health_tips
import faq
import emergency
import blood_donation
import feedback
import appointment_reminders
import ambulance_tracking
import specialist_consultation
import digital_health_records
import ai_health_bot
import hospital_directory
import free_health_camps
import health_schemes_integration
import organ_donation_registry
import e_prescription

def placeholder_page():
    st.title("This is a placeholder page")
    st.write("This page will contain content for the selected facility.")

# --- Initialize session state ---
if "language" not in st.session_state:
    st.session_state.language = "English"
if "user_is_logged_in" not in st.session_state:
    st.session_state.user_is_logged_in = False
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"
if "username" not in st.session_state:
    st.session_state.username = None

# --- Language Dictionary (with detailed Vision & Mission) ---
translations = {
    "English": {
        "title": "MEDiSMART : A Digital BHARAT Initiative",
        "tagline": "Your Health, Our Priority",
        "vision_title": "Vision: To create a unified healthcare system across India.",
        "vision_para": """The vision of the E-Hospital Portal is to establish a unified, transparent, and accessible healthcare 
ecosystem across India. By integrating hospitals, clinics, doctors, and patients under one 
government-supported digital platform, we aim to remove geographical and administrative barriers. 
This vision focuses on ensuring that every citizen, whether in rural or urban areas, has equal access 
to reliable healthcare services at their fingertips.""",
        "mission_title": "Mission: To connect hospitals, doctors, and citizens for better health services.",
        "mission_para": """The mission of the E-Hospital Portal is to leverage emerging technologies like Artificial Intelligence, 
Machine Learning, and IoT to improve healthcare delivery. Our goal is to provide real-time hospital 
information, doctor availability, online consultation facilities, emergency blood donation alerts, and 
digitized health records linked with unique IDs like Aadhaar. We are committed to making healthcare 
affordable, efficient, and citizen-centric while empowering doctors and hospitals with a seamless 
digital infrastructure.""",
        "flash_news": [
            "New AI-powered diagnostic tools launched at Metropolis Lab, Mumbai on 2025-09-07 at 3:25 PM.",
            "Free health checkup camps in rural areas of Rajasthan, starting 2025-09-10.",
            "Emergency blood donation drive initiated in Chennai, Tamil Nadu on 2025-09-07.",
            "Online appointment booking for all specialists now available at Apollo Hospitals, Delhi from 2025-09-08.",
            "Government launches new health insurance scheme for citizens over 60, effective 2025-09-15."
        ],
        "login": "Login",
        "register": "Register",
        "guest": "Guest User",
        "logout": "Logout",
        "welcome": "Welcome",
        "home": "Home",
        "dashboard": "Dashboard",
        "checkup_corner": " Check-Up Corner",
        "about": "About",
        "contact": "Contact",
        "faq": "FAQ",
        "health_tips": "Health Tips",
        "emergency": "Emergency",
        "general_disease_prediction": "General Disease Prediction",
        "smart_doctor": "Smart Doctor",
        "symptoms_guide": "Symptoms Guide",
        "choose_prediction": "Choose a Disease Prediction:",
        "bp_diagnosis": "BP Diagnosis",
        "lung_cancer": "Lung Cancer",
        "heart_disease": "Heart Disease",
        "diabetes": "Diabetes",
        "parkinsons_disease": "Parkinson's Disease",
        "blood_donation": "Blood Donation Network",
        "hospital_directory": "Hospital Directory",
        "ai_health_bot": "AI Health Bot",
        "appointment_reminders": "Appointment Reminders",
        "ambulance_tracking": "Ambulance Tracking",
        "organ_donation_registry": "Organ Donation Registry",
        "specialist_consultation": "Specialist Consultation",
        "digital_health_records": "Digital Health Records",
        "e_prescription": "e-Prescription",
        "free_health_camps": "Free Health Camps",
        "health_schemes_integration": "Health Schemes Integration",
        "citizen_feedback": "Citizen Feedback",
    },
    "हिन्दी": {
        "title": "ई-हॉस्पिटल पोर्टल",
        "tagline": "आपका स्वास्थ्य, हमारी प्राथमिकता",
        "vision_title": "दृष्टि: पूरे भारत में एकीकृत स्वास्थ्य प्रणाली बनाना।",
        "vision_para": """ई-हॉस्पिटल पोर्टल का दृष्टिकोण पूरे भारत में एकीकृत, पारदर्शी और सुलभ स्वास्थ्य 
प्रणाली स्थापित करना है। अस्पतालों, क्लीनिकों, डॉक्टरों और मरीजों को एक 
सरकारी डिजिटल प्लेटफ़ॉर्म पर जोड़कर, हम भौगोलिक और प्रशासनिक बाधाओं को दूर करना चाहते हैं। 
यह दृष्टि सुनिश्चित करती है कि हर नागरिक, चाहे वह ग्रामीण क्षेत्र में हो या शहरी क्षेत्र में, 
उसे स्वास्थ्य सेवाओं तक समान और आसान पहुँच मिले।""",
        "mission_title": "मिशन: बेहतर स्वास्थ्य सेवाओं के लिए अस्पतालों, डॉक्टरों और नागरिकों को जोड़ना।",
        "mission_para": """ई-हॉस्पिटल पोर्टल का मिशन स्वास्थ्य सेवाओं को बेहतर बनाने के लिए आर्टिफिशियल इंटेलिजेंस, 
मशीन लर्निंग और IoT जैसी उभरती तकनीकों का उपयोग करना है। हमारा लक्ष्य है कि 
अस्पताल की वास्तविक समय की जानकारी, डॉक्टर की उपलब्धता, ऑनलाइन परामर्श, 
आपातकालीन रक्त दान अलर्ट और आधार जैसी यूनिक आईडी से जुड़े डिजिटाइज़्ड स्वास्थ्य रिकॉर्ड उपलब्ध कराए जाएँ। 
हम स्वास्थ्य सेवाओं को किफायती, प्रभावी और नागरिक-केंद्रित बनाने के लिए प्रतिबद्ध हैं।""",
        "flash_news": [
            "नए AI-संचालित निदान उपकरण मुंबई के मेट्रोपोलिस लैब में 2025-09-07 को 3:25 PM पर लॉन्च किए गए।",
            "राजस्थान के ग्रामीण क्षेत्रों में 2025-09-10 से नि:शुल्क स्वास्थ्य जांच शिविर शुरू हो रहे हैं।",
            "चेन्नई, तमिलनाडु में 2025-09-07 को आपातकालीन रक्तदान अभियान शुरू किया गया।",
            "दिल्ली के अपोलो हॉस्पिटल्स में 2025-09-08 से सभी विशेषज्ञों के लिए ऑनलाइन अपॉइंटमेंट बुकिंग अब उपलब्ध है।",
            "सरकार ने 60 वर्ष से अधिक आयु के नागरिकों के लिए नई स्वास्थ्य बीमा योजना 2025-09-15 से शुरू की।"
        ],
        "login": "लॉगिन",
        "register": "रजिस्टर",
        "guest": "अतिथि उपयोगकर्ता",
        "logout": "लॉगआउट",
        "welcome": "स्वागत है",
        "home": "होम",
        "dashboard": "डैशबोर्ड",
        "checkup_corner": " चेक-अप कॉर्नर",
        "about": "के बारे में",
        "contact": "संपर्क करें",
        "faq": "सामान्य प्रश्न",
        "health_tips": "स्वास्थ्य सुझाव",
        "emergency": "आपातकालीन",
        "general_disease_prediction": "सामान्य रोग का पूर्वानुमान",
        "smart_doctor": "स्मार्ट डॉक्टर",
        "symptoms_guide": "लक्षण मार्गदर्शिका",
        "choose_prediction": "रोग का पूर्वानुमान चुनें:",
        "bp_diagnosis": "बीपी निदान",
        "lung_cancer": "फेफड़ों का कैंसर",
        "heart_disease": "हृदय रोग",
        "diabetes": "मधुमेह",
        "parkinsons_disease": "पार्किंसंस रोग",
        "blood_donation": "रक्तदान नेटवर्क",
        "hospital_directory": "अस्पताल निर्देशिका",
        "ai_health_bot": "एआई हेल्थ बॉट",
        "appointment_reminders": "अपॉइंटमेंट रिमाइंडर",
        "ambulance_tracking": "एम्बुलेंस ट्रैकिंग",
        "organ_donation_registry": "अंगदान रजिस्ट्री",
        "specialist_consultation": "विशेषज्ञ परामर्श",
        "digital_health_records": "डिजिटल स्वास्थ्य रिकॉर्ड",
        "e_prescription": "ई-प्रिस्क्रिप्शन",
        "free_health_camps": "नि:शुल्क स्वास्थ्य शिविर",
        "health_schemes_integration": "स्वास्थ्य योजना एकीकरण",
        "citizen_feedback": "नागरिक फीडबैक",
    },
    "தமிழ்": {
        "title": "மின் மருத்துவமனை தளம்",
        "tagline": "உங்கள் ஆரோக்கியம், எங்கள் முன்னுரிமை",
        "vision_title": "காட்சி: இந்தியா முழுவதும் ஒருங்கிணைந்த சுகாதார அமைப்பை உருவாக்குதல்.",
        "vision_para": """மின் மருத்துவமனை தளத்தின் பணி சுகாதார சேவைகளை மேம்படுத்துவதற்காக 
செயற்கை நுண்ணறிவு, மெஷின் லேர்னிங் மற்றும் IoT போன்ற புதிய தொழில்நுட்பங்களைப் பயன்படுத்துவதாகும். 
எங்கள் நோக்கம் நேரடி மருத்துவமனை தகவல், மருத்துவர் கிடைக்கும் நிலை, ஆன்லைன் ஆலோசனை, 
அவசர இரத்த தான எச்சரிக்கைகள் மற்றும் ஆதார் போன்ற தனித்துவ அடையாள எண்களுடன் இணைக்கப்பட்ட 
டிஜிட்டல் சுகாதார பதிவுகளை வழங்குவதாகும். 
சுகாதாரத்தை மலிவானதாகவும், திறமையானதாகவும், குடிமக்கள் மையமாகவும் ஆக்குவதே எங்கள் உறுதிமொழியாகும்.""",
        "mission_title": "பணி: சிறந்த சுகாதார சேவைகளுக்காக மருத்துவமனைகள், மருத்துவர்கள் மற்றும் குடிமக்களை இணைத்தல்.",
        "mission_para": """மின் மருத்துவமனை தளத்தின் பணி சுகாதார சேவைகளை மேம்படுத்துவதற்காக 
செயற்கை நுண்ணறிவு, மெஷின் லேர்னிங் மற்றும் IoT போன்ற புதிய தொழில்நுட்பங்களைப் பயன்படுத்துவதாகும். 
எங்கள் நோக்கம் நேரடி மருத்துவமனை தகவல், மருத்துவர் கிடைக்கும் நிலை, ஆன்லைன் ஆலோசனை, 
அவசர இரத்த தான எச்சரிக்கைகள் மற்றும் ஆதார் போன்ற தனித்துவ அடையாள எண்களுடன் இணைக்கப்பட்ட 
டிஜிட்டல் சுகாதார பதிவுகளை வழங்குவதாகும். 
சுகாதாரத்தை மலிவானதாகவும், திறமையானதாகவும், குடிமக்கள் மையமாகவும் ஆக்குவதே எங்கள் உறுதிமொழியாகும்.""",
        "flash_news": [
            "மும்பையின் மெட்ரோபோலிஸ் லேப்பில் 2025-09-07, 3:25 PM மணிக்கு புதிய செயற்கை நுண்ணறிவு நோயறிதல் கருவிகள் தொடங்கப்பட்டன.",
            "ராஜஸ்தானின் கிராமப்புறங்களில் 2025-09-10 முதல் இலவச சுகாதார முகாம்கள் தொடங்குகின்றன.",
            "சென்னை, தமிழ்நாட்டில் 2025-09-07 அன்று அவசர இரத்த தான இயக்கம் தொடங்கப்பட்டது.",
            "டெல்லியின் அப்போலோ மருத்துவமனைகளில் 2025-09-08 முதல் அனைத்து நிபுணர்களுக்கும் ஆன்லைன் அப்பாயின்ட்மென்ட் முன்பதிவு இப்போது கிடைக்கும்.",
            "அரசு 60 வயதுக்கு மேற்பட்ட குடிமக்களுக்கான புதிய சுகாதார காப்பீட்டு திட்டத்தை 2025-09-15 முதல் அறிமுகப்படுத்தியது।"
        ],
        "login": "உள்நுழை",
        "register": "பதிவு செய்க",
        "guest": "விருந்தினர்",
        "logout": "வெளியேறு",
        "welcome": "வரவேற்பு",
        "home": "முகப்பு",
        "dashboard": "டாஷ்போர்டு",
        "checkup_corner": " சோதனை மூலை",
        "about": "பற்றி",
        "contact": "தொடர்பு",
        "faq": "அடிக்கடி கேட்கப்படும் கேள்விகள்",
        "health_tips": "சுகாதார குறிப்புகள்",
        "emergency": "அவசரம்",
        "general_disease_prediction": "பொதுவான நோய் கணிப்பு",
        "smart_doctor": "ஸ்மார்ட் மருத்துவர்",
        "symptoms_guide": "அறிகுறிகள் வழிகாட்டி",
        "choose_prediction": "நோய் கணிப்பைக் தேர்ந்தெடுக்கவும்:",
        "bp_diagnosis": "பிபி கண்டறிதல்",
        "lung_cancer": "நுரையீரல் புற்றுநோய்",
        "heart_disease": "இதய நோய்",
        "diabetes": "நீரிழிவு நோய்",
        "parkinsons_disease": "பார்கின்சன் நோய்",
        "blood_donation": "இரத்த தான நெட்வொர்க்",
        "hospital_directory": "மருத்துவமனை அடைவு",
        "ai_health_bot": "ஏஐ ஹெல்த் பாட்டி",
        "appointment_reminders": "நேரம் நினைவூட்டல்கள்",
        "ambulance_tracking": "ஆம்புலன்ஸ் கண்காணிப்பு",
        "organ_donation_registry": "உடல் தான பதிவு",
        "specialist_consultation": "சிறப்பு நிபுணர் ஆலோசனை",
        "digital_health_records": "டிஜிட்டல் சுகாதார பதிவுகள்",
        "e_prescription": "மின்பரிந்துரை",
        "free_health_camps": "இலவச சுகாதார முகாம்கள்",
        "health_schemes_integration": "சுகாதார திட்ட ஒருங்கிணைப்பு",
        "citizen_feedback": "பொது கருத்து",
    },
}

# --- Load Translations ---
lang_data = translations.get(st.session_state.language, translations["English"])

# --- Top Navigation ---
def show_navbar():
    col1, col2, col3 = st.columns([1, 2, 1.5]) 
    
    with col1:
        st.image("logo.jpg", width=160) # Adjusted logo size
    
    with col2:
        st.markdown(f"<h2 class='main-title'>{lang_data['title']}</h2>", unsafe_allow_html=True)
    
    with col3:
        if st.session_state.user_is_logged_in:
            st.markdown(f"<span style='font-size: 16px; font-weight: bold; margin-right: 15px;'>{lang_data['welcome']}, {st.session_state.username}</span>", unsafe_allow_html=True)
            if st.button(lang_data['logout'], key="logout_btn", help="Click to logout"):
                st.session_state.user_is_logged_in = False
                st.session_state.current_page = "home"
                st.session_state.username = None
                st.rerun()
        else:
            with st.container():
                st.markdown('<div class="top-right-buttons">', unsafe_allow_html=True)
                if st.button(lang_data['login'], key="top_login"):
                    st.session_state.current_page = "login"
                    st.rerun()
                if st.button(lang_data['register'], key="top_register"):
                    st.session_state.current_page = "register"
                    st.rerun()
                if st.button(lang_data['guest'], key="top_guest"):
                    st.session_state.current_page = "guest"
                    st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)


# --- Sidebar Navigation ---
def create_sidebar_button(label, page_key):
    if st.button(label, key=page_key, use_container_width=True):
        st.session_state.current_page = page_key
        st.rerun()
    if st.session_state.current_page == page_key:
        st.markdown(f"""
            <style>
                .stButton[data-testid="stButton-{page_key}"] > button {{
                    background-color: #004aad;
                    color: white;
                    font-weight: 600;
                }}
                .stButton[data-testid="stButton-{page_key}"] > button:hover {{
                    background-color: #003a80;
                }}
            </style>
        """, unsafe_allow_html=True)


with st.sidebar:
    st.markdown("### Navigation")
    
    # Language Selection (Added this section)
    st.selectbox(
        "Select Language",
        list(translations.keys()),
        key="language_selector",
        on_change=lambda: st.session_state.update(language=st.session_state.language_selector)
    )
    
    # Main Navigation
    create_sidebar_button(lang_data["home"], "home")
    create_sidebar_button(lang_data["dashboard"], "dashboard")
    create_sidebar_button(lang_data["checkup_corner"], "checkup_corner")
    create_sidebar_button(lang_data["about"], "about")
    create_sidebar_button(lang_data["contact"], "contact")
    create_sidebar_button(lang_data["faq"], "faq")
    create_sidebar_button(lang_data["health_tips"], "health_tips")
    create_sidebar_button(lang_data["emergency"], "emergency")

    # Sub-sections for Check-Up Corner, only visible when selected
    if st.session_state.current_page in ["checkup_corner", "smart_doctor", "symptoms_guide", "bp_diagnosis", "lung_cancer", "heart_disease", "diabetes", "parkinsons_disease"]:
        st.markdown("---")
        st.markdown(f"**{lang_data['general_disease_prediction']}**")
        create_sidebar_button(lang_data["smart_doctor"], "smart_doctor")
        create_sidebar_button(lang_data["symptoms_guide"], "symptoms_guide")
        
        st.markdown("---")
        st.markdown(f"**{lang_data['choose_prediction']}**")
        create_sidebar_button(lang_data["bp_diagnosis"], "bp_diagnosis")
        create_sidebar_button(lang_data["lung_cancer"], "lung_cancer")
        create_sidebar_button(lang_data["heart_disease"], "heart_disease")
        create_sidebar_button(lang_data["diabetes"], "diabetes")
        create_sidebar_button(lang_data["parkinsons_disease"], "parkinsons_disease")

# --- Define Home Page Content ---
def show_home_page():
    # --- Tagline ---
    st.markdown(f"<h3 style='text-align:center;color:#ff7b00;'>{lang_data['tagline']}</h3>", unsafe_allow_html=True)
    
    # Gap between tagline and news
    st.markdown("<div style='margin-top: 3rem;'></div>", unsafe_allow_html=True)

    # --- Flash News Section ---
    news_items = " | ".join(lang_data['flash_news'])
    st.markdown(
        f"""
        <div class="flash-news-container">
            <div class="flash-news-marquee">
                {news_items}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Gap between news and vision
    st.markdown("<div style='margin-top: 3rem;'></div>", unsafe_allow_html=True)

    # --- Vision & Mission ---
    st.subheader(lang_data["vision_title"])
    st.write(lang_data["vision_para"])
    st.subheader(lang_data["mission_title"])
    st.write(lang_data["mission_para"])
    st.markdown("---")

    # --- Features Section (NEW BUTTONS IMPLEMENTATION) ---
    st.markdown("## Facilities of the E-Hospital Portal")

    # This dictionary maps facility names to their corresponding page keys
    # You need to create new pages (e.g., blood_donation.py) to match these keys.
    features_data = {
        "English": [
            ("Blood Donation Network", "Connects blood donors with hospitals and patients in real time.", "blood_donation"),
            ("Specialist Consultation", "Search and book appointments with certified specialists across India.", "specialist_consultation"),
            ("Hospital Directory", "Unified database of hospitals with departments, facilities, and services.", "hospital_directory"),
            ("Digital Health Records", "Secure access to patient history linked with Aadhaar or other IDs.", "digital_health_records"),
            ("e-Prescription", "Upload and verify prescriptions digitally with OCR-based automation.", "e_prescription"),
            ("AI Health Bot", "24x7 chatbot for health queries, symptoms guidance, and first aid.", "ai_health_bot"),
            ("Free Health Camps", "Updates on government and NGO-led free health checkup camps.", "free_health_camps"),
            ("Appointment Reminders", "SMS and app-based reminders for scheduled consultations and tests.", "appointment_reminders"),
            ("Health Schemes Integration", "Access healthcare schemes and insurance details.", "health_schemes_integration"),
            ("Ambulance Tracking", "Real-time ambulance availability and GPS tracking.", "ambulance_tracking"),
            ("Organ Donation Registry", "Register and connect with organ donation programs.", "organ_donation_registry"),
            ("Citizen Feedback", "Share hospital and doctor feedback for service improvements.", "citizen_feedback"),
        ],
        "हिन्दी": [
            ("रक्तदान नेटवर्क", "रक्त दाताओं को अस्पतालों और रोगियों से वास्तविक समय में जोड़ता है।", "blood_donation"),
            ("विशेषज्ञ परामर्श", "पूरे भारत में प्रमाणित विशेषज्ञों के साथ अपॉइंटमेंट खोजें और बुक करें।", "specialist_consultation"),
            ("अस्पताल निर्देशिका", "विभागों, सुविधाओं और सेवाओं के साथ अस्पतालों का एकीकृत डेटाबेस।", "hospital_directory"),
            ("डिजिटल स्वास्थ्य रिकॉर्ड", "आधार या अन्य आईडी से जुड़े रोगी इतिहास तक सुरक्षित पहुंच।", "digital_health_records"),
            ("ई-प्रिस्क्रिप्शन", "ओसीआर-आधारित ऑटोमेशन के साथ प्रिस्क्रिप्शन अपलोड और सत्यापित करें।", "e_prescription"),
            ("एआई हेल्थ बॉट", "स्वास्थ्य प्रश्नों और प्राथमिक चिकित्सा के लिए 24x7 चैटबॉट।", "ai_health_bot"),
            ("नि:शुल्क स्वास्थ्य शिविर", "सरकारी और एनजीओ-आधारित नि:शुल्क स्वास्थ्य शिविरों की जानकारी।", "free_health_camps"),
            ("अपॉइंटमेंट रिमाइंडर", "परामर्श और परीक्षणों के लिए एसएमएस और ऐप रिमाइंडर।", "appointment_reminders"),
            ("स्वास्थ्य योजना एकीकरण", "सरकारी स्वास्थ्य योजनाओं और बीमा जानकारी तक पहुंच।", "health_schemes_integration"),
            ("एम्बुलेंस ट्रैकिंग", "एम्बुलेंस की उपलब्धता और जीपीएस ट्रैकिंग।", "ambulance_tracking"),
            ("अंगदान रजिस्ट्री", "अंगदान कार्यक्रमों में पंजीकरण और कनेक्ट करें।", "organ_donation_registry"),
            ("नागरिक फीडबैक", "अस्पताल और डॉक्टर सेवाओं पर फीडबैक साझा करें।", "citizen_feedback"),
        ],
        "தமிழ்": [
            ("இரத்த தான நெட்வொர்க்", "இரத்த தானதாரர்களை மருத்துவமனைகளும் நோயாளிகளும் நேரடியாக இணைக்கிறது.", "blood_donation"),
            ("சிறப்பு நிபுணர் ஆலோசனை", "இந்திய முழுவதும் நிபுணர்களுடன் நேரம் ஒதுக்கீடு செய்யுங்கள்.", "specialist_consultation"),
            ("மருத்துவமனை அடைவு", "மருத்துவமனைகள், துறைகள், சேவைகள் அனைத்தும் ஒரே இடத்தில்.", "hospital_directory"),
            ("டிஜிட்டல் சுகாதார பதிவுகள்", "ஆதார் அல்லது பிற அடையாளங்களுடன் நோயாளி வரலாற்றை அணுகவும்.", "digital_health_records"),
            ("மின்பரிந்துரை", "OCR அடிப்படையிலான தானியக்கத்துடன் பரிந்துரைகளை பதிவேற்றவும்.", "e_prescription"),
            ("ஏஐ ஹெல்த் பாட்டி", "சுகாதார கேள்விகளுக்கும் முதலுதலுக்கும் 24x7 உரையாடல்.", "ai_health_bot"),
            ("இலவச சுகாதார முகாம்கள்", "அரசு மற்றும் என்.ஜி.ஓ நடத்தும் முகாம்களின் தகவல்கள்.", "free_health_camps"),
            ("நேரம் நினைவூட்டல்கள்", "எஸ்எம்எஸ் மற்றும் ஆப் நினைவூட்டல்கள்.", "appointment_reminders"),
            ("சுகாதார திட்ட ஒருங்கிணைப்பு", "சுகாதார திட்டங்கள் மற்றும் காப்பீட்டு விவரங்கள்.", "health_schemes_integration"),
            ("ஆம்புலன்ஸ் கண்காணிப்பு", "உடனடி ஆம்புலன்ஸ் கிடைக்கும் நிலை மற்றும் GPS.", "ambulance_tracking"),
            ("உடல் தான பதிவு", "உடல் தான திட்டங்களில் பதிவு செய்யுங்கள்.", "organ_donation_registry"),
            ("பொது கருத்து", "மருத்துவமனை மற்றும் மருத்துவர் சேவைகள் பற்றிய கருத்துகளை பகிரவும்.", "citizen_feedback"),
        ]
    }

    features = features_data.get(st.session_state.language, features_data["English"])
    cols = st.columns(2)
    for i, (title, desc, page_key) in enumerate(features):
        with cols[i % 2]:
            st.markdown(
                f"""
                <div style="
                    border: 2px solid #004aad;
                    border-radius: 12px;
                    padding: 20px;
                    margin: 10px 0;
                    background-color: #f9f9f9;
                    box-shadow: 2px 2px 6px rgba(0,0,0,0.1);
                ">
                    <h3 style="color:#004aad; font-size:20px; font-family:Arial, Helvetica, sans-serif;">{title}</h3>
                    <p style="font-size:16px; font-family:Arial, Helvetica, sans-serif; color:#333;">{desc}</p>
                """,
                unsafe_allow_html=True
            )
            # Add the button inside the div
            if st.button("Go to " + title, key="feature_btn_" + page_key):
                st.session_state.current_page = page_key
                st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)


# --- Main App Logic ---
show_navbar()

# --- Page Routing (updated to include new pages) ---
if st.session_state.current_page == "home":
    show_home_page()
elif st.session_state.current_page == "login":
    login.show_page()
elif st.session_state.current_page == "personal_dashboard":
    personal_dashboard.show_page()
elif st.session_state.current_page == "register":
    register.show_page()
elif st.session_state.current_page == "guest": 
    guest.show_page()
elif st.session_state.current_page == "dashboard":
    dashboard.show_page()
elif st.session_state.current_page == "checkup_corner":
    checkup_corner.show_page()
elif st.session_state.current_page == "about":
    about.show_page()
elif st.session_state.current_page == "contact":
    contact.show_page()
elif st.session_state.current_page == "faq":
    faq.show_page()
elif st.session_state.current_page == "health_tips":
    health_tips.show_page()
elif st.session_state.current_page == "emergency":
    emergency.show_page()
elif st.session_state.current_page == "smart_doctor":
    smart_doctor.show_page()
elif st.session_state.current_page == "symptoms_guide":
    symptoms_guide.show_page()
elif st.session_state.current_page == "bp_diagnosis":
    bp_diagnosis.show_page()
elif st.session_state.current_page == "lung_cancer":
    lung_cancer.show_page()
elif st.session_state.current_page == "heart_disease":
    heart_disease.show_page()
elif st.session_state.current_page == "diabetes":
    diabetes.show_page()
elif st.session_state.current_page == "parkinsons_disease": 
    parkinsons.show_page()
# Add new elif blocks for each new page you create
elif st.session_state.current_page == "blood_donation":
    blood_donation.show_page()
elif st.session_state.current_page == "hospital_directory":
    hospital_directory.show_page()

elif st.session_state.current_page == "ai_health_bot":
    ai_health_bot.show_page()
elif st.session_state.current_page == "appointment_reminders":
    appointment_reminders.show_page()
elif st.session_state.current_page == "ambulance_tracking":
    ambulance_tracking.show_page()
elif st.session_state.current_page == "organ_donation_registry":
    organ_donation_registry.show_page()
elif st.session_state.current_page == "specialist_consultation":
    specialist_consultation.show_page()
elif st.session_state.current_page == "digital_health_records":
    digital_health_records.show_page()
elif st.session_state.current_page == "e_prescription":
    e_prescription.show_page()
elif st.session_state.current_page == "free_health_camps":
    free_health_camps.show_page()
elif st.session_state.current_page == "health_schemes_integration":
    health_schemes_integration.show_page()

elif st.session_state.current_page == "citizen_feedback":

    feedback.show_page()


