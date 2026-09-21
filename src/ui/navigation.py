import streamlit as st

def create_tabs():
    return st.tabs([
        "📊 Overview",
        "🚚 Route Analysis",
        "💰 Sales Analysis",
        "📦 Product Analysis",
        "📄 Data Explorer"
    ])