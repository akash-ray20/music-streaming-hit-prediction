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
<div style="
    background: linear-gradient(90deg, #1f2937, #111827);
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 25px;
">
    <h1 style="margin-bottom: 5px;">🧠 Predict Song Popularity</h1>
    <p style="margin-top: 0;">
    Estimate expected stream counts using a trained Random Forest model.
    </p>
    <p style="font-size: 14px; opacity: 0.8;">
    Model trained on log-transformed stream data for improved generalization.
    </p>
</div>
""", unsafe_allow_html=True)

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
    key_options = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    selected_key = st.selectbox("Musical Key", key_options, index=0)
    key_mapping = {
        'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5,
        'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11
    }
    key_encoded = key_mapping[selected_key]
    mode = st.radio("Mode", options=[0, 1], index=1, format_func=lambda x: "Minor" if x == 0 else "Major")

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
st.markdown("---")

if st.button("🎯 Predict Number of Streams"):
    try:
        log_pred = model.predict(input_df)[0]
        predicted_streams = int(np.exp(log_pred))
        st.success(f"🎧 **Estimated Streams:** {predicted_streams:,}")
        st.caption("This prediction assumes distribution similar to the dataset and average platform visibility.")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
