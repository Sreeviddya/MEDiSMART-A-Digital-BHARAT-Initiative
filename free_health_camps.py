import streamlit as st
import pandas as pd

def show_page():
    """Generates the content for the free health camps page."""
    
    # Using a container to center the content and add padding
    with st.container():
        st.title(" Free Health Camps")
        st.caption("Updates on government and NGO-led free health checkup camps.")
        st.divider()

        # Data for the health camps
        camps_data = [
            {
                "title": "Medical Camp at Community Hall",
                "date": "25 September 2024",
                "time": "9:00 AM - 4:00 PM",
                "location": "Gandhi Nagar, Community Hall, New Delhi",
                "organizer": "Ministry of Health & Family Welfare",
                "services": "General Medical Checkup (Blood Pressure, Sugar Level), Eye & Dental Screening, Free Consultation with Specialist Doctors, Distribution of Essential Medicines"
            },
            {
                "title": "Child & Women Health Initiative",
                "date": "10 October 2024",
                "time": "10:00 AM - 5:00 PM",
                "location": "Primary Health Centre, Civil Lines, Mumbai",
                "organizer": "Save the Children NGO",
                "services": "Anemia and Malnutrition Screening, Pre-natal and Post-natal Care Consultation, Immunization and Vaccination for Children, Nutritional Counselling"
            },
            {
                "title": "Diabetes Awareness & Screening Camp",
                "date": "15 November 2024",
                "time": "11:00 AM - 3:00 PM",
                "location": "Sarojini Park, Kanpur",
                "organizer": "Health for All Foundation",
                "services": "Blood Sugar Level Testing, Consultation with Diabetologists, Diet and Lifestyle Advice, Information on Diabetes Management"
            },
            {
                "title": "Senior Citizen Health Checkup",
                "date": "05 October 2024",
                "time": "9:00 AM - 2:00 PM",
                "location": "Old Age Home, Anna Nagar, Chennai",
                "organizer": "HelpAge India",
                "services": "Geriatric Care Consultation, Arthritis and Joint Pain Screening, Physiotherapy Sessions, Medication Review"
            },
            {
                "title": "Cardiac Health Camp",
                "date": "20 October 2024",
                "time": "8:00 AM - 1:00 PM",
                "location": "City Auditorium, Bangalore",
                "organizer": "Indian Heart Association",
                "services": "ECG Screening, Blood Pressure Monitoring, Cholesterol Testing, Cardiology Consultation"
            },
            {
                "title": "Dental Care for All",
                "date": "02 November 2024",
                "time": "10:00 AM - 4:00 PM",
                "location": "Local School, Sector 15, Chandigarh",
                "organizer": "Smile Foundation",
                "services": "Oral Hygiene Education, Dental Cleaning, Cavity and Gum Disease Screening, Free Toothbrushes & Paste"
            },
            {
                "title": "Mental Wellness Workshop",
                "date": "28 October 2024",
                "time": "1:00 PM - 5:00 PM",
                "location": "Community Center, Vile Parle, Mumbai",
                "organizer": "Mindful Living NGO",
                "services": "Stress Management Counselling, Anxiety and Depression Screening, Mindfulness Sessions, Group Therapy"
            },
            {
                "title": "Blood Donation Drive",
                "date": "14 November 2024",
                "time": "9:00 AM - 5:00 PM",
                "location": "Railway Station, Hyderabad",
                "organizer": "Red Cross Society",
                "services": "Blood Donation, Hemoglobin Testing, Blood Grouping, Health Checkup"
            },
            {
                "title": "Nutrition and Diet Camp",
                "date": "01 December 2024",
                "time": "10:00 AM - 2:00 PM",
                "location": "Public Library, Pune",
                "organizer": "Healthy India Initiative",
                "services": "Nutritional Assessment, Diet Planning, Weight Management Guidance, Counselling for Healthy Eating"
            },
            {
                "title": "General Health Camp",
                "date": "20 November 2024",
                "time": "9:00 AM - 4:00 PM",
                "location": "Village Primary School, Jhansi",
                "organizer": "Rural Health Mission",
                "services": "Fever and Common Illness Checkup, Basic First Aid Training, Free Medicines, Hygiene Education"
            },
            {
                "title": "Cervical Cancer Screening",
                "date": "08 December 2024",
                "time": "9:00 AM - 1:00 PM",
                "location": "Women's Clinic, Gwalior",
                "organizer": "Indian Cancer Society",
                "services": "Pap Smear Test, Gynaecological Consultation, HPV Vaccination Awareness, General Women's Health Check"
            },
            {
                "title": "Asthma and Respiratory Camp",
                "date": "18 November 2024",
                "time": "10:00 AM - 3:00 PM",
                "location": "Government Hospital, Lucknow",
                "organizer": "Lung Care Foundation",
                "services": "Spirometry Test, Inhaler Technique Demonstration, Pulmonologist Consultation, Asthma Management Education"
            },
            {
                "title": "Pediatric Health Camp",
                "date": "25 November 2024",
                "time": "9:00 AM - 1:00 PM",
                "location": "Primary School, Jaipur",
                "organizer": "Child Welfare Committee",
                "services": "Growth Monitoring, Vision and Hearing Screening, Vaccination Schedule Review, Paediatrician Consultation"
            },
            {
                "title": "Spinal & Joint Health Camp",
                "date": "05 January 2025",
                "time": "10:00 AM - 4:00 PM",
                "location": "Sports Complex, Ludhiana",
                "organizer": "Orthopedic Association of India",
                "services": "Postural Assessment, Joint Mobility Check, Physiotherapy Advice, Consultation with Orthopedic Surgeons"
            },
            {
                "title": "Free Eye Checkup Camp",
                "date": "15 January 2025",
                "time": "9:00 AM - 5:00 PM",
                "location": "Market Area, Kolkata",
                "organizer": "Sightsavers India",
                "services": "Vision Testing, Cataract & Glaucoma Screening, Free Spectacles for Needy, Consultation with Ophthalmologists"
            },
            {
                "title": "Kidney Health Awareness",
                "date": "20 January 2025",
                "time": "10:00 AM - 2:00 PM",
                "location": "Community Center, Ahmedabad",
                "organizer": "Nephrology Forum",
                "services": "Urine & Blood Creatinine Testing, Blood Pressure Check, Diet Consultation for Kidney Health, Early Disease Detection"
            },
            {
                "title": "General Health & Hygiene Camp",
                "date": "28 December 2024",
                "time": "9:00 AM - 3:00 PM",
                "location": "Panchayat Bhawan, Rohtak",
                "organizer": "Government Health Services",
                "services": "General Body Checkup, Sanitation Education, Hand Washing Demonstrations, Distribution of Soap & Sanitizer"
            },
            {
                "title": "Skin & Hair Care Camp",
                "date": "03 February 2025",
                "time": "11:00 AM - 4:00 PM",
                "location": "Urban Clinic, Bhopal",
                "organizer": "Dermatology Society of India",
                "services": "Skin Condition Diagnosis, Hair Fall Consultation, Advice on Skin & Hair Care Routine, Free Product Samples"
            },
            {
                "title": "Liver Health & Screening Camp",
                "date": "10 February 2025",
                "time": "10:00 AM - 2:00 PM",
                "location": "Medical College, Visakhapatnam",
                "organizer": "Gastroenterology Association",
                "services": "Liver Function Test (LFT) Screening, Hepatitis B & C Awareness, Diet for Liver Health, Consultation with Gastroenterologists"
            },
            {
                "title": "Thyroid Health Camp",
                "date": "22 February 2025",
                "time": "9:00 AM - 1:00 PM",
                "location": "Endocrinology Center, Coimbatore",
                "organizer": "Endocrine Society of India",
                "services": "Thyroid Function Test (TFT) Screening, Consultation for Thyroid Disorders, Symptom Management Advice, General Health Checkup"
            },
            {
                "title": "Hearing & Speech Checkup",
                "date": "01 March 2025",
                "time": "10:00 AM - 3:00 PM",
                "location": "Rehabilitation Center, Ranchi",
                "organizer": "NGO for Differently-Abled",
                "services": "Hearing Test, Speech Therapy Consultation, Ear Care Education, Distribution of Hearing Aids (case-by-case)"
            },
            {
                "title": "Hypertension Screening Camp",
                "date": "15 March 2025",
                "time": "9:00 AM - 1:00 PM",
                "location": "District Hospital, Agartala",
                "organizer": "National Health Mission",
                "services": "Blood Pressure Measurement, Lifestyle Modification Advice, Risk Factor Assessment, Consultation with Doctors"
            },
            {
                "title": "Women's Health & Gynaecology Camp",
                "date": "08 March 2025",
                "time": "9:00 AM - 5:00 PM",
                "location": "Community Hall, Indore",
                "organizer": "Family Planning Association of India",
                "services": "General Gynaecology Checkup, PCOD/PCOS Screening, Family Planning Consultation, Breast Cancer Awareness"
            }
        ]
        
        # Convert to DataFrame for easier searching
        df = pd.DataFrame(camps_data)

        st.markdown(
            """
            This page provides the latest updates on free health camps organized by the government and various non-governmental organizations (NGOs) for the benefit of all citizens. Please check the details below for a camp near you and take advantage of these vital services.
            """
        )

        st.divider()

        # Search bar
        search_query = st.text_input("🔍 Search for a health camp...", placeholder="e.g., Eye, Mumbai, Blood Donation").strip().lower()

        # Filter the DataFrame based on the search query
        filtered_df = df[
            df.apply(lambda row: search_query in ' '.join(row.astype(str).values).lower(), axis=1)
        ]

        if not filtered_df.empty:
            # Display each health camp using st.expander, with expanded=True
            for _, camp in filtered_df.iterrows():
                with st.expander(f"**{camp['title']}** - *{camp['date']}*", expanded=True):
                    st.markdown(f"**Time:** {camp['time']}")
                    st.markdown(f"**Location:** {camp['location']}")
                    st.markdown(f"**Organizing Body:** {camp['organizer']}")
                    st.markdown(f"**Services Offered:** {camp['services']}")
        else:
            st.info("No health camps found matching your search. Please try a different keyword.")

# Call the function to display the page when the script is run
if __name__ == "__main__":
    show_page()
