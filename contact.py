import streamlit as st

def show_page():
    # --- Language Dictionary for this page ---
    translations = {
        "English": {
            "title": "Contact Us",
            "tagline": "Get in Touch with the E-Hospital Portal Team",
            "introduction": "We value your feedback and are here to assist you. Please use the form below to reach out to us with any queries, suggestions, or issues.",
            "contact_info_title": "Our Contact Details",
            "address_label": "Office Address",
            "address_text": "National Health Authority, New Delhi, India",
            "phone_label": "Helpline Numbers",
            "phone_text": "+91 11 2301 2345 (General Inquiries)",
            "email_label": "Official Email",
            "email_text": "support@ehospital.gov.in",
            "form_header": "Send Us a Message",
            "name_placeholder": "Your Full Name",
            "email_placeholder": "Your Email Address",
            "subject_placeholder": "Subject",
            "message_placeholder": "Your Message",
            "submit_button": "Submit",
            "form_success": "Thank you for your message! We have received your query and will get back to you shortly.",
            "disclaimer_title": "Important Note",
            "disclaimer_text": "For medical emergencies, please do not use this form. Contact your nearest hospital or emergency services immediately."
        },
        "हिन्दी": {
            "title": "हमसे संपर्क करें",
            "tagline": "ई-हॉस्पिटल पोर्टल टीम से संपर्क करें",
            "introduction": "हम आपकी प्रतिक्रिया को महत्व देते हैं और आपकी सहायता के लिए यहाँ हैं। किसी भी प्रश्न, सुझाव या समस्या के लिए कृपया नीचे दिए गए फॉर्म का उपयोग करके हमसे संपर्क करें।",
            "contact_info_title": "हमारे संपर्क विवरण",
            "address_label": "कार्यालय का पता",
            "address_text": "राष्ट्रीय स्वास्थ्य प्राधिकरण, नई दिल्ली, भारत",
            "phone_label": "हेल्पलाइन नंबर",
            "phone_text": "+91 11 2301 2345 (सामान्य पूछताछ)",
            "email_label": "आधिकारिक ईमेल",
            "email_text": "support@ehospital.gov.in",
            "form_header": "हमें एक संदेश भेजें",
            "name_placeholder": "आपका पूरा नाम",
            "email_placeholder": "आपका ईमेल पता",
            "subject_placeholder": "विषय",
            "message_placeholder": "आपका संदेश",
            "submit_button": "प्रस्तुत करें",
            "form_success": "आपके संदेश के लिए धन्यवाद! हमें आपका प्रश्न प्राप्त हो गया है और हम जल्द ही आपसे संपर्क करेंगे।",
            "disclaimer_title": "महत्वपूर्ण नोट",
            "disclaimer_text": "चिकित्सा आपात स्थितियों के लिए, कृपया इस फॉर्म का उपयोग न करें। तुरंत अपने निकटतम अस्पताल या आपातकालीन सेवाओं से संपर्क करें।"
        },
        "தமிழ்": {
            "title": "எங்களைத் தொடர்புகொள்ளவும்",
            "tagline": "மின் மருத்துவமனை குழுவை தொடர்பு கொள்ளவும்",
            "introduction": "உங்கள் கருத்தை நாங்கள் மதிக்கிறோம், மேலும் உங்களுக்கு உதவ நாங்கள் இங்கு இருக்கிறோம். ஏதேனும் கேள்விகள், பரிந்துரைகள் அல்லது சிக்கல்களுக்கு எங்களைத் தொடர்பு கொள்ள கீழே உள்ள படிவத்தைப் பயன்படுத்தவும்.",
            "contact_info_title": "எங்கள் தொடர்பு விவரங்கள்",
            "address_label": "அலுவலக முகவரி",
            "address_text": "தேசிய சுகாதார ஆணையம், புது தில்லி, இந்தியா",
            "phone_label": "ஹெல்ப்லைன் எண்கள்",
            "phone_text": "+91 11 2301 2345 (பொது விசாரணைகள்)",
            "email_label": "அதிகாரப்பூர்வ மின்னஞ்சல்",
            "email_text": "support@ehospital.gov.in",
            "form_header": "எங்களுக்கு ஒரு செய்தியை அனுப்பவும்",
            "name_placeholder": "உங்கள் முழு பெயர்",
            "email_placeholder": "உங்கள் மின்னஞ்சல் முகவரி",
            "subject_placeholder": "பொருள்",
            "message_placeholder": "உங்கள் செய்தி",
            "submit_button": "சமர்ப்பி",
            "form_success": "உங்கள் செய்திக்கு நன்றி! உங்கள் கேள்வியை நாங்கள் பெற்றுள்ளோம், விரைவில் உங்களைத் தொடர்புகொள்வோம்.",
            "disclaimer_title": "முக்கிய குறிப்பு",
            "disclaimer_text": "மருத்துவ அவசரநிலைகளுக்கு, இந்த படிவத்தைப் பயன்படுத்த வேண்டாம். உடனடியாக உங்கள் அருகிலுள்ள மருத்துவமனை அல்லது அவசர சேவைகளைத் தொடர்பு கொள்ளவும்."
        }
    }

    # Get the language from session state and use a default if not found
    try:
        lang_data = translations[st.session_state.language]
    except (KeyError, AttributeError):
        lang_data = translations["English"]

    st.header(lang_data["title"])
    st.markdown(f"<p style='font-size: 1.25rem; color: #ff7b00;'>{lang_data['tagline']}</p>", unsafe_allow_html=True)
    st.markdown("---")
    st.write(lang_data["introduction"])

    # --- Contact Information Section ---
    st.subheader(lang_data["contact_info_title"])
    st.markdown(f"**{lang_data['address_label']}:** {lang_data['address_text']}")
    st.markdown(f"**{lang_data['phone_label']}:** {lang_data['phone_text']}")
    st.markdown(f"**{lang_data['email_label']}:** {lang_data['email_text']}")
    
    st.markdown("---")

    # --- Contact Form ---
    with st.form("contact_form"):
        st.subheader(lang_data["form_header"])
        name = st.text_input(lang_data["name_placeholder"])
        email = st.text_input(lang_data["email_placeholder"])
        subject = st.text_input(lang_data["subject_placeholder"])
        message = st.text_area(lang_data["message_placeholder"])
        
        submitted = st.form_submit_button(lang_data["submit_button"])

    if submitted:
        if name and email and subject and message:
            st.success(lang_data["form_success"])
        else:
            st.error("Please fill in all fields before submitting.")

    st.markdown("---")

    # --- Important Note Disclaimer ---
    st.subheader(lang_data["disclaimer_title"])
    st.warning(lang_data["disclaimer_text"])
