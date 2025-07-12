import streamlit as st

st.markdown("<h1 style='text-align: center;'>Job Application Copilot</h1>", unsafe_allow_html=True)

# THE FIX: This CSS targets a stable Streamlit attribute to control the gap.
st.markdown("""
    <style>
        [data-testid="stHorizontalBlock"] {
            gap: 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)


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
    st.markdown(
        "<div style='text-align: right; margin-top: 0.5rem;'>💰 Desired Salary</div>",
        unsafe_allow_html=True
    )

with col3:
    salary = st.text_input(
        "",
        placeholder="E.g., $95,000",
        label_visibility="collapsed"
    )
