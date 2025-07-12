import streamlit as st

st.markdown("<h1 style='text-align: center;'>Job Application Copilot</h1>", unsafe_allow_html=True)

# start a single flex row for all three widgets
st.markdown(
    "<div style='display:flex; align-items:baseline; gap:1rem; width:100%;'>",
    unsafe_allow_html=True
)

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

st.markdown(
    "<h3 style='margin:0; font-size:1.25rem;'>💰 Desired Salary</h3>",
    unsafe_allow_html=True
)

salary = st.text_input(
    "",
    placeholder="E.g., $95,000",
    label_visibility="collapsed"
)

# close the flex row
st.markdown("</div>", unsafe_allow_html=True)
