import streamlit as st
from PIL import Image
import altair as alt

# Page configuration (must appear once and at top)
st.set_page_config(
    page_title="🎵 Song Popularity Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

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
st.markdown("---")
st.markdown("### 👤 Author")
st.markdown("""
- **Name:** Akash Ray  
- **LinkedIn:** [Akash Ray](https://www.linkedin.com/in/akashray1/)  
- **Project Goal:** Showcase complete data science workflow from analysis to deployment.
""")

# Problem Statement
st.markdown("---")
st.markdown("### 🧩 Problem Statement")
st.markdown("""
As a data scientist at a music streaming company, your task is to analyze the key **musical** and **platform-related** features that influence a song’s popularity in 2023.

We aim to:
- Predict the popularity of a song based on its **audio** and **platform** attributes.
- Provide **actionable insights** to the **Marketing** and **A&R teams**.
- Help with playlist curation, cross-platform promotion, and artist scouting decisions.
""")

# Workflow
st.markdown("---")
st.markdown("### 🔍 Project Workflow")
st.markdown("""
1. **Understanding the Dataset**
2. **EDA (Exploratory Data Analysis)**
3. **Model Building**
4. **Evaluation**
5. **Deployment**
""")

st.markdown("---")
st.success("Use the sidebar to navigate through insights, model training, predictions, and final takeaways.")
