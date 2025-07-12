import streamlit as st

st.markdown("<h1 style='text-align: center;'>Job Application Copilot</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([3, 4])

with col1:
    with st.expander("📘 How to Use This Tool", expanded=False):
        st.markdown("""
        <div style='text-align: left;'>
            <p><strong>Step 1:</strong> Set your job preferences</p>
            <p><strong>Step 2:</strong> Paste a job description</p>
            <p><strong>Step 3:</strong> Upload Resume</p>
            <p><strong>Step 4:</strong> Click "GO" to assess Fit</p>
            <p><strong>Step 5:</strong> (Optional) Generate a tailored cover letter or resume</p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <h5 style='text-align: center; line-height: 1.1; margin-top: -0.5rem; margin-bottom: -0.2rem; font-size: 1.1rem;'>
            💰 Desired Minimum Salary
        </h5>
    """, unsafe_allow_html=True)
