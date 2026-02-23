import streamlit as st
from PIL import Image
import altair as alt

# Page configuration (must appear once and at top)
st.set_page_config(
    page_title="🎵 Song Popularity Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

from components.nav import render_nav
render_nav("Home")

st.markdown("""
<style>
.card {
    background: rgba(255, 255, 255, 0.04);
    border-radius: 16px;
    padding: 25px 30px;
    margin-bottom: 30px;
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(10px);
    transition: all 0.25s ease;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 30px rgba(255, 0, 200, 0.25);
}
</style>
""", unsafe_allow_html=True)

# Centered Title
st.markdown(
    "<h1 style='text-align: center;'>🎵 Song Popularity Prediction Dashboard</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center;'>An end-to-end Data Science project on music analytics</p>",
    unsafe_allow_html=True
)

st.write("")

# Banner image
try:
    image = Image.open("images/banner.png")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(image, use_container_width=True)

except Exception:
    st.warning("Banner image not found.")

# Author section
st.markdown("""
<div class="card">
<h3>👤 Author</h3>
<ul>
<li><strong>Name:</strong> Akash Ray</li>
<li><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/akashray1/" target="_blank">Akash Ray</a></li>
<li><strong>Project Goal:</strong> Showcase complete data science workflow from analysis to deployment.</li>
</ul>
</div>
""", unsafe_allow_html=True)

# Problem Statement
st.markdown("""
<div class="card">
<h3>🧩 Problem Statement</h3>
<p>
As a data scientist at a music streaming company, your task is to analyze the key 
<strong>musical</strong> and <strong>platform-related</strong> features that influence a song’s popularity in 2023.
</p>

<ul>
<li>Predict popularity using <strong>audio</strong> and <strong>platform</strong> attributes.</li>
<li>Provide insights to <strong>Marketing</strong> and <strong>A&amp;R teams</strong>.</li>
<li>Support playlist curation and artist scouting decisions.</li>
</ul>
</div>
""", unsafe_allow_html=True)

# Workflow
st.markdown("""
<div class="card">
<h3>🔍 Project Workflow</h3>
<ol>
<li><strong>Understanding the Dataset</strong></li>
<li><strong>EDA (Exploratory Data Analysis)</strong></li>
<li><strong>Model Building</strong></li>
<li><strong>Evaluation</strong></li>
<li><strong>Deployment</strong></li>
</ol>
</div>
""", unsafe_allow_html=True)

st.success("Use the navigation bar above to explore insights, model training, predictions, and final takeaways.")
