import streamlit as st
import random

def go_to_login_page():
    # The button click already triggers a rerun, so we only need to set the state.
    st.session_state.current_page = "login"

def show_page():
    st.title("New User Registration")
    st.markdown("Register to create your E-Hospital account and a unique Digital Health ID.")
    st.info("All data is collected as per the Digital Personal Data Protection Act, 2023. We will only collect data that is absolutely necessary for providing services.")

    if "reg_step" not in st.session_state:
        st.session_state.reg_step = "form"
    if "generated_otp" not in st.session_state:
        st.session_state.generated_otp = None
    if "reg_mobile" not in st.session_state:
        st.session_state.reg_mobile = ""

    if st.session_state.reg_step == "form":
        with st.form("registration_form"):
            st.subheader("Personal Information")
            
            col1, col2 = st.columns(2)
            with col1:
                st.session_state.reg_full_name = st.text_input("Full Name (as per ID proof)")
                st.session_state.reg_dob = st.date_input("Date of Birth")
                st.session_state.reg_gender = st.selectbox("Gender", ["Male", "Female", "Other"])
                st.session_state.reg_email = st.text_input("Email (Optional)")

            with col2:
                st.session_state.aadhaar_no = st.text_input("Aadhaar Number (Optional, but recommended for ABHA creation)", max_chars=12)
                st.markdown("<small>Your Aadhaar will be used for a secure, one-time e-KYC. We do not store your Aadhaar number.</small>", unsafe_allow_html=True)
                
                st.session_state.reg_mobile = st.text_input("Mobile Number (for OTP verification)")
                st.session_state.reg_username = st.text_input("Choose a Username")
                st.session_state.reg_password = st.text_input("Choose a Password", type="password")
                st.session_state.reg_confirm_password = st.text_input("Confirm Password", type="password")
            
            st.markdown("---")
            st.subheader("Consent & Terms")
            st.session_state.consent1 = st.checkbox("I consent to the collection and processing of my personal data as per the [E-Hospital Privacy Policy](link_to_your_policy).")
            st.session_state.consent2 = st.checkbox("I agree to the [Terms & Conditions](link_to_your_terms).")

            submit_button = st.form_submit_button("Register Account")

        if submit_button:
            if not (st.session_state.reg_full_name and st.session_state.reg_mobile and st.session_state.reg_username and st.session_state.reg_password):
                st.error("Please fill in all mandatory fields.")
            elif st.session_state.reg_password != st.session_state.reg_confirm_password:
                st.error("Passwords do not match.")
            elif not (st.session_state.consent1 and st.session_state.consent2):
                st.error("You must agree to the Privacy Policy and Terms & Conditions to proceed.")
            else:
                st.session_state.reg_step = "verify_otp"
                st.session_state.generated_otp = random.randint(100000, 999999)
                st.success("Please check your mobile. A 6-digit OTP has been sent to complete your registration.")
                st.rerun()

    if st.session_state.reg_step == "verify_otp":
        st.subheader("Verify Your Mobile Number")
        st.info(f"An OTP has been sent to your mobile number: **{st.session_state.reg_mobile}**")
        st.markdown(f"**For demo purposes, your OTP is:** `{st.session_state.generated_otp}`")
        
        entered_otp = st.text_input("Enter the OTP", max_chars=6)
        
        if st.button("Verify OTP"):
            if entered_otp == str(st.session_state.generated_otp):
                st.success("OTP verified successfully! Your account has been created.")
                st.balloons()
                st.session_state.reg_step = "done"
                st.rerun()
            else:
                st.error("Incorrect OTP. Please try again.")

    if st.session_state.reg_step == "done":
        st.success("Your E-Hospital account has been successfully created!")
        st.subheader("Login to your new account")
        st.button("Go to Login Page", on_click=go_to_login_page)
