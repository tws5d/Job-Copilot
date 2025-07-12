import streamlit as st

st.markdown("<h1 style='text-align: center;'>Job Application Copilot</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])  # equal column size

with col1:
    with st.expander("📘 How to Use This Tool", expanded=False):
        st.markdown("""
        <div style='text-align: left;'>
            <p><strong>Step 1:</strong> Set your job preferences below</p>
            <p><strong>Step 2:</strong> Paste a job description</p>
            <p><strong>Step 3:</strong> Upload Resume</p>
            <p><strong>Step 4:</strong> Click GO to see your Fit Score</p>
            <p><strong>Step 5:</strong> Review feedback</p>
            <p><strong>Step 6:</strong> (Optional) Generate a tailored cover letter or resume</p>
        </div>
        """, unsafe_allow_html=True)


