import streamlit as st

def kpi_card(icon, title, value):
    st.markdown(
        f"""
        <div class="kpi">
            <div class="kpi-title">{icon} {title}</div>
            <div class="kpi-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )