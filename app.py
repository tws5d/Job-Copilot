import streamlit as st

# It's good practice to set the page config first.
st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center;'>Job Application Copilot</h1>", unsafe_allow_html=True)

# --- Column Layout ---
# The list [3, 4] creates two columns where the second column is 4/3 (~1.33x)
# wider than the first. To make them equal, you would use st.columns(2).
col1, col2 = st.columns([3, 4])

with col1:
    # The expander is a great way to tuck away instructions!
    with st.expander("📘 How to Use This Tool", expanded=False):
        st.markdown("""
            **Step 1:** Set your job preferences
            **Step 2:** Paste a job description
            **Step 3:** Upload Resume
            **Step 4:** Click "GO" to assess Fit
            **Step 5:** (Optional) Generate a tailored cover letter or resume
        """) # No need for the div or <p> tags, markdown handles this.

with col2:
    # --- Simplified Input Widget ---
    # It's better to use the widget's built-in label for titles.
    # This avoids complex HTML/CSS and ensures proper alignment.
    # st.number_input is also more suitable for salary than text_input.
    salary_input = st.number_input(
        label="💰 Desired Minimum Salary",
        min_value=0,
        placeholder="e.g., 125000",
        step=1000,
        format="%d" # Use %d for a clean integer display
    )

st.write(f"Salary input: ${salary_input:,}") # Example of how to display the input
