import streamlit as st

from components.nav import render_nav
render_nav("Project Summary")

st.set_page_config(page_title="Project Summary", layout="wide")

# ============================================================================
# CUSTOM CSS STYLING
# ============================================================================
st.markdown("""
<style>
    /* Main title styling */
    h1 {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.8em;
        font-weight: 800;
        margin-bottom: 2rem;
    }

    /* Section header styling */
    h2 {
        color: #667eea;
        font-size: 1.8em;
        font-weight: 700;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 3px solid;
        border-image: linear-gradient(90deg, #667eea 0%, #764ba2 100%) 1;
        padding-bottom: 0.8rem;
    }

    /* Subsection headers */
    h3 {
        color: #764ba2;
        font-size: 1.2em;
        font-weight: 600;
        margin-top: 1.2rem;
        margin-bottom: 0.8rem;
    }

    /* List item styling */
    li {
        color: #e0e0e0;
        line-height: 1.8;
        font-size: 0.95rem;
        margin-bottom: 0.6rem;
    }

    /* Intro text styling */
    .intro-text {
        color: #b0b0b0;
        font-size: 0.95rem;
        line-height: 1.6;
        font-style: italic;
        margin-bottom: 1.5rem;
    }

    /* Highlight styling */
    .highlight {
        background: linear-gradient(120deg, rgba(102, 126, 234, 0.25), rgba(118, 75, 162, 0.25));
        padding: 0.2em 0.6em;
        border-radius: 4px;
        color: #a8d5ff;
        font-weight: 600;
    }

    /* Conclusion box */
    .conclusion-box {
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.12) 0%, rgba(102, 126, 234, 0.12) 100%);
        border-left: 4px solid #00d4ff;
        border-radius: 10px;
        padding: 2rem;
        margin: 2.5rem 0;
    }

    .conclusion-box h3 {
        margin-top: 0;
        color: #00d4ff;
    }

    /* Divider */
    hr {
        border: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.5), transparent);
        margin: 2.5rem 0;
    }

    /* Body text */
    p {
        color: #e0e0e0;
        line-height: 1.8;
        font-size: 0.95rem;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# PAGE CONTENT
# ============================================================================

st.title("Project Summary")

# Problem Statement Section
st.markdown("## 🎯 Problem Statement")
st.markdown('<p class="intro-text">Understanding what drives song popularity in the streaming era</p>', unsafe_allow_html=True)

st.markdown("""
The goal of this project was to analyze and predict the <span class="highlight">popularity of songs on streaming platforms</span> such as Spotify, Apple Music, and Deezer. The key metric used was the number of Spotify streams. By leveraging audio features and platform presence data, we aimed to identify which factors influence a song's streaming success and build a reliable regression model to estimate future song popularity.
""", unsafe_allow_html=True)

st.markdown("---")

# Methodology Section
st.markdown("## 🔬 Methodology Followed")
st.markdown('<p class="intro-text">A systematic data science lifecycle from exploration to deployment</p>', unsafe_allow_html=True)

st.markdown("We followed a typical data science lifecycle structured into the following phases:")

with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 1️⃣ Data Exploration and Cleaning")
        st.markdown("""
        - Removed unnecessary columns such as track names and artist names
        - Checked for missing values and cleaned the dataset
        - Performed exploratory analysis to visualize feature distributions
        """)
        
        st.markdown("### 2️⃣ Data Transformation")
        st.markdown("""
        - Observed heavy right-skew in the streams distribution
        - Applied log transformation to reduce skew and improve model performance
        """)
        
        st.markdown("### 3️⃣ Model Training")
        st.markdown("""
        - Trained three regression models: Linear Regression, Random Forest, and XGBoost
        - Evaluated models using R², MAE, and MSE
        - Performed cross-validation to assess generalizability
        """)
    
    with col2:
        st.markdown("### 4️⃣ Feature Importance")
        st.markdown("""
        - Extracted and visualized feature importance scores
        - Identified which features most strongly influence predictions
        """)
        
        st.markdown("### 5️⃣ Model Deployment")
        st.markdown("""
        - Saved the best performing model (Random Forest after log transformation)
        - Built a clean and interactive front-end using Streamlit
        - Created tools for predictions and data exploration
        """)

st.markdown("---")

# Key Learnings Section
st.markdown("## 💡 Key Learnings and Insights")
st.markdown('<p class="intro-text">Critical discoveries that shaped our understanding of streaming success</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    📈 **Platform Presence** (especially Spotify playlists and charts) is a strong predictor of success.
    
    🎵 **Audio Features** like energy, danceability, and tempo show moderate predictive power.
    """)

with col2:
    st.markdown("""
    📅 **Song Metadata** such as release month and artist count influence popularity trends.
    
    🎼 Pure musical features like key and mode had <span class="highlight">less direct impact</span> on performance.
    """, unsafe_allow_html=True)

st.markdown("---")

# Business Implications Section
st.markdown("## 💼 Business Implications")
st.markdown('<p class="intro-text">Strategic applications for the music industry</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **📈 Marketing Signal**
    
    Early playlist traction can act as a <span class="highlight">signal for marketing investment</span>.
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    **🎯 Strategic Planning**
    
    Understanding platform influence allows <span class="highlight">A&R and marketing teams</span> to plan better campaigns.
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    **🚀 Forecast Success**
    
    Data can be used to <span class="highlight">forecast breakout tracks</span> and improve ROI on promotions.
    """, unsafe_allow_html=True)

st.markdown("---")

# Next Steps Section
st.markdown("## 🚀 Next Steps & Future Improvements")
st.markdown('<p class="intro-text">Roadmap for enhancing the model and expanding its capabilities</p>', unsafe_allow_html=True)

st.markdown("""
- ✅ Incorporate additional sources (e.g., YouTube, TikTok trends) for richer prediction signals
- ✅ Experiment with ensemble models or neural networks for better accuracy
- ✅ Enable bulk predictions and CSV export functionality
- ✅ Monitor model drift and retrain periodically with updated data
""")

st.markdown("---")

# Conclusion
st.markdown("""
<div class="conclusion-box">
    <h3>✨ Impact & Value</h3>
    <p>
    This project offers both <span class="highlight">technical insight</span> and <span class="highlight">business value</span>, 
    showcasing how data-driven analysis can support decision-making in the music industry. By combining machine learning 
    with domain expertise, we've created a tool that empowers stakeholders to make informed decisions about song promotion, 
    artist development, and platform strategy.
    </p>
</div>
""", unsafe_allow_html=True)
