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
    [data-testid="stAppViewContainer"] h1 {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.8em;
        font-weight: 800;
        margin-bottom: 2rem;
        text-shadow: 0 0 30px rgba(102, 126, 234, 0.3);
    }

    /* Section header styling */
    .section-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 1.8em;
        font-weight: 700;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        position: relative;
        padding-bottom: 0.5rem;
    }

    .section-header::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 60px;
        height: 3px;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        border-radius: 2px;
    }

    /* Card styling for sections */
    .section-card {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border: 1px solid rgba(102, 126, 234, 0.3);
        border-radius: 12px;
        padding: 2rem;
        margin: 1.5rem 0;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }

    .section-card:hover {
        border-color: rgba(102, 126, 234, 0.6);
        box-shadow: 0 8px 32px rgba(102, 126, 234, 0.2);
        transform: translateY(-2px);
    }

    /* Subsection headers */
    .subsection-header {
        color: #667eea;
        font-size: 1.3em;
        font-weight: 600;
        margin-top: 1.2rem;
        margin-bottom: 0.8rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    /* List item styling */
    .custom-list {
        list-style: none;
        padding: 0;
    }

    .custom-list li {
        padding: 0.7rem 0;
        padding-left: 1.8rem;
        position: relative;
        color: #e0e0e0;
        line-height: 1.6;
        font-size: 0.95rem;
    }

    .custom-list li::before {
        content: '▸';
        position: absolute;
        left: 0;
        color: #764ba2;
        font-weight: bold;
        font-size: 1.2em;
    }

    /* Highlight styling */
    .highlight {
        background: linear-gradient(120deg, rgba(102, 126, 234, 0.2), rgba(118, 75, 162, 0.2));
        padding: 0.2em 0.5em;
        border-radius: 4px;
        color: #a8d5ff;
        font-weight: 600;
    }

    /* Divider styling */
    .custom-divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.5), transparent);
        margin: 2rem 0;
        border-radius: 1px;
    }

    /* Section intro text */
    .section-intro {
        color: #b0b0b0;
        font-size: 1rem;
        line-height: 1.7;
        margin-bottom: 1.5rem;
        font-style: italic;
    }

    /* Conclusion box */
    .conclusion-box {
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.1) 0%, rgba(102, 126, 234, 0.1) 100%);
        border-left: 4px solid #00d4ff;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 2rem 0;
        color: #e0e0e0;
    }

    /* Smooth transitions */
    * {
        transition: color 0.3s ease, background 0.3s ease;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# PAGE CONTENT
# ============================================================================

st.title("📊 Project Summary")

# Problem Statement Section
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">🎯 Problem Statement</h2>', unsafe_allow_html=True)

st.markdown("""
<p class="section-intro">
Understanding what drives song popularity in the streaming era
</p>

The goal of this project was to analyze and predict the <span class="highlight">popularity of songs on streaming platforms</span> such as Spotify, Apple Music, and Deezer. The key metric used was the number of Spotify streams. By leveraging audio features and platform presence data, we aimed to identify which factors influence a song's streaming success and build a reliable regression model to estimate future song popularity.
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Methodology Section
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">🔬 Methodology Followed</h2>', unsafe_allow_html=True)

st.markdown("""
<p class="section-intro">
A systematic data science lifecycle from exploration to deployment
</p>

We followed a typical data science lifecycle structured into the following phases:
""", unsafe_allow_html=True)

# Methodology Subsections
methodology_items = [
    {
        "title": "1. Data Exploration and Cleaning",
        "items": [
            "Removed unnecessary columns such as track names and artist names to avoid NLP-based influence.",
            "Checked for missing values and cleaned the dataset.",
            "Performed exploratory analysis to visualize feature distributions and relationships with the target."
        ]
    },
    {
        "title": "2. Data Transformation",
        "items": [
            "Observed heavy right-skew in the streams distribution.",
            "Applied log transformation to reduce skew and improve model performance on outliers."
        ]
    },
    {
        "title": "3. Model Training",
        "items": [
            "Trained three regression models: Linear Regression, Random Forest, and XGBoost.",
            "Evaluated models using R², MAE, and MSE.",
            "Performed cross-validation to assess generalizability."
        ]
    },
    {
        "title": "4. Feature Importance",
        "items": [
            "Extracted and visualized feature importance scores for Random Forest and XGBoost.",
            "Identified which features most strongly influence predictions."
        ]
    },
    {
        "title": "5. Model Deployment",
        "items": [
            "Saved the best performing model (Random Forest after log transformation).",
            "Built a clean and interactive front-end using Streamlit for predictions and data exploration."
        ]
    }
]

for item in methodology_items:
    st.markdown(f'<h3 class="subsection-header">⚙️ {item["title"]}</h3>', unsafe_allow_html=True)
    
    list_html = '<ul class="custom-list">'
    for point in item["items"]:
        list_html += f'<li>{point}</li>'
    list_html += '</ul>'
    
    st.markdown(list_html, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Key Learnings Section
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">💡 Key Learnings and Insights</h2>', unsafe_allow_html=True)

st.markdown("""
<p class="section-intro">
Critical discoveries that shaped our understanding of streaming success
</p>
""", unsafe_allow_html=True)

learnings = [
    ("<span class=\"highlight\">Platform Presence</span> (especially Spotify playlists and charts) is a strong predictor of success.", "📈"),
    ("<span class=\"highlight\">Audio Features</span> like energy, danceability, and tempo show moderate predictive power.", "🎵"),
    ("<span class=\"highlight\">Song Metadata</span> such as release month and artist count influence popularity trends.", "📅"),
    ("Pure musical features like key and mode had <span class=\"highlight\">less direct impact</span> on performance.", "🎼")
]

learning_html = '<ul class="custom-list">'
for learning, emoji in learnings:
    learning_html += f'<li>{emoji} {learning}</li>'
learning_html += '</ul>'

st.markdown(learning_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Business Implications Section
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">💼 Business Implications</h2>', unsafe_allow_html=True)

st.markdown("""
<p class="section-intro">
Strategic applications for the music industry
</p>
""", unsafe_allow_html=True)

implications = [
    "Early playlist traction can act as a <span class=\"highlight\">signal for marketing investment</span>.",
    "Understanding platform influence allows <span class=\"highlight\">A&R and marketing teams</span> to plan better campaigns.",
    "Release timing, energy, and exposure data can be used to <span class=\"highlight\">forecast breakout tracks</span> and improve ROI on promotions."
]

implications_html = '<ul class="custom-list">'
for impl in implications:
    implications_html += f'<li>{impl}</li>'
implications_html += '</ul>'

st.markdown(implications_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Next Steps Section
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">🚀 Next Steps & Future Improvements</h2>', unsafe_allow_html=True)

st.markdown("""
<p class="section-intro">
Roadmap for enhancing the model and expanding its capabilities
</p>
""", unsafe_allow_html=True)

next_steps = [
    "Incorporate additional sources (e.g., YouTube, TikTok trends) for richer prediction signals.",
    "Experiment with ensemble models or neural networks for better accuracy.",
    "Enable bulk predictions and CSV export functionality.",
    "Monitor model drift and retrain periodically with updated data."
]

next_steps_html = '<ul class="custom-list">'
for step in next_steps:
    next_steps_html += f'<li>{step}</li>'
next_steps_html += '</ul>'

st.markdown(next_steps_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Conclusion
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="conclusion-box">
    <h3 style="margin-top: 0; color: #00d4ff;">✨ Impact & Value</h3>
    <p>
    This project offers both <span class="highlight">technical insight</span> and <span class="highlight">business value</span>, 
    showcasing how data-driven analysis can support decision-making in the music industry. By combining machine learning 
    with domain expertise, we've created a tool that empowers stakeholders to make informed decisions about song promotion, 
    artist development, and platform strategy.
    </p>
</div>
""", unsafe_allow_html=True)
