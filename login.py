import streamlit as st
import random

# --- Demo User Configuration ---
DEMO_USERNAME = "ViddyaKS"
DEMO_PASSWORD = "Viddya@5"
DEMO_MOBILE = "9063209584"

def show_page():
    st.title("User Login")
    st.markdown("Login to your E-Hospital account. Demo user credentials are provided below for easy access.")
    st.info(f"**Demo User:**\n- Username: `{DEMO_USERNAME}`\n- Password: `{DEMO_PASSWORD}`\n- Mobile: `{DEMO_MOBILE}`")

    # --- Initialize session state for login steps ---
    if "login_step" not in st.session_state:
        st.session_state.login_step = "form"
    if "login_otp" not in st.session_state:
        st.session_state.login_otp = None
    if "login_method" not in st.session_state:
        st.session_state.login_method = "Username/Password"
    if "user_is_logged_in" not in st.session_state:
        st.session_state.user_is_logged_in = False
    if "otp_verified" not in st.session_state:
        st.session_state.otp_verified = False
    if "username" not in st.session_state:
        st.session_state.username = None


    # --- Login Method Selection ---
    st.session_state.login_method = st.radio(
        "Choose Login Method:",
        ("Username/Password", "Mobile Number"),
        key="login_method_radio"
    )

    # --- Login Form Step ---
    if st.session_state.login_step == "form":
        if st.session_state.login_method == "Username/Password":
            with st.form("login_form_username"):
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                
                submit_button = st.form_submit_button("Login")

            if submit_button:
                if username == DEMO_USERNAME and password == DEMO_PASSWORD:
                    st.session_state.login_step = "verify_otp"
                    st.session_state.login_otp = random.randint(1000, 9999)
                    st.session_state.username = username # Save the username
                    st.success("Please check your mobile. A 4-digit OTP has been sent.")
                    st.rerun()
                else:
                    st.error("Invalid username or password. Please try again.")

        elif st.session_state.login_method == "Mobile Number":
            with st.form("login_form_mobile"):
                mobile = st.text_input("Mobile Number", max_chars=10)
                
                submit_button = st.form_submit_button("Login")

            if submit_button:
                if mobile == DEMO_MOBILE:
                    st.session_state.login_step = "verify_otp"
                    st.session_state.login_otp = random.randint(1000, 9999)
                    # For this demo, we'll use a placeholder username for mobile login
                    st.session_state.username = "MobileUser" 
                    st.success("Please check your mobile. A 4-digit OTP has been sent.")
                    st.rerun()
                else:
                    st.error("Invalid mobile number. Please try again.")

    # --- OTP Verification Step ---
    elif st.session_state.login_step == "verify_otp":
        st.subheader("Verify Your Mobile Number")
        st.info(f"An OTP has been sent to your mobile number: **{DEMO_MOBILE}**")
        st.markdown(f"**For demo purposes, your OTP is:** `{st.session_state.login_otp}`")

        entered_otp = st.text_input("Enter the OTP", max_chars=4)
        
        if st.button("Verify OTP"):
            if entered_otp == str(st.session_state.login_otp):
                st.session_state.otp_verified = True
                st.success("OTP verified successfully!")
            else:
                st.session_state.otp_verified = False
                st.error("Incorrect OTP. Please try again.")
        
        # This button is only shown AFTER a successful OTP verification
        if st.session_state.otp_verified:
            if st.button("Go to Personal Dashboard"):
                st.session_state.user_is_logged_in = True
                st.session_state.current_page = "personal_dashboard"
                st.rerun()