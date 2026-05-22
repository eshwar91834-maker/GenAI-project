import streamlit as st
from jd_rewrited import rewrite_jd

st.set_page_config(page_title="JD Rewriter", page_icon=":memo:", layout="centered")

st.title("JD Rewriter")
st.write("Rewrite jargon-heavy job descriptions into concise and detailed versions.")

job_description = st.text_area("Enter the job description to rewrite:", height=200)

temperature = st.slider("Temperature:", min_value=0.0, max_value=1.0, value=0.2, step=0.1)

if st.button("Rewrite JD"):
    if not job_description.strip():
        st.warning("Please enter a job description to rewrite.")
    else:
        with st.spinner("Rewriting the job description..."):
            try:
                result = rewrite_jd(job_description, temperature)
                st.subheader("Concise Version")
                st.write(result.concise_version)
                st.subheader("Detailed Version")
                st.write(result.detailed_version)
            except Exception as e:
                st.error(f"An error occurred: {e}")