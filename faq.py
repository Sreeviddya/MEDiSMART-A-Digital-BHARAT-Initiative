import streamlit as st

def show_page():
    # Load translations from the main application
    try:
        from main_app import translations
        lang_data = translations.get(st.session_state.language, translations["English"])
    except ImportError:
        # Fallback in case of direct access or for local testing
        lang_data = {
            "title": "FAQ - Frequently Asked Questions",
            "section_general": "General Questions",
            "section_registration": "Registration & Account Management",
            "section_services": "Services & Features",
            "section_security": "Security & Privacy",
            "section_technical": "Technical Support",
            "faq_list": [
                {
                    "question": "What is the E-Hospital Portal?",
                    "answer": "The E-Hospital Portal is a government-supported digital platform designed to provide a unified healthcare ecosystem. It connects hospitals, doctors, and citizens for seamless access to health services, including appointments, digital health records, and emergency alerts."
                },
                {
                    "question": "Is the E-Hospital Portal free to use?",
                    "answer": "Yes, basic services on the E-Hospital Portal are completely free for all citizens. Some advanced features, like premium teleconsultations with certain specialists, may have associated fees, which will be clearly indicated."
                },
                {
                    "question": "Who can use this portal?",
                    "answer": "The portal is accessible to all Indian citizens. Both registered users and guest users can access various features, though a user account is required for personalized services like digital health records and appointment booking."
                },
                {
                    "question": "What is the 'Smart Doctor' feature?",
                    "answer": "The 'Smart Doctor' is an AI-powered diagnostic tool. You can input your symptoms, and the system will provide an initial assessment and suggest potential medical conditions. It is important to note that this is for informational purposes only and not a substitute for professional medical advice."
                },
                {
                    "question": "How do I book an appointment with a doctor?",
                    "answer": "Once you are logged in, navigate to the 'Check-Up Corner' and select 'Book an Appointment'. You can search for doctors by specialty, location, or hospital and book an available slot that suits your schedule."
                },
                {
                    "question": "What information is required to register?",
                    "answer": "To register, you will need to provide your full name, a valid mobile number, and set a password. An OTP (One-Time Password) will be sent to your number for verification."
                },
                {
                    "question": "Can I register using my Aadhaar card?",
                    "answer": "Yes, you can register using your Aadhaar number. This provides a more secure way to link your digital health records and other government-issued health IDs to your account."
                },
                {
                    "question": "I forgot my password. How can I reset it?",
                    "answer": "On the login page, click on the 'Forgot Password' link. You will be prompted to enter your registered mobile number. An OTP will be sent to your number to verify your identity and allow you to set a new password."
                },
                {
                    "question": "How can I update my personal information?",
                    "answer": "After logging in, go to your 'Personal Dashboard'. There, you will find an 'Edit Profile' section where you can update your contact details, address, and other personal information."
                },
                {
                    "question": "Are my personal health records secure?",
                    "answer": "Yes. We use advanced encryption and robust security protocols to ensure that all your personal and medical data is kept confidential and secure. Your records are linked to a unique ID (like Aadhaar) and are only accessible by you and authorized healthcare providers with your consent."
                },
                {
                    "question": "How is my data used?",
                    "answer": "Your data is used solely for the purpose of providing and improving healthcare services. It is never sold or shared with third-party advertisers. Aggregated and anonymized data may be used for public health research and statistical analysis to benefit the community."
                },
                {
                    "question": "What is the 'Blood Donation Network'?",
                    "answer": "The 'Blood Donation Network' is a feature that connects voluntary blood donors with hospitals and patients in real-time. You can register as a donor, and in case of an emergency, you might receive a notification if your blood type is urgently needed in a nearby hospital."
                },
                {
                    "question": "Can I view my lab reports online?",
                    "answer": "Yes. If the hospital or laboratory you visited is integrated with our portal, your lab reports will be automatically uploaded to your 'Digital Health Records' section for secure viewing and downloading."
                },
                {
                    "question": "What is the 'Symptoms Guide'?",
                    "answer": "The 'Symptoms Guide' is an educational tool that provides information on various diseases and their common symptoms. It helps you understand what to look for and when to seek professional medical help."
                },
                {
                    "question": "How do 'e-Prescriptions' work?",
                    "answer": "Doctors can issue digital prescriptions directly through the portal. This e-prescription is stored in your health records and can be shown to any integrated pharmacy for a seamless and paperless experience."
                },
                {
                    "question": "What should I do in a medical emergency?",
                    "answer": "In a medical emergency, you can use the 'Emergency' button on the sidebar. This feature provides a list of nearby hospitals, emergency contact numbers, and can send a distress alert with your location to emergency services."
                },
                {
                    "question": "What is the 'Health Tips' section?",
                    "answer": "The 'Health Tips' section provides daily and weekly articles, videos, and infographics on a variety of health and wellness topics, from nutrition and exercise to mental health and disease prevention."
                },
                {
                    "question": "Can I give feedback about a hospital or doctor?",
                    "answer": "Yes. Your feedback is crucial for improving services. You can leave ratings and reviews for hospitals and doctors you have consulted with through the portal."
                },
                {
                    "question": "What if I can't find a hospital on the portal?",
                    "answer": "Our team is continuously working to onboard more hospitals and healthcare providers. If a hospital is not listed, you can still use other features of the portal. We encourage you to notify us via the 'Contact' page to request an addition."
                },
                {
                    "question": "Which web browsers are supported?",
                    "answer": "The E-Hospital Portal is optimized for all modern web browsers, including Google Chrome, Mozilla Firefox, Microsoft Edge, and Safari."
                },
                {
                    "question": "I am facing a technical issue. What should I do?",
                    "answer": "If you encounter a technical problem, please try clearing your browser's cache and cookies. If the issue persists, please report it to our technical support team using the form on the 'Contact' page. Provide as much detail as possible, including your device and browser information."
                }
            ],
            # --- Hindi Translations (Please translate these for your final version) ---
            "faq_list_hi": [
                {"question": "ई-हॉस्पिटल पोर्टल क्या है?", "answer": "कृपया इस उत्तर का अनुवाद करें।"},
                {"question": "क्या यह पोर्टल मुफ़्त है?", "answer": "कृपया इस उत्तर का अनुवाद करें।"},
                {"question": "कौन उपयोग कर सकता है?", "answer": "कृपया इस उत्तर का अनुवाद करें।"},
                {"question": "'स्मार्ट डॉक्टर' क्या है?", "answer": "कृपया इस उत्तर का अनुवाद करें।"},
                {"question": "डॉक्टर के साथ अपॉइंटमेंट कैसे बुक करें?", "answer": "कृपया इस उत्तर का अनुवाद करें।"},
                {"question": "पंजीकरण के लिए क्या जानकारी चाहिए?", "answer": "कृपया इस उत्तर का अनुवाद करें।"},
                {"question": "आधार कार्ड से पंजीकरण कर सकते हैं?", "answer": "कृपया इस उत्तर का अनुवाद करें।"},
                {"question": "पासवर्ड भूल गया हूँ।", "answer": "कृपया इस उत्तर का अनुवाद करें।"},
                {"question": "व्यक्तिगत जानकारी कैसे अपडेट करें?", "answer": "कृपया इस उत्तर का अनुवाद करें।"},
                {"question": "स्वास्थ्य रिकॉर्ड सुरक्षित हैं?", "answer": "कृपया इस उत्तर का अनुवाद करें।"},
                {"question": "मेरा डेटा कैसे उपयोग होता है?", "answer": "कृपया इस उत्तर का अनुवाद करें।"},
                {"question": "'रक्तदान नेटवर्क' क्या है?", "answer": "कृपया इस उत्तर का अनुवाद करें।"},
                {"question": "ऑनलाइन लैब रिपोर्ट देख सकता हूँ?", "answer": "कृपया इस उत्तर का अनुवाद करें।"},
                {"question": "'लक्षण मार्गदर्शिका' क्या है?", "answer": "कृपया इस उत्तर का अनुवाद करें।"},
                {"question": "ई-प्रिस्क्रिप्शन कैसे काम करता है?", "answer": "कृपया इस उत्तर का अनुवाद करें।"},
                {"question": "आपातकालीन स्थिति में क्या करें?", "answer": "कृपया इस उत्तर का अनुवाद करें।"},
                {"question": "'स्वास्थ्य सुझाव' क्या है?", "answer": "कृपया इस उत्तर का अनुवाद करें।"},
                {"question": "फीडबैक दे सकता हूँ?", "answer": "कृपया इस उत्तर का अनुवाद करें।"},
                {"question": "अस्पताल नहीं मिल रहा है?", "answer": "कृपया इस उत्तर का अनुवाद करें।"},
                {"question": "कौन से ब्राउज़र समर्थित हैं?", "answer": "कृपया इस उत्तर का अनुवाद करें।"},
                {"question": "तकनीकी समस्या है।", "answer": "कृपया इस उत्तर का अनुवाद करें।"}
            ],
            # --- Tamil Translations (Please translate these for your final version) ---
            "faq_list_ta": [
                {"question": "ஈ-மருத்துவமனை போர்டல் என்றால் என்ன?", "answer": "தயவுசெய்து இந்த பதிலுக்கு மொழிபெயர்க்கவும்."},
                {"question": "போர்டல் இலவசமானதா?", "answer": "தயவுசெய்து இந்த பதிலுக்கு மொழிபெயர்க்கவும்."},
                {"question": "யார் பயன்படுத்தலாம்?", "answer": "தயவுசெய்து இந்த பதிலுக்கு மொழிபெயர்க்கவும்."},
                {"question": "'ஸ்மார்ட் டாக்டர்' என்றால் என்ன?", "answer": "தயவுசெய்து இந்த பதிலுக்கு மொழிபெயர்க்கவும்."},
                {"question": "மருத்துவரை எப்படி பதிவு செய்வது?", "answer": "தயவுசெய்து இந்த பதிலுக்கு மொழிபெயர்க்கவும்."},
                {"question": "பதிவுக்கு என்ன தகவல் தேவை?", "answer": "தயவுசெய்து இந்த பதிலுக்கு மொழிபெயர்க்கவும்."},
                {"question": "ஆதார் அட்டை மூலம் பதிவு செய்யலாமா?", "answer": "தயவுசெய்து இந்த பதிலுக்கு மொழிபெயர்க்கவும்."},
                {"question": "கடவுச்சொல்லை மறந்துவிட்டேன்.", "answer": "தயவுசெய்து இந்த பதிலுக்கு மொழிபெயர்க்கவும்."},
                {"question": "தனிப்பட்ட தகவலை எப்படி புதுப்பிப்பது?", "answer": "தயவுசெய்து இந்த பதிலுக்கு மொழிபெயர்க்கவும்."},
                {"question": "சுகாதார பதிவுகள் பாதுகாப்பானதா?", "answer": "தயவுசெய்து இந்த பதிலுக்கு மொழிபெயர்க்கவும்."},
                {"question": "எனது தரவு எப்படி பயன்படுத்தப்படுகிறது?", "answer": "தயவுசெய்து இந்த பதிலுக்கு மொழிபெயர்க்கவும்."},
                {"question": "'இரத்த தானம் நெட்வொர்க்' என்றால் என்ன?", "answer": "தயவுசெய்து இந்த பதிலுக்கு மொழிபெயர்க்கவும்."},
                {"question": "ஆன்லைனில் ஆய்வக அறிக்கைகளை பார்க்கலாமா?", "answer": "தயவுசெய்து இந்த பதிலுக்கு மொழிபெயர்க்கவும்."},
                {"question": "'அறிகுறிகள் வழிகாட்டி' என்றால் என்ன?", "answer": "தயவுசெய்து இந்த பதிலுக்கு மொழிபெயர்க்கவும்."},
                {"question": "மின்-பரிந்துரைகள் எப்படி வேலை செய்கின்றன?", "answer": "தயவுசெய்து இந்த பதிலுக்கு மொழிபெயர்க்கவும்."},
                {"question": "அவசர நிலையில் என்ன செய்ய வேண்டும்?", "answer": "தயவுசெய்து இந்த பதிலுக்கு மொழிபெயர்க்கவும்."},
                {"question": "'சுகாதார குறிப்புகள்' பிரிவு என்றால் என்ன?", "answer": "தயவுசெய்து இந்த பதிலுக்கு மொழிபெயர்க்கவும்."},
                {"question": "மருத்துவமனை அல்லது மருத்துவர் பற்றி கருத்து தெரிவிக்கலாமா?", "answer": "தயவுசெய்து இந்த பதிலுக்கு மொழிபெயர்க்கவும்."},
                {"question": "ஒரு மருத்துவமனை கிடைக்கவில்லை என்றால்?", "answer": "தயவுசெய்து இந்த பதிலுக்கு மொழிபெயர்க்கவும்."},
                {"question": "எந்த வலைத்தளங்கள் ஆதரிக்கப்படுகின்றன?", "answer": "தயவுசெய்து இந்த பதிலுக்கு மொழிபெயர்க்கவும்."},
                {"question": "தொழில்நுட்ப சிக்கல் உள்ளது.", "answer": "தயவுசெய்து இந்த பதிலுக்கு மொழிபெயர்க்கவும்."}
            ]
        }
    
    st.title(lang_data.get("title", "FAQ - Frequently Asked Questions"))
    st.markdown("---")

    faq_list = lang_data.get("faq_list", [])
    if st.session_state.language == "हिन्दी":
        faq_list = lang_data.get("faq_list_hi", [])
    elif st.session_state.language == "தமிழ்":
        faq_list = lang_data.get("faq_list_ta", [])

    # Grouping logic remains the same
    sections = {
        lang_data.get("section_general", "General Questions"): faq_list[0:4],
        lang_data.get("section_registration", "Registration & Account Management"): faq_list[5:9],
        lang_data.get("section_services", "Services & Features"): faq_list[9:17],
        lang_data.get("section_security", "Security & Privacy"): faq_list[9:11],
        lang_data.get("section_technical", "Technical Support"): faq_list[19:21]
    }

    # Correction: The sections list was not properly slicing the questions.
    # The fix below makes it more robust.
    
    sections = {
        lang_data.get("section_general", "General Questions"): faq_list[0:4],
        lang_data.get("section_registration", "Registration & Account Management"): faq_list[4:9],
        lang_data.get("section_services", "Services & Features"): faq_list[9:18],
        lang_data.get("section_technical", "Technical Support"): faq_list[18:21]
    }

    # Render the sections and expanders
    for section, faqs in sections.items():
        st.header(section)
        for item in faqs:
            with st.expander(f"**{item['question']}**", expanded=False):
                st.write(item['answer'])

    # Adding a contact section at the end
    st.markdown("---")
    st.subheader("Still Have Questions?")
    st.info("If you couldn't find the answer you were looking for, please feel free to contact our support team via the 'Contact' page.")