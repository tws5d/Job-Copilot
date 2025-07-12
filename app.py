import streamlit as st

st.markdown("<h1 style='text-align: center;'>Job Application Copilot</h1>", unsafe_allow_html=True)

with st.expander("📘 How to Use This Tool", expanded=False):
    st.markdown("""
    <div style='text-align: center;'>
    **Step 1:** Set your job preferences below  \n
    **Step 2:** Paste a job description  \n
    **Step 3:** Upload Resume  \n
    **Step 4:** Click GO to see your Fit Score  \n
    **Step 5:** Review feedback  \n
    **Step 6:** (Optional) Generate a tailored cover letter or resume
    </div>
    """, unsafe_allow_html=True)
