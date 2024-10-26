import streamlit as st
from chains import HealthcareChain
from PIL import Image
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the HealthcareChain class
healthcare_chain = HealthcareChain()

# Set up the Streamlit app
st.title("Multimodal Healthcare Expert")

# Input for patient's medical history
st.subheader("Patient's Medical History")
patient_history = st.text_area(
    "Enter the patient's history (symptoms, previous diagnoses, etc.):",
    help="Provide a detailed medical history for accurate analysis."
)

# File uploader for medical image input (e.g., X-ray, MRI)
st.subheader("Upload Medical Image")
uploaded_file = st.file_uploader("Choose a medical image (e.g., X-ray, MRI)", type=["jpg", "jpeg", "png", "bmp"])

# Action button to process the input
if st.button("Analyze Case"):

    if patient_history:
        # Open the image
        patient_image = None
        if uploaded_file:
            patient_image = Image.open(uploaded_file)
        
            # Display the uploaded image
            st.image(patient_image, caption="Uploaded Medical Image", use_column_width=True)
        
        # Invoke the model with patient's history and image
        try:
            result = healthcare_chain.analyze_patient_case(patient_history, patient_image)
            
            # Display the result
            st.subheader("Diagnosis")
            st.json(result)  # Render the JSON response for clear readability
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please provide both patient history and a medical image for analysis.")
