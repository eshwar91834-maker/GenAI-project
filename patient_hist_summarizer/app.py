#Frontend using streamlit
import streamlit as st
import os
from utils import extract_text_from_pdf
from summarizer import summarize_case_sheet
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Patient History Summarizer", page_icon="🩺")
st.title("Patient History Summarizer")

uploaded_file = st.file_uploader("Upload a patient case sheet (PDF)", type=["pdf"])

if uploaded_file:

    os.makedirs("uploads", exist_ok=True)
    file_path = os.path.join("uploads", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    extracted_text = extract_text_from_pdf(file_path)

    st.subheader("Extracted Case Sheet Preview")

    st.text_area("Preview",extracted_text[:3000], height=300)

    if st.button("Summarize Case Sheet"):

        with st.spinner("Summarizing..."):
            api_key = os.getenv("OPENAI_API_KEY")
            summary = summarize_case_sheet(extracted_text, api_key)

            st.subheader("### Patient Overview")
            st.write(summary.patient_overview)
            st.subheader("### Chief Complaint")
            st.write(summary.chief_complaints)

            st.subheader("### Diagnosis")
            st.write(summary.diagnosis)

            st.subheader("### Medications")
            st.write(summary.medications)

            st.subheader("### Lab Findings")
            st.write(summary.lab_findings)

            st.subheader("### Treatment Given")
            st.write(summary.treatment_given)

            st.subheader("### Risks & Alerts")
            st.write(summary.risks_alerts)

            st.subheader("### Timeline")
            for event in summary.timeline:
                st.write(f"{event.date}: {event.event}")

            st.subheader("### Doctor Handoff Summary")
            st.write(summary.doctor_handoff_summary)

