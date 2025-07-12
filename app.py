import streamlit as st

st.markdown("<h1 style='text-align: center;'>Job Application Copilot</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([3, 4])

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
    # keep the 2:1 split
    sub1, sub2 = st.columns([2, 1])

    # tighten up the right- and bottom-margins here
    sub1.markdown(
        "<h3 style='text-align:left; margin:0 0.2rem -1rem 0; font-size:1.25rem;'>💰 Desired Salary</h3>",
        unsafe_allow_html=True
    )

    # wrap the text_input in a custom container
    sub2.markdown('<div class="salary-input-wrapper">', unsafe_allow_html=True)

    # empty label, placeholder text
    salary = sub2.text_input("", placeholder="E.g., $95,000")

    # close the wrapper and inject scoped CSS to lift it via transform
    sub2.markdown("""
    </div>
    <style>
    .salary-input-wrapper {
        transform: translateY(-0.5rem) !important;
    }
    </style>
    """, unsafe_allow_html=True)


