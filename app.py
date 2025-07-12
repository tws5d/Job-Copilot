import streamlit as st

st.markdown("<h1 style='text-align: center;'>Job Application Copilot</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([3, 4])  # equal column size

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
    st.markdown("<h4 style='text-align: center;'>💰 Desired Minimum Salary</h4>", unsafe_allow_html=True)
    
    # Hide default slider value labels using CSS
    st.markdown("""
        <style>
        div[data-testid="stSlider"] > label + div div:nth-of-type(2) {
            display: none;
        }
        </style>
    """, unsafe_allow_html=True)


    salary = st.slider(
        label="",
        min_value=0,
        max_value=500000,
        step=5000,
        value=250000,
        label_visibility="collapsed"
    )

    # Custom labels under the slider
    st.markdown(f"""
    <div style='display: flex; justify-content: space-between; padding: 0 8px;'>
        <span style='color: #aaa;'>$0</span>
        <span style='color: red; font-weight: bold;'>${salary:,.0f}</span>
        <span style='color: #aaa;'>$500K+</span>
    </div>
    """, unsafe_allow_html=True)

    

