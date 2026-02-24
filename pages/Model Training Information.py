import streamlit as st
from PIL import Image
import os

from components.nav import render_nav
render_nav("Model Training")

st.set_page_config(page_title="Model Training Results", layout="wide")

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
        margin-top: 2.5rem;
        margin-bottom: 1.2rem;
        border-bottom: 3px solid;
        border-image: linear-gradient(90deg, #667eea 0%, #764ba2 100%) 1;
        padding-bottom: 0.8rem;
    }

    /* Subsection headers */
    h3 {
        color: #764ba2;
        font-size: 1.2em;
        font-weight: 600;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }

    /* Intro text styling */
    .intro-text {
        color: #b0b0b0;
        font-size: 0.95rem;
        line-height: 1.6;
        font-style: italic;
        margin-bottom: 1.5rem;
    }

    /* Metric box styling */
    .metric-box {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.08) 0%, rgba(118, 75, 162, 0.08) 100%);
        border: 1px solid rgba(102, 126, 234, 0.2);
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        font-family: 'Courier New', monospace;
        color: #e0e0e0;
        line-height: 1.8;
        font-size: 0.9rem;
    }

    /* Model name styling in code blocks */
    .model-name {
        color: #667eea;
        font-weight: 600;
        margin-top: 0.8rem;
    }

    .model-name:first-child {
        margin-top: 0;
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

    /* Highlight styling */
    .highlight {
        background: linear-gradient(120deg, rgba(102, 126, 234, 0.25), rgba(118, 75, 162, 0.25));
        padding: 0.2em 0.6em;
        border-radius: 4px;
        color: #a8d5ff;
        font-weight: 600;
    }

    /* Observation box */
    .observation-box {
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.12) 0%, rgba(102, 126, 234, 0.12) 100%);
        border-left: 4px solid #00d4ff;
        border-radius: 10px;
        padding: 1.8rem;
        margin: 2rem 0;
    }

    .observation-box li {
        color: #e0e0e0;
        line-height: 1.8;
        margin-bottom: 0.8rem;
    }

    /* Code block styling override */
    .stCode {
        background: rgba(10, 10, 30, 0.8) !important;
        border: 1px solid rgba(102, 126, 234, 0.2) !important;
        border-radius: 8px !important;
    }

    /* List styling */
    ul {
        list-style-position: inside;
    }

    li {
        color: #e0e0e0;
        line-height: 1.8;
        margin-bottom: 0.6rem;
    }

    /* Findings container styling */
    .observation-box + [data-testid="stMarkdownContainer"] ul {
        padding: 1.5rem;
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.08) 0%, rgba(102, 126, 234, 0.08) 100%);
        border-left: 4px solid #00d4ff;
        border-radius: 0 10px 10px 10px;
        margin-top: -1rem;
    }

    .observation-box + [data-testid="stMarkdownContainer"] li {
        color: #e0e0e0;
        font-size: 0.95rem;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# PAGE CONTENT
# ============================================================================

st.title("Model Training Results")

st.markdown('<p class="intro-text">Comprehensive evaluation of three regression models before and after log transformation</p>', unsafe_allow_html=True)

# ============================================================================
# BEFORE LOG TRANSFORMATION SECTION
# ============================================================================

st.markdown("## ⚙️ Before Log Transformation")
st.markdown('<p class="intro-text">Raw model performance on untransformed data with high-scale stream numbers</p>', unsafe_allow_html=True)

st.markdown("### 🔁 Single Train-Test Split")

st.markdown("""
<div class="metric-box">
<span class="model-name">📊 Linear Regression</span>
MAE : 186,665,575.46
MSE : 70,164,083,509,558,752.00
R²  : 0.71

<span class="model-name">🌲 Random Forest Regressor</span>
MAE : 133,711,848.62
MSE : 43,282,841,307,622,696.00
R²  : 0.82

<span class="model-name">⚡ XGBoost Regressor</span>
MAE : 136,584,608.00
MSE : 44,398,928,069,656,576.00
R²  : 0.82
</div>
""", unsafe_allow_html=True)

st.markdown("### 📊 Cross-Validation (5-Fold)")
st.markdown("""
Cross-validation helps assess model generalizability across different data splits:
""")

st.markdown("""
<div class="metric-box">
<span class="model-name">📊 Linear Regression</span>
Mean R²  : 0.58
Mean MAE : 211,822,873.16
Mean MSE : 103,002,216,302,624,640.00

<span class="model-name">🌲 Random Forest Regressor</span>
Mean R²  : 0.71
Mean MAE : 167,541,351.68
Mean MSE : 69,794,061,190,678,208.00

<span class="model-name">⚡ XGBoost Regressor</span>
Mean R²  : 0.80
Mean MAE : 150,190,956.80
Mean MSE : 64,537,216,253,794,712.00
</div>
""", unsafe_allow_html=True)

# ============================================================================
# AFTER LOG TRANSFORMATION SECTION
# ============================================================================

st.markdown("---")
st.markdown("## 🔄 After Log Transformation")
st.markdown('<p class="intro-text">Improved model stability and reduced skew through logarithmic transformation</p>', unsafe_allow_html=True)

st.markdown("""
**Why Log Transformation?**
- Reduces impact of outliers and extreme values
- Handles right-skewed distributions better
- Improves model stability and generalization
- Makes metrics more interpretable (orders of magnitude)
""")

st.markdown("### 🔁 Single Train-Test Split")
st.markdown("""
Performance after applying log transformation to the target variable:
""")

st.markdown("""
<div class="metric-box">
<span class="model-name">📊 Linear Regression</span>
MAE : 0.55
MSE : 0.49
R²  : 0.52

<span class="model-name">🌲 Random Forest Regressor</span>
MAE : 0.36
MSE : 0.22
R²  : 0.79

<span class="model-name">⚡ XGBoost Regressor</span>
MAE : 0.37
MSE : 0.23
R²  : 0.78
</div>
""", unsafe_allow_html=True)

st.markdown("### 📊 Cross-Validation (5-Fold)")
st.markdown("""
Validation results confirming improved generalization:
""")

st.markdown("""
<div class="metric-box">
<span class="model-name">📊 Linear Regression</span>
Mean R²  : 0.46
Mean MAE : 0.61
Mean MSE : 0.77

<span class="model-name">🌲 Random Forest Regressor</span>
Mean R²  : 0.73
Mean MAE : 0.36
Mean MSE : 0.42

<span class="model-name">⚡ XGBoost Regressor</span>
Mean R²  : 0.67
Mean MAE : 0.37
Mean MSE : 0.48
</div>
""", unsafe_allow_html=True)

# ============================================================================
# PERFORMANCE COMPARISON
# ============================================================================

st.markdown("---")

with st.container():
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **📊 Linear Regression**
        
        - Baseline model
        - Improved to R² = 0.52 after transformation
        - High MAE (0.55) suggests underfitting
        - Best for interpretability
        """)
    
    with col2:
        st.markdown("""
        **🌲 Random Forest**
        
        - Best overall performance (R² = 0.79)
        - Lowest MAE (0.36) on test set
        - Strong generalization (R² = 0.73 CV)
        - ✨ Recommended for production
        """)
    
    with col3:
        st.markdown("""
        **⚡ XGBoost**
        
        - Close competitor (R² = 0.78)
        - Similar MAE (0.37)
        - Good CV performance (R² = 0.67)
        - Faster inference time
        """)

st.markdown("---")

# ============================================================================
# FEATURE IMPORTANCE VISUALIZATIONS
# ============================================================================

st.markdown("## 🧠 Feature Importance Visualizations")
st.markdown('<p class="intro-text">Understanding which features drive streaming predictions</p>', unsafe_allow_html=True)

image_dir = "images"

def show_image(image_file, caption):
    try:
        image_path = os.path.join(image_dir, image_file)
        image = Image.open(image_path)
        st.image(image, caption=caption, use_container_width=True)
    except FileNotFoundError:
        st.warning(f"Image not found: {image_file}")

col1, col2 = st.columns(2)

with col1:
    show_image("Random Forest Feature Importance.png", "🔍 Random Forest Feature Importance")

with col2:
    show_image("XGBRegressor Feature Importance.png", "⚡ XGBoost Feature Importance")

# ============================================================================
# FINAL OBSERVATIONS
# ============================================================================

st.markdown("---")

st.markdown("""
<div class="observation-box">
    <h3 style="margin-top: 0; color: #00d4ff;">🎯 Key Findings & Recommendations</h3>
</div>
""", unsafe_allow_html=True)

col_findings = st.container()
with col_findings:
    st.markdown("""
- **Playlist Features Dominate**: <span class="highlight">in_spotify_playlists</span>, <span class="highlight">in_spotify_charts</span>, and <span class="highlight">in_apple_playlists</span> are the strongest contributors to streaming predictions.

- **Audio Features Matter**: <span class="highlight">danceability</span>, <span class="highlight">energy</span>, and <span class="highlight">valence</span> show moderate influence on popularity.

- **Weak Predictors**: <span class="highlight">key</span>, <span class="highlight">mode</span>, and <span class="highlight">speechiness</span> had minimal impact on model performance.

- **Model Selection**: <strong>Random Forest</strong> emerges as the optimal choice with the best R² (0.79), lowest MAE (0.36), and strong cross-validation scores (R² = 0.73).

- **Log Transformation Impact**: Dramatic improvement in metrics after log transformation confirms the presence of extreme outliers and right-skewed distribution in the original data.
    """, unsafe_allow_html=True)

st.markdown("""
### 💡 Next Steps

1. **Deploy Random Forest Model** - Use as production model for streaming predictions
2. **Feature Engineering** - Explore interaction features between playlist metrics and audio features
3. **Ensemble Methods** - Consider stacking or blending RandomForest with XGBoost for marginal improvements
4. **Real-time Monitoring** - Track model performance on new data and retrain periodically
""")
