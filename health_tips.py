import streamlit as st

def show_page():
    # --- Language Dictionary for this page ---
    translations = {
        "English": {
            "title": "Health and Wellness Tips",
            "tagline": "A Comprehensive Guide to a Healthier Life",
            "introduction": "This page provides essential health and wellness tips curated by medical experts. Implementing these simple practices into your daily routine can significantly improve your overall well-being and help prevent common diseases.",
            "section_nutrition_title": "Nutrition: Fueling Your Body",
            "nutrition_tip1_title": "Balanced Diet",
            "nutrition_tip1_text": "Ensure your diet includes a variety of fruits, vegetables, whole grains, lean proteins, and healthy fats. A balanced diet provides the necessary vitamins, minerals, and nutrients to support bodily functions and boost immunity.",
            "nutrition_tip2_title": "Hydration",
            "nutrition_tip2_text": "Drinking an adequate amount of water (8-10 glasses per day) is crucial for maintaining bodily functions, regulating body temperature, and flushing out toxins. Avoid sugary drinks and excessive caffeine.",
            "nutrition_tip3_title": "Mindful Eating",
            "nutrition_tip3_text": "Pay attention to your body's hunger and fullness cues. Eat slowly and savor your meals. This can help prevent overeating and improve digestion.",

            "section_physical_activity_title": "Physical Activity: Move for Health",
            "physical_tip1_title": "Regular Exercise",
            "physical_tip1_text": "Aim for at least 30 minutes of moderate-intensity exercise, such as brisk walking, cycling, or swimming, most days of the week. Physical activity strengthens your heart, improves mood, and helps manage weight.",
            "physical_tip2_title": "Flexibility and Strength",
            "physical_tip2_text": "Incorporate strength training exercises (e.g., using weights or bodyweight) and flexibility exercises (e.g., stretching, yoga) into your routine at least twice a week to build muscle and improve joint health.",
            "physical_tip3_title": "Active Lifestyle",
            "physical_tip3_text": "Look for ways to be more active throughout the day, such as taking the stairs instead of the elevator, walking during phone calls, or doing light stretches while watching television.",

            "section_mental_wellness_title": "Mental Wellness: Nurturing Your Mind",
            "mental_tip1_title": "Stress Management",
            "mental_tip1_text": "Practice stress-reducing activities like meditation, deep breathing exercises, or hobbies. Chronic stress can negatively impact both mental and physical health.",
            "mental_tip2_title": "Quality Sleep",
            "mental_tip2_text": "Aim for 7-9 hours of quality sleep per night. Establish a consistent sleep schedule and create a relaxing bedtime routine to improve sleep quality, which is vital for cognitive function and emotional regulation.",
            "mental_tip3_title": "Social Connection",
            "mental_tip3_text": "Maintain strong social bonds with family and friends. A supportive social network can reduce feelings of loneliness and provide a sense of belonging.",

            "section_hygiene_title": "Hygiene and Disease Prevention",
            "hygiene_tip1_title": "Hand Hygiene",
            "hygiene_tip1_text": "Wash your hands with soap and water frequently, especially before eating and after using the restroom. This is the simplest and most effective way to prevent the spread of infections.",
            "hygiene_tip2_title": "Vaccination",
            "hygiene_tip2_text": "Stay up-to-date with recommended vaccinations. Vaccines are a safe and effective way to protect yourself and your community from infectious diseases.",
            "hygiene_tip3_title": "Regular Check-ups",
            "hygiene_tip3_text": "Schedule regular health check-ups with your doctor. Early detection and management of health issues are key to a long and healthy life.",
            
            "section_laws_title": "Health Laws and Public Initiatives",
            "laws_intro": "Public health is a shared responsibility. The Government of India continuously implements and enforces various laws and initiatives to protect citizens' health. Following the tips on this page is a crucial step in supporting these national efforts. For example, maintaining personal hygiene directly contributes to the success of public health campaigns aimed at preventing infectious diseases.",
            "laws_point1": "The National Health Policy aims to improve public health standards and access to quality healthcare for all citizens. Your proactive health measures align with its goals.",
            "laws_point2": "Public awareness campaigns on nutrition, physical activity, and mental health are central to government health strategies. Adhering to these tips helps strengthen these initiatives from the grassroots level.",

            "disclaimer_title": "Important Disclaimer",
            "disclaimer_text": "The health tips provided on this platform are for informational purposes only. They are not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or a qualified healthcare provider with any questions you may have regarding a medical condition."
        },
        "हिन्दी": {
            "title": "स्वास्थ्य और कल्याण युक्तियाँ",
            "tagline": "एक स्वस्थ जीवन के लिए एक व्यापक मार्गदर्शिका",
            "introduction": "यह पृष्ठ चिकित्सा विशेषज्ञों द्वारा संकलित आवश्यक स्वास्थ्य और कल्याण युक्तियाँ प्रदान करता है। इन सरल प्रथाओं को अपनी दैनिक दिनचर्या में लागू करने से आपके समग्र कल्याण में काफी सुधार हो सकता है और सामान्य बीमारियों को रोकने में मदद मिल सकती है।",
            "section_nutrition_title": "पोषण: अपने शरीर को ईंधन देना",
            "nutrition_tip1_title": "संतुलित आहार",
            "nutrition_tip1_text": "सुनिश्चित करें कि आपके आहार में विभिन्न प्रकार के फल, सब्जियां, साबुत अनाज, लीन प्रोटीन और स्वस्थ वसा शामिल हैं। एक संतुलित आहार शरीर के कार्यों का समर्थन करने और प्रतिरक्षा को बढ़ावा देने के लिए आवश्यक विटामिन, खनिज और पोषक तत्व प्रदान करता है।",
            "nutrition_tip2_title": "जलयोजन",
            "nutrition_tip2_text": "पर्याप्त मात्रा में पानी (प्रतिदिन 8-10 गिलास) पीना शरीर के कार्यों को बनाए रखने, शरीर के तापमान को नियंत्रित करने और विषाक्त पदार्थों को बाहर निकालने के लिए महत्वपूर्ण है। शर्करा युक्त पेय और अत्यधिक कैफीन से बचें।",
            "nutrition_tip3_title": "सजग होकर भोजन करना",
            "nutrition_tip3_text": "अपने शरीर की भूख और पेट भरने के संकेतों पर ध्यान दें। धीरे-धीरे खाएं और अपने भोजन का स्वाद लें। यह अधिक खाने से रोकने और पाचन में सुधार करने में मदद कर सकता है।",

            "section_physical_activity_title": "शारीरिक गतिविधि: स्वास्थ्य के लिए चलें",
            "physical_tip1_title": "नियमित व्यायाम",
            "physical_tip1_text": "सप्ताह के अधिकांश दिनों में 30 मिनट के मध्यम-तीव्रता वाले व्यायाम, जैसे तेज चलना, साइकिल चलाना या तैराकी का लक्ष्य रखें। शारीरिक गतिविधि आपके दिल को मजबूत करती है, मूड में सुधार करती है और वजन को नियंत्रित करने में मदद करती है।",
            "physical_tip2_title": "लचीलापन और ताकत",
            "physical_tip2_text": "मांसपेशियों का निर्माण और जोड़ों के स्वास्थ्य में सुधार के लिए सप्ताह में कम से कम दो बार अपने दिनचर्या में शक्ति प्रशिक्षण अभ्यास (जैसे, वजन या शरीर के वजन का उपयोग करके) और लचीलापन अभ्यास (जैसे, स्ट्रेचिंग, योग) को शामिल करें।",
            "physical_tip3_title": "सक्रिय जीवनशैली",
            "physical_tip3_text": "दिन भर में अधिक सक्रिय रहने के तरीके खोजें, जैसे लिफ्ट के बजाय सीढ़ियों का उपयोग करना, फोन पर बात करते समय चलना, या टेलीविजन देखते समय हल्के स्ट्रेच करना।",

            "section_mental_wellness_title": "मानसिक कल्याण: अपने मन का पोषण करना",
            "mental_tip1_title": "तनाव प्रबंधन",
            "mental_tip1_text": "ध्यान, गहरी साँस लेने के अभ्यास या शौक जैसी तनाव कम करने वाली गतिविधियों का अभ्यास करें। पुराना तनाव मानसिक और शारीरिक स्वास्थ्य दोनों को नकारात्मक रूप से प्रभावित कर सकता है।",
            "mental_tip2_title": "गुणवत्तापूर्ण नींद",
            "mental_tip2_text": "प्रति रात 7-9 घंटे की गुणवत्तापूर्ण नींद का लक्ष्य रखें। एक सुसंगत नींद अनुसूची स्थापित करें और संज्ञानात्मक कार्य और भावनात्मक नियमन के लिए महत्वपूर्ण नींद की गुणवत्ता में सुधार के लिए एक आरामदायक सोने का समय दिनचर्या बनाएं।",
            "mental_tip3_title": "सामाजिक संबंध",
            "mental_tip3_text": "परिवार और दोस्तों के साथ मजबूत सामाजिक संबंध बनाए रखें। एक सहायक सामाजिक नेटवर्क अकेलेपन की भावनाओं को कम कर सकता है और संबंधित होने की भावना प्रदान कर सकता है।",
            
            "section_hygiene_title": "स्वच्छता और रोग निवारण",
            "hygiene_tip1_title": "हाथों की स्वच्छता",
            "hygiene_tip1_text": "अपने हाथों को साबुन और पानी से बार-बार धोएं, खासकर खाने से पहले और शौचालय का उपयोग करने के बाद। यह संक्रमण के प्रसार को रोकने का सबसे सरल और सबसे प्रभावी तरीका है।",
            "hygiene_tip2_title": "टीकाकरण",
            "hygiene_tip2_text": "अनुशंसित टीकाकरण के साथ अद्यतित रहें। टीके संक्रामक रोगों से खुद को और अपने समुदाय को बचाने का एक सुरक्षित और प्रभावी तरीका हैं।",
            "hygiene_tip3_title": "नियमित जांच",
            "hygiene_tip3_text": "अपने डॉक्टर के साथ नियमित स्वास्थ्य जांच निर्धारित करें। स्वास्थ्य समस्याओं का शीघ्र पता लगाना और प्रबंधन एक लंबे और स्वस्थ जीवन की कुंजी है।",

            "section_laws_title": "स्वास्थ्य कानून और सार्वजनिक पहल",
            "laws_intro": "सार्वजनिक स्वास्थ्य एक साझा जिम्मेदारी है। भारत सरकार लगातार नागरिकों के स्वास्थ्य की रक्षा के लिए विभिन्न कानूनों और पहलों को लागू और लागू करती है। इस पृष्ठ पर दी गई युक्तियों का पालन करना इन राष्ट्रीय प्रयासों का समर्थन करने में एक महत्वपूर्ण कदम है। उदाहरण के लिए, व्यक्तिगत स्वच्छता बनाए रखना सीधे संक्रामक रोगों को रोकने के उद्देश्य से सार्वजनिक स्वास्थ्य अभियानों की सफलता में योगदान देता है।",
            "laws_point1": "राष्ट्रीय स्वास्थ्य नीति का उद्देश्य सभी नागरिकों के लिए सार्वजनिक स्वास्थ्य मानकों और गुणवत्तापूर्ण स्वास्थ्य सेवा तक पहुंच में सुधार करना है। आपके सक्रिय स्वास्थ्य उपाय इसके लक्ष्यों के अनुरूप हैं।",
            "laws_point2": "पोषण, शारीरिक गतिविधि और मानसिक स्वास्थ्य पर सार्वजनिक जागरूकता अभियान सरकारी स्वास्थ्य रणनीतियों के लिए केंद्रीय हैं। इन युक्तियों का पालन करना जमीनी स्तर से इन पहलों को मजबूत करने में मदद करता है।",
            
            "disclaimer_title": "महत्वपूर्ण अस्वीकरण",
            "disclaimer_text": "इस प्लेटफॉर्म पर दी गई स्वास्थ्य युक्तियाँ केवल सूचनात्मक उद्देश्यों के लिए हैं। वे पेशेवर चिकित्सा सलाह, निदान, या उपचार का विकल्प नहीं हैं। चिकित्सा स्थिति के संबंध में आपके किसी भी प्रश्न के लिए हमेशा अपने चिकित्सक या एक योग्य स्वास्थ्य सेवा प्रदाता की सलाह लें।"
        },
        "தமிழ்": {
            "title": "சுகாதாரம் மற்றும் நல்வாழ்வு குறிப்புகள்",
            "tagline": "ஆரோக்கியமான வாழ்க்கைக்கான ஒரு விரிவான வழிகாட்டி",
            "introduction": "இந்த பக்கம் மருத்துவ நிபுணர்களால் தொகுக்கப்பட்ட அத்தியாவசிய சுகாதாரம் மற்றும் நல்வாழ்வு குறிப்புகளை வழங்குகிறது. இந்த எளிய நடைமுறைகளை உங்கள் அன்றாட வழக்கத்தில் செயல்படுத்துவது உங்கள் ஒட்டுமொத்த நல்வாழ்வை கணிசமாக மேம்படுத்தலாம் மற்றும் பொதுவான நோய்களைத் தடுக்க உதவும்.",
            "section_nutrition_title": "ஊட்டச்சத்து: உங்கள் உடலுக்கு எரிபொருள்",
            "nutrition_tip1_title": "சமச்சீர் உணவு",
            "nutrition_tip1_text": "உங்கள் உணவில் பல்வேறு வகையான பழங்கள், காய்கறிகள், முழு தானியங்கள், மெலிந்த புரதங்கள் மற்றும் ஆரோக்கியமான கொழுப்புகள் ஆகியவை இருப்பதை உறுதிப்படுத்தவும். ஒரு சமச்சீர் உணவு உடல் செயல்பாடுகளை ஆதரிக்கவும், நோய் எதிர்ப்பு சக்தியை அதிகரிக்கவும் தேவையான வைட்டமின்கள், தாதுக்கள் மற்றும் ஊட்டச்சத்துக்களை வழங்குகிறது.",
            "nutrition_tip2_title": "நீரேற்றம்",
            "nutrition_tip2_text": "போதுமான அளவு தண்ணீர் (ஒரு நாளைக்கு 8-10 கிளாஸ்) குடிப்பது உடல் செயல்பாடுகளைப் பராமரிக்கவும், உடல் வெப்பநிலையை ஒழுங்குபடுத்தவும், மற்றும் நச்சுக்களை வெளியேற்றவும் முக்கியமானது. சர்க்கரை பானங்கள் மற்றும் அதிகப்படியான காஃபின் ஆகியவற்றைத் தவிர்க்கவும்.",
            "nutrition_tip3_title": "நினைவில் கொண்டு உண்ணுதல்",
            "nutrition_tip3_text": "உங்கள் உடலின் பசி மற்றும் நிறைவு சமிக்ஞைகளுக்கு கவனம் செலுத்துங்கள். மெதுவாக சாப்பிட்டு உங்கள் உணவை ரசியுங்கள். இது அதிகமாக சாப்பிடுவதைத் தடுக்கவும், செரிமானத்தை மேம்படுத்தவும் உதவும்.",

            "section_physical_activity_title": "உடல் செயல்பாடு: ஆரோக்கியத்திற்காக நகரவும்",
            "physical_tip1_title": "வழக்கமான உடற்பயிற்சி",
            "physical_tip1_text": "வாரத்தின் பெரும்பாலான நாட்களில், வேகமாக நடத்தல், சைக்கிள் ஓட்டுதல் அல்லது நீச்சல் போன்ற 30 நிமிட மிதமான-தீவிர உடற்பயிற்சியை நோக்கமாகக் கொள்ளுங்கள். உடல் செயல்பாடு உங்கள் இதயத்தை பலப்படுத்துகிறது, மனநிலையை மேம்படுத்துகிறது மற்றும் எடையை நிர்வகிக்க உதவுகிறது.",
            "physical_tip2_title": "நெகிழ்வுத்தன்மை மற்றும் வலிமை",
            "physical_tip2_text": "தசையை உருவாக்கவும், மூட்டு ஆரோக்கியத்தை மேம்படுத்தவும் வாரத்திற்கு இரண்டு முறையாவது உங்கள் வழக்கத்தில் வலிமை பயிற்சி பயிற்சிகள் (எ.கா., எடைகள் அல்லது உடல் எடையைப் பயன்படுத்தி) மற்றும் நெகிழ்வுத்தன்மை பயிற்சிகள் (எ.கா., நீட்டுதல், யோகா) ஆகியவற்றை இணைக்கவும்.",
            "physical_tip3_title": "செயலில் உள்ள வாழ்க்கை முறை",
            "physical_tip3_text": "லிஃப்ட்டுக்குப் பதிலாக படிக்கட்டுகளைப் பயன்படுத்துதல், தொலைபேசி அழைப்புகளின் போது நடத்தல் அல்லது தொலைக்காட்சி பார்க்கும்போது லேசான நீட்டுதல் போன்ற நாள் முழுவதும் செயலில் இருக்க வழிகளைத் தேடுங்கள்.",

            "section_mental_wellness_title": "மன நல்வாழ்வு: உங்கள் மனதை வளர்ப்பது",
            "mental_tip1_title": "மன அழுத்த மேலாண்மை",
            "mental_tip1_text": "தியானம், ஆழ்ந்த சுவாசம் அல்லது பொழுதுபோக்குகள் போன்ற மன அழுத்தத்தைக் குறைக்கும் நடவடிக்கைகளைப் பயிற்சி செய்யுங்கள். நாள்பட்ட மன அழுத்தம் மன மற்றும் உடல் ஆரோக்கியம் இரண்டையும் எதிர்மறையாக பாதிக்கலாம்.",
            "mental_tip2_title": "தரமான தூக்கம்",
            "mental_tip2_text": "ஒரு இரவுக்கு 7-9 மணிநேர தரமான தூக்கத்தை நோக்கமாகக் கொள்ளுங்கள். ஒரு சீரான தூக்க அட்டவணையை நிறுவி, அறிவாற்றல் செயல்பாடு மற்றும் உணர்ச்சி ஒழுங்குமுறைக்கு இன்றியமையாத தூக்கத்தின் தரத்தை மேம்படுத்த ஒரு நிதானமான படுக்கை நேர வழக்கத்தை உருவாக்கவும்.",
            "mental_tip3_title": "சமூக தொடர்பு",
            "mental_tip3_text": "குடும்பம் மற்றும் நண்பர்களுடன் வலுவான சமூக பிணைப்புகளைப் பராமரிக்கவும். ஒரு ஆதரவான சமூக வலையமைப்பு தனிமை உணர்வுகளைக் குறைத்து, சொந்தம் என்ற உணர்வை வழங்க முடியும்.",
            
            "section_hygiene_title": "சுகாதாரம் மற்றும் நோய் தடுப்பு",
            "hygiene_tip1_title": "கைகளின் சுகாதாரம்",
            "hygiene_tip1_text": "குறிப்பாக சாப்பிடுவதற்கு முன் மற்றும் கழிப்பறையைப் பயன்படுத்திய பிறகு உங்கள் கைகளை சோப்பு மற்றும் தண்ணீரால் அடிக்கடி கழுவவும். இது நோய்த்தொற்றுகளின் பரவலைத் தடுக்க எளிய மற்றும் மிகவும் பயனுள்ள வழியாகும்.",
            "hygiene_tip2_title": "தடுப்பூசி",
            "hygiene_tip2_text": "பரிந்துரைக்கப்பட்ட தடுப்பூசிகளுடன் புதுப்பித்த நிலையில் இருங்கள். தடுப்பூசிகள் தொற்று நோய்களிலிருந்து உங்களையும் உங்கள் சமூகத்தையும் பாதுகாக்க ஒரு பாதுகாப்பான மற்றும் பயனுள்ள வழியாகும்.",
            "hygiene_tip3_title": "வழக்கமான பரிசோதனைகள்",
            "hygiene_tip3_text": "சுகாதார சிக்கல்களை முன்கூட்டியே கண்டறிந்து நிர்வகிப்பது நீண்ட மற்றும் ஆரோக்கியமான வாழ்க்கைக்கு முக்கியமானது.",

            "section_laws_title": "சுகாதார சட்டங்கள் மற்றும் பொது முன்முயற்சிகள்",
            "laws_intro": "பொது சுகாதாரம் ஒரு பகிரப்பட்ட பொறுப்பு. இந்திய அரசு குடிமக்களின் ஆரோக்கியத்தைப் பாதுகாக்க பல்வேறு சட்டங்கள் மற்றும் முன்முயற்சிகளை தொடர்ந்து செயல்படுத்தி வருகிறது. இந்த பக்கத்தில் உள்ள குறிப்புகளைப் பின்பற்றுவது இந்த தேசிய முயற்சிகளை ஆதரிப்பதில் ஒரு முக்கியமான படியாகும். உதாரணமாக, தனிப்பட்ட சுகாதாரத்தைப் பராமரிப்பது தொற்று நோய்களைத் தடுப்பதை நோக்கமாகக் கொண்ட பொது சுகாதார பிரச்சாரங்களின் வெற்றிக்கு நேரடியாக பங்களிக்கிறது.",
            "laws_point1": "தேசிய சுகாதாரக் கொள்கை அனைத்து குடிமக்களுக்கும் பொது சுகாதார தரநிலைகள் மற்றும் தரமான சுகாதார சேவையை மேம்படுத்துவதை நோக்கமாகக் கொண்டுள்ளது. உங்கள் முன்கூட்டிய சுகாதார நடவடிக்கைகள் அதன் இலக்குகளுடன் ஒத்துப்போகின்றன.",
            "laws_point2": "ஊட்டச்சத்து, உடல் செயல்பாடு மற்றும் மன ஆரோக்கியம் குறித்த பொது விழிப்புணர்வு பிரச்சாரங்கள் அரசு சுகாதார உத்திகளின் மையமாக உள்ளன. இந்த குறிப்புகளைப் பின்பற்றுவது அடிமட்ட மட்டத்திலிருந்து இந்த முயற்சிகளை பலப்படுத்த உதவுகிறது.",
            
            "disclaimer_title": "முக்கியமான மறுப்பு",
            "disclaimer_text": "இந்த தளத்தில் வழங்கப்பட்ட சுகாதார குறிப்புகள் தகவல் நோக்கங்களுக்காக மட்டுமே. அவை தொழில்முறை மருத்துவ ஆலோசனை, நோயறிதல் அல்லது சிகிச்சைக்கு மாற்றாக இல்லை. மருத்துவ நிலை குறித்து உங்களுக்கு ஏதேனும் கேள்விகள் இருந்தால் எப்போதும் உங்கள் மருத்துவர் அல்லது தகுதிவாய்ந்த சுகாதார வழங்குநரின் ஆலோசனையை நாடுங்கள்."
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

    # Nutrition Section
    st.subheader(f" {lang_data['section_nutrition_title']}")
    with st.expander(lang_data["nutrition_tip1_title"]):
        st.write(lang_data["nutrition_tip1_text"])
    with st.expander(lang_data["nutrition_tip2_title"]):
        st.write(lang_data["nutrition_tip2_text"])
    with st.expander(lang_data["nutrition_tip3_title"]):
        st.write(lang_data["nutrition_tip3_text"])

    st.markdown("---")
    
    # Physical Activity Section
    st.subheader(f" {lang_data['section_physical_activity_title']}")
    with st.expander(lang_data["physical_tip1_title"]):
        st.write(lang_data["physical_tip1_text"])
    with st.expander(lang_data["physical_tip2_title"]):
        st.write(lang_data["physical_tip2_text"])
    with st.expander(lang_data["physical_tip3_title"]):
        st.write(lang_data["physical_tip3_text"])

    st.markdown("---")
    
    # Mental Wellness Section
    st.subheader(f" {lang_data['section_mental_wellness_title']}")
    with st.expander(lang_data["mental_tip1_title"]):
        st.write(lang_data["mental_tip1_text"])
    with st.expander(lang_data["mental_tip2_title"]):
        st.write(lang_data["mental_tip2_text"])
    with st.expander(lang_data["mental_tip3_title"]):
        st.write(lang_data["mental_tip3_text"])

    st.markdown("---")

    # Hygiene Section
    st.subheader(f" {lang_data['section_hygiene_title']}")
    with st.expander(lang_data["hygiene_tip1_title"]):
        st.write(lang_data["hygiene_tip1_text"])
    with st.expander(lang_data["hygiene_tip2_title"]):
        st.write(lang_data["hygiene_tip2_text"])
    with st.expander(lang_data["hygiene_tip3_title"]):
        st.write(lang_data["hygiene_tip3_text"])

    st.markdown("---")

    # Health Laws and Public Initiatives Section
    st.subheader(f" {lang_data['section_laws_title']}")
    st.write(lang_data["laws_intro"])
    st.markdown(f"- {lang_data['laws_point1']}")
    st.markdown(f"- {lang_data['laws_point2']}")

    st.markdown("---")

    # Important Disclaimer
    st.subheader(lang_data["disclaimer_title"])
    st.warning(lang_data["disclaimer_text"])
