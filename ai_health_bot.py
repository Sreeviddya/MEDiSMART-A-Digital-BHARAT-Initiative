import streamlit as st
import requests
import json
import time

def show_page():
    """
    Renders the complete Streamlit medical chatbot application inside a single function.
    This structure is useful for multi-page applications.
    """
    class WorkingMedicalChatbot:
        """
        A class to handle the logic for a medical chatbot, with a fallback
        to a built-in knowledge base if an API token is not provided or
        the API call fails.
        """
        def __init__(self):
            # List of medical models to try (in order of preference)
            self.medical_models = [
                "microsoft/DialoGPT-medium",
                "facebook/blenderbot-400M-distill",
                "microsoft/DialoGPT-small",
            ]
            self.current_model_index = 0
            
            # Medical knowledge base as fallback
            self.medical_kb = {
                "fever": {
                    "symptoms": "Body temperature above 100.4°F (38°C), chills, sweating, headache, muscle aches",
                    "causes": "Viral infections (flu, cold), bacterial infections, immune reactions, medications",
                    "advice": "Rest, stay hydrated, take fever reducers (acetaminophen/ibuprofen). Seek medical care if fever >103°F or persists >3 days",
                    "warning": "Seek immediate care for fever with difficulty breathing, chest pain, severe headache, or confusion"
                },
                "cold": {
                    "symptoms": "Runny nose, congestion, sneezing, mild cough, sore throat, low-grade fever",
                    "causes": "Viral infections (rhinovirus, coronavirus, etc.), weakened immune system",
                    "advice": "Rest, fluids, warm salt water gargling, humidifier use. Symptoms typically resolve in 7-10 days",
                    "warning": "See doctor if symptoms worsen after 10 days or include high fever, severe headache, or difficulty breathing"
                },
                "headache": {
                    "symptoms": "Head pain, pressure, throbbing, sensitivity to light/sound",
                    "causes": "Tension, stress, dehydration, eye strain, migraines, sinus issues",
                    "advice": "Rest in dark room, stay hydrated, apply cold/warm compress, over-the-counter pain relievers",
                    "warning": "Seek emergency care for sudden severe headache, headache with fever/stiff neck, or vision changes"
                },
                "cough": {
                    "symptoms": "Persistent coughing, may be dry or with phlegm, throat irritation",
                    "causes": "Viral infections, allergies, asthma, acid reflux, environmental irritants",
                    "advice": "Stay hydrated, use honey for throat soothing, avoid irritants, consider cough drops",
                    "warning": "See doctor for cough lasting >3 weeks, blood in cough, or difficulty breathing"
                }
            }
        
        def get_hf_token(self):
            """Get Hugging Face token from user input"""
            if 'hf_token' not in st.session_state:
                st.session_state.hf_token = ""
            
            token = st.text_input(
                "🔑 Enter your Hugging Face API Token (Optional):",
                value=st.session_state.hf_token,
                type="password",
                help="Get free token from: https://huggingface.co/settings/tokens. Leave empty to use offline responses.",
                key="hf_token_input"
            )
            
            if token:
                st.session_state.hf_token = token
            return token
        
        def extract_symptoms(self, text):
            """Extract symptoms from user input"""
            text_lower = text.lower()
            found_symptoms = []
            
            # Check for exact matches and common variations
            symptom_keywords = {
                "fever": ["fever", "temperature", "hot", "chills"],
                "cold": ["cold", "runny nose", "congestion", "sneezing"],
                "headache": ["headache", "head pain", "migraine", "head ache"],
                "cough": ["cough", "coughing", "throat", "phlegm"]
            }
            
            for symptom, keywords in symptom_keywords.items():
                if any(keyword in text_lower for keyword in keywords):
                    found_symptoms.append(symptom)
            
            return found_symptoms
        
        def generate_offline_response(self, user_input):
            """Generate medical response using built-in knowledge base"""
            symptoms = self.extract_symptoms(user_input)
            
            if not symptoms:
                return self.get_general_medical_response()
            
            response = "Based on the symptoms you've described, here's what I can tell you:\n\n"
            
            for symptom in symptoms[:2]:  # Limit to 2 symptoms for clarity
                if symptom in self.medical_kb:
                    info = self.medical_kb[symptom]
                    response += f"**{symptom.title()}:**\n"
                    response += f"• **Common symptoms:** {info['symptoms']}\n"
                    response += f"• **Possible causes:** {info['causes']}\n"
                    response += f"• **General advice:** {info['advice']}\n"
                    response += f"• **⚠️ Seek medical care:** {info['warning']}\n\n"
            
            response += self.get_medical_disclaimer()
            return response
        
        def get_general_medical_response(self):
            """Provide general medical guidance"""
            response = "I'd be happy to help with medical information. Could you describe your specific symptoms? "
            response += "I can provide guidance on common conditions like:\n\n"
            response += "• **Fever** - High temperature, chills, body aches\n"
            response += "• **Cold symptoms** - Runny nose, congestion, sneezing\n"
            response += "• **Headaches** - Head pain, pressure, migraines\n"
            response += "• **Cough** - Persistent coughing, throat irritation\n\n"
            response += "Please describe what you're experiencing, and I'll provide relevant information.\n\n"
            response += self.get_medical_disclaimer()
            return response
        
        def get_medical_disclaimer(self):
            """Standard medical disclaimer"""
            return ("⚠️ **Important Medical Disclaimer:** This information is for educational purposes only and "
                          "should not replace professional medical advice. Always consult with a qualified healthcare "
                          "provider for proper diagnosis and treatment, especially for serious or persistent symptoms.")
        
        def try_api_call(self, user_input, token):
            """Try to get response from Hugging Face API"""
            if not token or not token.startswith('hf_'):
                return None
            
            model_name = self.medical_models[self.current_model_index]
            api_url = f"https://api-inference.huggingface.co/models/{model_name}"
            
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }
            
            # Create a medical-focused prompt
            prompt = f"Patient asks: {user_input}\n\nMedical advice:"
            
            payload = {
                "inputs": prompt,
                "parameters": {
                    "max_new_tokens": 150,
                    "temperature": 0.7,
                    "return_full_text": False
                }
            }
            
            try:
                response = requests.post(api_url, headers=headers, json=payload, timeout=20)
                
                if response.status_code == 200:
                    result = response.json()
                    if isinstance(result, list) and len(result) > 0:
                        generated_text = result[0].get('generated_text', '').strip()
                        if generated_text and len(generated_text) > 20:
                            return generated_text + "\n\n" + self.get_medical_disclaimer()
                
                elif response.status_code == 503:
                    # Model loading, try next model
                    self.current_model_index = (self.current_model_index + 1) % len(self.medical_models)
                    return None
                
            except Exception as e:
                st.warning(f"API call failed: {str(e)}")
            
            return None
        
        def generate_response(self, user_input):
            """Generate medical response with fallback options"""
            token = st.session_state.get('hf_token', '')
            
            # Try API if token is provided
            if token:
                with st.spinner(f"🔍 Trying AI model: {self.medical_models[self.current_model_index]}"):
                    api_response = self.try_api_call(user_input, token)
                    if api_response:
                        return f"**🤖 AI Response:**\n{api_response}"
                    else:
                        st.info("API unavailable, using built-in medical knowledge...")
            
            # Fallback to offline knowledge base
            return f"**🩺 Medical Information:**\n{self.generate_offline_response(user_input)}"

    # --- Start of the Streamlit App UI ---
    st.title("🩺 Medical Assistant Chatbot")
    st.markdown("*Get medical information through AI or built-in medical knowledge*")
    
    # Initialize chatbot
    if 'working_chatbot' not in st.session_state:
        st.session_state.working_chatbot = WorkingMedicalChatbot()
    
    # Get token (optional)
    token = st.session_state.working_chatbot.get_hf_token()
    
    # Show status
    if token and token.startswith('hf_'):
        st.success("✅ API token configured - will try AI models first")
    else:
        st.info("💡 No API token - using built-in medical knowledge (works offline)")
    
    # Initialize chat history
    if 'working_chat_history' not in st.session_state:
        st.session_state.working_chat_history = []
    
    # Chat interface
    st.markdown("---")
    col1, col2 = st.columns([4, 1])
    
    with col1:
        user_input_key = "working_input"
        user_input = st.text_input(
            "💬 Describe your symptoms or medical question:",
            placeholder="e.g., I have fever and cold symptoms",
            key=user_input_key
        )
    
    with col2:
        send_button = st.button("Send 🚀", key="working_send")
    
    if send_button and user_input.strip():
        # Add user message
        st.session_state.working_chat_history.append({
            "role": "user",
            "content": user_input
        })
        
        # Generate response
        response = st.session_state.working_chatbot.generate_response(user_input)
        
        # Add bot response
        st.session_state.working_chat_history.append({
            "role": "assistant",
            "content": response
        })
        
        st.rerun()
    
    # Display chat history
    if st.session_state.working_chat_history:
        st.markdown("---")
        st.subheader("💬 Consultation History")
        
        for message in st.session_state.working_chat_history[-6:]:  # Last 6 messages
            if message["role"] == "user":
                st.markdown(f"**👤 You:** {message['content']}")
            else:
                st.markdown(message['content'])
            st.markdown("---")
    
    # Quick symptom buttons
    st.subheader("🔍 Quick Symptom Check")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("🤒 Fever"):
            st.session_state[user_input_key] = "I have a fever"
    
    with col2:
        if st.button("🤧 Cold"):
            st.session_state[user_input_key] = "I have cold symptoms"
    
    with col3:
        if st.button("🤕 Headache"):
            st.session_state[user_input_key] = "I have a headache"
    
    with col4:
        if st.button("😷 Cough"):
            st.session_state[user_input_key] = "I have a persistent cough"
    
    # Clear chat
    if st.button("🗑️ Clear Chat"):
        st.session_state.working_chat_history = []
        st.rerun()

if __name__ == "__main__":
    show_page()
