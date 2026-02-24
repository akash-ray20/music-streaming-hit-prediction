import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ============================================================
# MUST BE FIRST
# ============================================================
st.set_page_config(page_title="Predict Song Streams", layout="wide")

from components.nav import render_nav
render_nav("Prediction Tool")

# ============================================================
# PAGE HEADER
# ============================================================

st.markdown("""
<style>
@keyframes pulse-bar {
    0%, 100% { transform: scaleY(1); opacity: 0.7; }
    50%       { transform: scaleY(1.6); opacity: 1; }
}
.hero-banner {
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, #0d0d1a 0%, #1a0a2e 40%, #0a1628 100%);
    border: 1px solid rgba(255, 0, 204, 0.2);
    border-radius: 18px;
    padding: 36px 40px;
    margin-bottom: 28px;
}
.eq-bars {
    position: absolute;
    right: 40px;
    top: 50%;
    transform: translateY(-50%);
    display: flex;
    align-items: flex-end;
    gap: 5px;
    height: 60px;
    opacity: 0.25;
}
.eq-bar {
    width: 6px;
    border-radius: 3px;
    background: linear-gradient(180deg, #ff00cc, #6633ff);
    animation: pulse-bar 1.2s ease-in-out infinite;
}
.eq-bar:nth-child(1) { height: 30%; animation-delay: 0.0s; }
.eq-bar:nth-child(2) { height: 70%; animation-delay: 0.15s; }
.eq-bar:nth-child(3) { height: 50%; animation-delay: 0.3s; }
.eq-bar:nth-child(4) { height: 90%; animation-delay: 0.45s; }
.eq-bar:nth-child(5) { height: 40%; animation-delay: 0.6s; }
.eq-bar:nth-child(6) { height: 75%; animation-delay: 0.75s; }
.eq-bar:nth-child(7) { height: 55%; animation-delay: 0.9s; }
.eq-bar:nth-child(8) { height: 85%; animation-delay: 1.05s; }
.hero-banner::before {
    content: "";
    position: absolute;
    top: -40px;
    left: -40px;
    width: 220px;
    height: 220px;
    background: radial-gradient(circle, rgba(255,0,204,0.12) 0%, transparent 70%);
    pointer-events: none;
}
.hero-tag {
    display: inline-block;
    background: rgba(255, 0, 204, 0.12);
    border: 1px solid rgba(255, 0, 204, 0.35);
    color: #ff99ee;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 4px 14px;
    border-radius: 20px;
    margin-bottom: 14px;
}
.hero-title {
    font-size: 2.2rem;
    font-weight: 800;
    margin: 0 0 10px 0;
    background: linear-gradient(90deg, #ffffff 0%, #cc99ff 60%, #ff99ee 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.2;
}
.hero-sub {
    font-size: 0.95rem;
    color: rgba(255,255,255,0.6);
    margin: 0 0 18px 0;
    max-width: 520px;
}
.hero-stats { display: flex; gap: 24px; flex-wrap: wrap; }
.hero-stat { display: flex; flex-direction: column; }
.hero-stat-value { font-size: 1.1rem; font-weight: 700; color: #ff99ee; }
.hero-stat-label { font-size: 0.72rem; color: rgba(255,255,255,0.4); letter-spacing: 0.06em; text-transform: uppercase; }
</style>
""", unsafe_allow_html=True)

st.markdown(
    "<div class='hero-banner'>"
    "<div class='eq-bars'>"
    "<div class='eq-bar'></div><div class='eq-bar'></div><div class='eq-bar'></div>"
    "<div class='eq-bar'></div><div class='eq-bar'></div><div class='eq-bar'></div>"
    "<div class='eq-bar'></div><div class='eq-bar'></div>"
    "</div>"
    "<div class='hero-tag'>&#127925; ML-Powered Stream Predictor</div>"
    "<h1 class='hero-title'>Predict Song Popularity</h1>"
    "<p class='hero-sub'>Tune your song attributes and get an instant stream estimate powered by a Random Forest model trained on data from Spotify.</p>"
    "<div class='hero-stats'>"
    "<div class='hero-stat'><span class='hero-stat-value'>~950</span><span class='hero-stat-label'>Songs Trained On</span></div>"
    "<div class='hero-stat'><span class='hero-stat-value'>R&#178; 0.79</span><span class='hero-stat-label'>Model Accuracy</span></div>"
    "<div class='hero-stat'><span class='hero-stat-value'>Log-Scale</span><span class='hero-stat-label'>Output Transform</span></div>"
    "<div class='hero-stat'><span class='hero-stat-value'>22</span><span class='hero-stat-label'>Input Features</span></div>"
    "</div></div>",
    unsafe_allow_html=True
)

# ============================================================
# LOAD MODEL
# ============================================================
@st.cache_resource
def load_model():
    return joblib.load("models/random_forest_log_model.pkl")

model = load_model()


# ============================================================
# SECTION 1 — RELEASE & PLATFORM INFO (3 columns)
# ============================================================
st.markdown("### 🎵 Release Information & Platform Presence")
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**🗓 Release Details**")
    artist_count = st.number_input("Number of Artists", min_value=1, max_value=10, value=1)
    released_year = st.selectbox("Release Year", options=range(2015, 2025), index=7)
    released_month = st.slider("Release Month", 1, 12, 6)
    released_day = st.slider("Release Day", 1, 31, 15)

with col2:
    st.markdown("**🎧 Spotify & Apple**")
    in_spotify_playlists = st.slider("In Spotify Playlists", 0, 500, 30)
    in_spotify_charts = st.slider("In Spotify Charts", 0, 200, 5)
    in_apple_playlists = st.slider("In Apple Playlists", 0, 200, 3)
    in_apple_charts = st.slider("In Apple Charts", 0, 200, 2)

with col3:
    st.markdown("**📊 Deezer, Shazam & Tempo**")
    in_deezer_playlists = st.slider("In Deezer Playlists", 0, 100, 1)
    in_deezer_charts = st.slider("In Deezer Charts", 0, 100, 1)
    in_shazam_charts = st.slider("In Shazam Charts", 0.0, 100.0, 2.5)
    bpm = st.slider("Beats Per Minute (BPM)", 60, 200, 120)

key_col, mode_col = st.columns([1, 2])
with key_col:
    key_options = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    selected_key = st.selectbox("Musical Key", key_options, index=0)
    key_mapping = {
        'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5,
        'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11
    }
    key_encoded = key_mapping[selected_key]
with mode_col:
    mode = st.radio("Mode", options=[0, 1], index=1, format_func=lambda x: "Minor" if x == 0 else "Major", horizontal=True)

# ============================================================
# SECTION 2 — AUDIO FEATURES (7 sliders in a row)
# ============================================================
st.markdown("### 🎚 Audio Features")
st.markdown("---")

a1, a2, a3, a4 = st.columns(4)
with a1:
    danceability = st.slider("Danceability (%)", 0, 100, 70)
with a2:
    valence = st.slider("Valence (%)", 0, 100, 60)
with a3:
    energy = st.slider("Energy (%)", 0, 100, 65)
with a4:
    acousticness = st.slider("Acousticness (%)", 0, 100, 15)

b1, b2, b3, b4 = st.columns(4)
with b1:
    instrumentalness = st.slider("Instrumentalness (%)", 0, 100, 10)
with b2:
    liveness = st.slider("Liveness (%)", 0, 100, 20)
with b3:
    speechiness = st.slider("Speechiness (%)", 0, 100, 5)
with b4:
    st.empty()  # intentional — keeps grid balanced with 7 items

# ============================================================
# BUILD INPUT DATAFRAME
# ============================================================
input_df = pd.DataFrame({
    'artist_count': [artist_count],
    'released_year': [released_year],
    'released_month': [released_month],
    'released_day': [released_day],
    'in_spotify_playlists': [in_spotify_playlists],
    'in_spotify_charts': [in_spotify_charts],
    'in_apple_playlists': [in_apple_playlists],
    'in_apple_charts': [in_apple_charts],
    'in_deezer_playlists': [in_deezer_playlists],
    'in_deezer_charts': [in_deezer_charts],
    'in_shazam_charts': [in_shazam_charts],
    'bpm': [bpm],
    'mode': [mode],
    'danceability_%': [danceability],
    'valence_%': [valence],
    'energy_%': [energy],
    'acousticness_%': [acousticness],
    'instrumentalness_%': [instrumentalness],
    'liveness_%': [liveness],
    'speechiness_%': [speechiness],
    'key_encoded': [key_encoded]
})

# ============================================================
# PREDICT
# ============================================================

st.markdown('<div class="predict-btn-container">', unsafe_allow_html=True)

predict_clicked = st.button("🎯 Predict Number of Streams", key="predict_btn")

st.markdown('</div>', unsafe_allow_html=True)

if predict_clicked:
    try:
        log_pred = model.predict(input_df)[0]
        predicted_streams = int(np.exp(log_pred))
        st.success(f"🎧 **Estimated Streams:** {predicted_streams:,}")
        st.caption("This prediction assumes distribution similar to the dataset and average platform visibility.")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
