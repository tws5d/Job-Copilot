import streamlit as st
import plotly.graph_objects as go

st.markdown("<h1 style='text-align: center;'>Job Application Copilot</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

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

    st.markdown("<div style='text-align: center; font-size: 25px; font-weight: bold;'>Job Fit: 🟡 Moderate</div>", unsafe_allow_html=True) # placeholder fit logic
    
    # Placeholder radar chart
    categories = ['Skills', 'Experience', 'Culture', 'Location', 'Salary']
    values = [3, 4, 2, 5, 3]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Fit Score',
        mode='lines',
        text=[]
    ))
    fig.update_layout(
        width=350,
        height=350,
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 5]),
        ),
        margin=dict(l=60, r=80, t=0, b=40),
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)
    
with col2:
    salary = st.text_input(
        "",
        placeholder="💰 Desired Salary (E.g., $95,000)",
        label_visibility="collapsed"
    )
    st.markdown("<div style='text-align: center; font-weight: bold; margin-top: -10px;'>Preferred Work Setup</div>", unsafe_allow_html=True)

    location_pref = st.multiselect(
        label="",
        options=["Remote", "Hybrid", "On Site"]
    )


