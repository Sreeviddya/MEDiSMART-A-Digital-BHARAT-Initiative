import streamlit as st

def show_page():
    # --- Language Dictionary for this page ---
    translations = {
        "English": {
            "title": "About E-Hospital Portal",
            "tagline": "Bridging Healthcare with Technology",
            "introduction": "The E-Hospital Portal is a comprehensive digital health platform designed to simplify access to medical information and services for every citizen.",
            "principles_title": "Our Guiding Principles",
            "principles_list": {
                "Accessibility": "Ensuring our services are available to all, regardless of location or economic status.",
                "Transparency": "Maintaining open communication and data integrity to build trust with our citizens.",
                "Innovation": "Continuously leveraging new technologies to improve healthcare delivery.",
                "Citizen-Centricity": "Placing the needs and well-being of the citizen at the core of every decision."
            },
            "journey_title": "Our Journey",
            "journey_para": "The E-Hospital Portal was conceptualized as part of the National Digital Health Mission to create a seamless and integrated healthcare experience for every Indian citizen. It began with a pilot project in a few states, and its success has led to a nationwide rollout. Our journey is a testament to the power of public-private collaboration and a shared vision for a healthier India.",
            "leadership_title": "Leadership Team",
            "leadership_members": [
                {"name": "Dr. Ananya Sharma", "role": "Director General"},
                {"name": "Mr. Rajesh Kumar", "role": "Chief Technology Officer"},
                {"name": "Ms. Priya Singh", "role": "Head of Public Relations"}
            ],
            "collaborations_title": "Strategic Collaborations",
            "collaborations_para": "We work closely with the Ministry of Health & Family Welfare, various state governments, leading medical research institutes, and technology partners to ensure our platform is robust, secure, and aligned with national health goals.",
            "roadmap_title": "The Road Ahead",
            "roadmap_para": "Our future plans include the integration of AI-driven personalized health advice, expansion of our telemedicine network to remote areas, and the development of a unified health data repository to support public health research and policy-making.",
            "vision_title": "Our Vision",
            "vision_para": """To establish a unified, transparent, and accessible healthcare ecosystem across India. By integrating hospitals, clinics, doctors, and patients under one 
            government-supported digital platform, we aim to remove geographical and administrative barriers. This vision focuses on ensuring that every citizen, whether in rural or urban areas, has equal access 
            to reliable healthcare services at their fingertips.""",
            "mission_title": "Our Mission",
            "mission_para": """To leverage emerging technologies like Artificial Intelligence, Machine Learning, and IoT to improve healthcare delivery. Our goal is to provide real-time hospital 
            information, doctor availability, online consultation facilities, emergency blood donation alerts, and digitized health records linked with unique IDs like Aadhaar. We are committed to making healthcare 
            affordable, efficient, and citizen-centric while empowering doctors and hospitals with a seamless digital infrastructure.""",
            "commitment_title": "Our Commitment",
            "commitment_para": "We are dedicated to providing a secure, reliable, and user-friendly platform. Our commitment is to empower you with the information you need to make informed decisions about your health.",
            "disclaimer_title": "Important Disclaimer",
            "disclaimer_para": "The predictive tools and information on this platform are for informational purposes only. They are not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or a qualified healthcare provider with any questions you may have regarding a medical condition."
        },
        "हिन्दी": {
            "title": "ई-हॉस्पिटल पोर्टल के बारे में",
            "tagline": "स्वास्थ्य सेवा और प्रौद्योगिकी को जोड़ना",
            "introduction": "ई-हॉस्पिटल पोर्टल एक व्यापक डिजिटल स्वास्थ्य मंच है जिसे हर नागरिक के लिए चिकित्सा जानकारी और सेवाओं तक पहुंच को सरल बनाने के लिए डिज़ाइन किया गया है।",
            "principles_title": "हमारे मार्गदर्शक सिद्धांत",
            "principles_list": {
                "पहुंचयोग्यता": "यह सुनिश्चित करना कि हमारी सेवाएँ हर किसी के लिए, उनकी भौगोलिक स्थिति या आर्थिक स्थिति की परवाह किए बिना उपलब्ध हों।",
                "पारदर्शिता": "नागरिकों के साथ विश्वास बनाने के लिए खुली बातचीत और डेटा अखंडता बनाए रखना।",
                "नवाचार": "स्वास्थ्य सेवा वितरण में सुधार के लिए नई तकनीकों का लगातार उपयोग करना।",
                "नागरिक-केंद्रितता": "हर निर्णय के मूल में नागरिक की जरूरतों और भलाई को रखना।"
            },
            "journey_title": "हमारी यात्रा",
            "journey_para": "ई-हॉस्पिटल पोर्टल की कल्पना राष्ट्रीय डिजिटल स्वास्थ्य मिशन के एक भाग के रूप में हर भारतीय नागरिक के लिए एक सहज और एकीकृत स्वास्थ्य सेवा अनुभव बनाने के लिए की गई थी। इसकी शुरुआत कुछ राज्यों में एक पायलट परियोजना के साथ हुई थी, और इसकी सफलता ने इसे राष्ट्रव्यापी स्तर पर लागू करने के लिए प्रेरित किया। हमारी यात्रा सार्वजनिक-निजी सहयोग और एक स्वस्थ भारत के लिए एक साझा दृष्टिकोण की शक्ति का प्रमाण है।",
            "leadership_title": "नेतृत्व टीम",
            "leadership_members": [
                {"name": "डॉ. अनन्या शर्मा", "role": "महानिदेशक"},
                {"name": "श्री राजेश कुमार", "role": "मुख्य प्रौद्योगिकी अधिकारी"},
                {"name": "श्रीमती प्रिया सिंह", "role": "जनसंपर्क प्रमुख"}
            ],
            "collaborations_title": "रणनीतिक सहयोग",
            "collaborations_para": "हम अपने मंच को मजबूत, सुरक्षित और राष्ट्रीय स्वास्थ्य लक्ष्यों के अनुरूप बनाने के लिए स्वास्थ्य और परिवार कल्याण मंत्रालय, विभिन्न राज्य सरकारों, प्रमुख चिकित्सा अनुसंधान संस्थानों और प्रौद्योगिकी भागीदारों के साथ मिलकर काम करते हैं।",
            "roadmap_title": "आगे का रास्ता",
            "roadmap_para": "हमारी भविष्य की योजनाओं में एआई-संचालित व्यक्तिगत स्वास्थ्य सलाह का एकीकरण, दूरदराज के क्षेत्रों में हमारे टेलीमेडिसिन नेटवर्क का विस्तार, और सार्वजनिक स्वास्थ्य अनुसंधान और नीति निर्माण का समर्थन करने के लिए एक एकीकृत स्वास्थ्य डेटा भंडार का विकास शामिल है।",
            "vision_title": "हमारी दृष्टि",
            "vision_para": """पूरे भारत में एक एकीकृत, पारदर्शी और सुलभ स्वास्थ्य प्रणाली स्थापित करना। अस्पतालों, क्लीनिकों, डॉक्टरों और मरीजों को एक सरकारी-समर्थित डिजिटल प्लेटफॉर्म के तहत जोड़कर, हम भौगोलिक और प्रशासनिक बाधाओं को दूर करना चाहते हैं। यह दृष्टि सुनिश्चित करती है कि हर नागरिक, चाहे वह ग्रामीण या शहरी क्षेत्रों में हो, उसकी उंगलियों पर विश्वसनीय स्वास्थ्य सेवाओं तक समान पहुंच हो।""",
            "mission_title": "हमारा मिशन",
            "mission_para": """स्वास्थ्य सेवा वितरण को बेहतर बनाने के लिए आर्टिफिशियल इंटेलिजेंस, मशीन लर्निंग और IoT जैसी उभरती प्रौद्योगिकियों का लाभ उठाना। हमारा लक्ष्य वास्तविक समय में अस्पताल की जानकारी, डॉक्टर की उपलब्धता, ऑनलाइन परामर्श सुविधाएं, आपातकालीन रक्त दान अलर्ट और आधार जैसी अद्वितीय आईडी से जुड़े डिजिटाइज़्ड स्वास्थ्य रिकॉर्ड प्रदान करना है। हम स्वास्थ्य सेवा को किफायती, कुशल और नागरिक-केंद्रित बनाने के लिए प्रतिबद्ध हैं, जबकि डॉक्टरों और अस्पतालों को एक निर्बाध डिजिटल बुनियादी ढांचा प्रदान करते हैं।""",
            "commitment_title": "हमारी प्रतिबद्धता",
            "commitment_para": "हम एक सुरक्षित, विश्वसनीय और उपयोगकर्ता के अनुकूल मंच प्रदान करने के लिए समर्पित हैं। हमारी प्रतिबद्धता आपको अपने स्वास्थ्य के बारे में सूचित निर्णय लेने के लिए आवश्यक जानकारी से सशक्त बनाना है।",
            "disclaimer_title": "महत्वपूर्ण अस्वीकरण",
            "disclaimer_para": "इस प्लेटफॉर्म पर पूर्वानुमानित उपकरण और जानकारी केवल सूचनात्मक उद्देश्यों के लिए हैं। वे पेशेवर चिकित्सा सलाह, निदान, या उपचार का विकल्प नहीं हैं। चिकित्सा स्थिति के संबंध में आपके किसी भी प्रश्न के लिए हमेशा अपने चिकित्सक या एक योग्य स्वास्थ्य सेवा प्रदाता की सलाह लें।"
        },
        "தமிழ்": {
            "title": "மின் மருத்துவமனை தளம் பற்றி",
            "tagline": "தொழில்நுட்பத்துடன் சுகாதாரத்தை இணைத்தல்",
            "introduction": "மின் மருத்துவமனை தளம் என்பது ஒவ்வொரு குடிமகனுக்கும் மருத்துவ தகவல் மற்றும் சேவைகளை எளிதாக்க வடிவமைக்கப்பட்ட ஒரு விரிவான டிஜிட்டல் சுகாதார தளமாகும்.",
            "principles_title": "எங்கள் வழிகாட்டுதல் கொள்கைகள்",
            "principles_list": {
                "அணுகல்தன்மை": "இருப்பிடம் அல்லது பொருளாதார நிலையைப் பொருட்படுத்தாமல், எங்கள் சேவைகள் அனைவருக்கும் கிடைக்கச் செய்தல்.",
                "வெளிப்படைத்தன்மை": "குடிமக்களுடன் நம்பிக்கையை உருவாக்க திறந்த தொடர்பு மற்றும் தரவு ஒருமைப்பாட்டைப் பராமரித்தல்.",
                "புத்தாக்கம்": "சுகாதார சேவை விநியோகத்தை மேம்படுத்த புதிய தொழில்நுட்பங்களை தொடர்ந்து பயன்படுத்துதல்.",
                "குடிமக்கள்-மையம்": "ஒவ்வொரு முடிவின் மையத்திலும் குடிமகனின் தேவைகளையும் நலன்களையும் வைத்திருத்தல்."
            },
            "journey_title": "எங்கள் பயணம்",
            "journey_para": "ஒவ்வொரு இந்திய குடிமகனுக்கும் தடையற்ற மற்றும் ஒருங்கிணைந்த சுகாதார அனுபவத்தை உருவாக்குவதற்காக தேசிய டிஜிட்டல் சுகாதார இயக்கத்தின் ஒரு பகுதியாக மின் மருத்துவமனை தளம் உருவாக்கப்பட்டது. இது ஒரு சில மாநிலங்களில் ஒரு முன்னோடி திட்டத்துடன் தொடங்கியது, அதன் வெற்றி நாடு தழுவிய அளவில் செயல்படுத்த வழிவகுத்தது. எங்கள் பயணம் பொது-தனியார் ஒத்துழைப்பின் சக்தி மற்றும் ஒரு ஆரோக்கியமான இந்தியாவுக்கான ஒரு பொதுவான பார்வைக்கு சான்றாகும்.",
            "leadership_title": "தலைமை குழு",
            "leadership_members": [
                {"name": "டாக்டர் அனன்யா ஷர்மா", "role": "தலைமை இயக்குநர்"},
                {"name": "திரு. ராஜேஷ் குமார்", "role": "தலைமை தொழில்நுட்ப அதிகாரி"},
                {"name": "திருமதி. பிரியா சிங்", "role": "மக்கள் தொடர்புத் தலைவர்"}
            ],
            "collaborations_title": "மூலோபாய ஒத்துழைப்புகள்",
            "collaborations_para": "எங்கள் தளம் வலுவானது, பாதுகாப்பானது மற்றும் தேசிய சுகாதார இலக்குகளுடன் ஒத்துப்போகிறது என்பதை உறுதிப்படுத்த, சுகாதார மற்றும் குடும்ப நல அமைச்சகம், பல்வேறு மாநில அரசுகள், முன்னணி மருத்துவ ஆராய்ச்சி நிறுவனங்கள் மற்றும் தொழில்நுட்ப கூட்டாளர்களுடன் நாங்கள் நெருக்கமாக பணியாற்றுகிறோம்.",
            "roadmap_title": "முன்னோக்கிய பாதை",
            "roadmap_para": "எங்கள் எதிர்கால திட்டங்களில் AI-உந்துதல் தனிப்பயனாக்கப்பட்ட சுகாதார ஆலோசனையின் ஒருங்கிணைப்பு, தொலைதூர பகுதிகளுக்கு எங்கள் தொலைமருத்துவ வலையமைப்பை விரிவுபடுத்துதல், மற்றும் பொது சுகாதார ஆராய்ச்சி மற்றும் கொள்கை உருவாக்கத்தை ஆதரிக்க ஒரு ஒருங்கிணைந்த சுகாதார தரவு களஞ்சியத்தை உருவாக்குதல் ஆகியவை அடங்கும்.",
            "vision_title": "எங்கள் நோக்கம்",
            "vision_para": """இந்தியா முழுவதும் ஒரு ஒருங்கிணைந்த, வெளிப்படையான மற்றும் அணுகக்கூடிய சுகாதார சூழலை நிறுவுதல். மருத்துவமனைகள், கிளினிக்குகள், மருத்துவர்கள் மற்றும் நோயாளிகளை ஒரு அரசாங்க ஆதரவு டிஜிட்டல் தளத்தின் கீழ் ஒருங்கிணைப்பதன் மூலம், புவியியல் மற்றும் நிர்வாக தடைகளை நீக்க நாங்கள் நோக்கமாக கொண்டுள்ளோம். இந்த நோக்கம், கிராமப்புறங்கள் அல்லது நகர்ப்புறங்களில் உள்ள ஒவ்வொரு குடிமகனுக்கும் நம்பகமான சுகாதார சேவைகளை எளிதாக அணுகுவதை உறுதி செய்வதில் கவனம் செலுத்துகிறது.""",
            "mission_title": "எங்கள் பணி",
            "mission_para": """ஆர்ட்டிஃபிஷியல் இன்டலிஜென்ஸ், மெஷின் லேர்னிங் மற்றும் ஐஓடி போன்ற வளர்ந்து வரும் தொழில்நுட்பங்களை பயன்படுத்தி சுகாதார விநியோகத்தை மேம்படுத்துதல். நிகழ்நேர மருத்துவமனை தகவல், மருத்துவர் கிடைக்கும் நிலை, ஆன்லைன் ஆலோசனை வசதிகள், அவசர இரத்த தான எச்சரிக்கைகள் மற்றும் ஆதார் போன்ற தனிப்பட்ட அடையாளங்களுடன் இணைக்கப்பட்ட டிஜிட்டல் சுகாதார பதிவுகளை வழங்குவதே எங்கள் நோக்கம். நாங்கள் சுகாதாரத்தை மலிவானதாகவும், திறமையானதாகவும், குடிமக்கள் மையமாகவும் மாற்ற உறுதியாக இருக்கிறோம், அதே நேரத்தில் மருத்துவர்கள் மற்றும் மருத்துவமனைகளுக்கு ஒரு தடையற்ற டிஜிட்டல் உள்கட்டமைப்பை வழங்குகிறோம்.""",
            "commitment_title": "எங்கள் அர்ப்பணிப்பு",
            "commitment_para": "பாதுகாப்பான, நம்பகமான மற்றும் பயனர் நட்பு தளத்தை வழங்குவதில் நாங்கள் அர்ப்பணிப்புடன் உள்ளோம். உங்கள் உடல்நலம் பற்றி அறிந்த முடிவுகளை எடுக்க உங்களுக்கு தேவையான தகவல்களை வழங்க எங்கள் அர்ப்பணிப்பு உள்ளது.",
            "disclaimer_title": "முக்கியமான மறுப்பு",
            "disclaimer_para": "இந்த தளத்தில் உள்ள முன்கணிப்பு கருவிகள் மற்றும் தகவல்கள் தகவல் நோக்கங்களுக்காக மட்டுமே. அவை தொழில்முறை மருத்துவ ஆலோசனை, நோயறிதல் அல்லது சிகிச்சைக்கு மாற்றாக இல்லை. மருத்துவ நிலை குறித்து உங்களுக்கு ஏதேனும் கேள்விகள் இருந்தால் எப்போதும் உங்கள் மருத்துவர் அல்லது தகுதிவாய்ந்த சுகாதார வழங்குநரின் ஆலோசனையை நாடுங்கள்."
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

    # Our Vision & Mission
    st.subheader(lang_data["vision_title"])
    st.write(lang_data["vision_para"])
    st.subheader(lang_data["mission_title"])
    st.write(lang_data["mission_para"])
    
    st.markdown("---")
    
    # Guiding Principles
    st.subheader(lang_data["principles_title"])
    for principle, desc in lang_data["principles_list"].items():
        with st.expander(f"**{principle}**"):
            st.write(desc)

    st.markdown("---")

    # Our Journey
    st.subheader(lang_data["journey_title"])
    st.write(lang_data["journey_para"])

    st.markdown("---")

    # Leadership Team
    st.subheader(lang_data["leadership_title"])
    cols = st.columns(len(lang_data["leadership_members"]))
    for i, member in enumerate(lang_data["leadership_members"]):
        with cols[i]:
            st.markdown(f"**{member['name']}**")
            st.markdown(f"*{member['role']}*")

    st.markdown("---")
    
    # Strategic Collaborations
    st.subheader(lang_data["collaborations_title"])
    st.write(lang_data["collaborations_para"])
    
    st.markdown("---")
    
    # The Road Ahead
    st.subheader(lang_data["roadmap_title"])
    st.write(lang_data["roadmap_para"])

    st.markdown("---")

    # Our Commitment
    st.subheader(lang_data["commitment_title"])
    st.write(lang_data["commitment_para"])

    st.markdown("---")

    # Disclaimer
    st.subheader(lang_data["disclaimer_title"])
    st.info(lang_data["disclaimer_para"])
