import streamlit as st

def open_chart_card(title, subtitle=""):
    st.markdown(
        f"""
        <div class="chart-card">
            <div class="chart-title">{title}</div>
            <div class="chart-subtitle">{subtitle}</div>
        """,
        unsafe_allow_html=True
    )

def close_chart_card():
    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )