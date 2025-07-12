import streamlit as st

st.markdown("<h1 style='text-align: center;'>Job Application Copilot</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([3, 2, 1])

with col1:
    with st.expander("🤖 How to Use This Tool", expanded=False):
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
    # THE FIX: Use a <p> tag with a font-size to match the other widgets.
    # The margin-bottom helps align it with the text inside the input box.
    st.markdown(
        """
        <p style='font-size: 1rem; text-align: right; margin-bottom: 0.65rem;'>
            💰 Desired Salary
        </p>
        """,
        unsafe_allow_html=True
    )

with col3:
    # This is the completed text_input call.
    salary = st.text_input(
        "",
        placeholder="E.g., $95,000",
        label_visibility="collapsed"
    )
