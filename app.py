import streamlit as st

st.set_page_config(
    page_title="🎵 Song Popularity Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Redirect to Home page
st.switch_page("pages/0_Home.py")
