import streamlit as st
from PIL import Image
import base64
import io
import os

# ============================================================
# MUST BE FIRST — before any other st calls
# ============================================================
st.set_page_config(page_title="EDA Insights", layout="wide")


# ============================================================
# HELPER FUNCTIONS — defined before they are called
# ============================================================

def image_to_base64(image_path: str, max_width: int = 900) -> str:
    """Convert a local image to a base64 string for HTML embedding."""
    img = Image.open(image_path)
    if img.width > max_width:
        ratio = max_width / img.width
        new_size = (max_width, int(img.height * ratio))
        img = img.resize(new_size, Image.LANCZOS)
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    encoded = base64.b64encode(buffer.getvalue()).decode()
    return encoded


def inject_hover_card_styles():
    """Injects CSS for the hover insight cards. Call once at top of page."""
    st.markdown("""
    <style>

    .insight-card {
        position: relative;
        width: 100%;
        border-radius: 16px;
        overflow: hidden;
        margin-bottom: 32px;
        border: 1px solid rgba(255, 255, 255, 0.06);
        background: rgba(255, 255, 255, 0.02);
        cursor: pointer;
    }

    .insight-card img {
        display: block;
        width: 100%;
        height: auto;
        border-radius: 16px;
        transition: filter 0.4s ease, transform 0.4s ease;
    }

    .insight-overlay {
        position: absolute;
        inset: 0;
        border-radius: 16px;
        background: linear-gradient(
            160deg,
            rgba(10, 5, 25, 0.97) 0%,
            rgba(20, 5, 40, 0.97) 100%
        );
        border: 1px solid rgba(255, 0, 204, 0.2);
        padding: 28px 32px;
        overflow-y: auto;
        opacity: 0;
        transform: translateY(8px);
        transition: opacity 0.35s ease, transform 0.35s ease;
        pointer-events: none;
    }

    .insight-card:hover img {
        filter: blur(3px) brightness(0.3);
        transform: scale(1.02);
    }

    .insight-card:hover .insight-overlay {
        opacity: 1;
        transform: translateY(0);
        pointer-events: auto;
    }

    .insight-overlay .card-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #ff99ee;
        letter-spacing: 0.04em;
        text-transform: uppercase;
        margin-bottom: 14px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .insight-overlay .card-title::before {
        content: "";
        display: inline-block;
        width: 3px;
        height: 16px;
        background: linear-gradient(180deg, #ff00cc, #6633ff);
        border-radius: 2px;
        flex-shrink: 0;
    }

    .insight-overlay p,
    .insight-overlay li {
        font-size: 0.88rem;
        line-height: 1.7;
        color: rgba(255, 255, 255, 0.82);
        margin-bottom: 6px;
    }

    .insight-overlay strong {
        color: #cc99ff;
        font-weight: 600;
    }

    .insight-overlay .tag-row {
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
        margin-top: 14px;
    }

    .insight-overlay .tag {
        background: rgba(255, 0, 204, 0.12);
        border: 1px solid rgba(255, 0, 204, 0.3);
        color: #ff99ee;
        border-radius: 20px;
        padding: 3px 12px;
        font-size: 0.75rem;
        font-weight: 500;
        letter-spacing: 0.03em;
    }

    .insight-caption {
        text-align: center;
        font-size: 0.82rem;
        color: rgba(255, 255, 255, 0.35);
        margin-top: -20px;
        margin-bottom: 24px;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }

    .hover-hint {
        position: absolute;
        bottom: 12px;
        right: 16px;
        font-size: 0.72rem;
        color: rgba(255, 255, 255, 0.3);
        letter-spacing: 0.06em;
        text-transform: uppercase;
        transition: opacity 0.3s ease;
        pointer-events: none;
    }

    .insight-card:hover .hover-hint {
        opacity: 0;
    }

    </style>
    """, unsafe_allow_html=True)


def display_hover_insight(image_path: str, caption: str, insight_html: str, tags: list = None):
    """Renders a full-width chart card with hover-reveal insight overlay."""
    b64 = image_to_base64(image_path)

    tag_html = ""
    if tags:
        pills = "".join(f'<span class="tag">{t}</span>' for t in tags)
        tag_html = f'<div class="tag-row">{pills}</div>'

    html = f"""
    <div class="insight-card">
        <img src="data:image/png;base64,{b64}" alt="{caption}" />
        <div class="hover-hint">⟳ hover for insight</div>
        <div class="insight-overlay">
            <div class="card-title">{caption}</div>
            {insight_html}
            {tag_html}
        </div>
    </div>
    <div class="insight-caption">↑ hover chart to reveal insights</div>
    """
    st.markdown(html, unsafe_allow_html=True)


# ============================================================
# NAV — after set_page_config, after all function definitions
# ============================================================
from components.nav import render_nav
render_nav("EDA Insights")

# ============================================================
# INJECT STYLES — now safe, function is already defined above
# ============================================================
inject_hover_card_styles()

# ============================================================
# PAGE HEADER
# ============================================================
st.markdown("""
# 📊 EDA Insights

Welcome to the **Exploratory Data Analysis** section.  
Here we break down patterns that help explain what drives a song's popularity on streaming platforms.

---
""")

image_dir = "images"


# ============================================================
# INSIGHT CARDS — filenames exactly match GitHub repo
# ============================================================

# 1. Distribution of Streams
display_hover_insight(
    image_path=os.path.join(image_dir, "Distribution (Spotify Streams).png"),
    caption="Distribution of Average Streams",
    insight_html="""
    <p><strong>Skewed Distribution</strong><br>
    The stream count distribution is heavily right-skewed — most songs have relatively
    low streams, but a few songs go viral and dominate.</p>

    <p><strong>Real-World Pattern</strong><br>
    This mirrors the "winner-takes-most" trend in digital platforms like Spotify and YouTube.</p>

    <p><strong>Why It Matters for Modeling</strong><br>
    Models trained on such data get biased by extreme outliers. To solve this, we applied a
    <strong>log transformation</strong> on stream counts to reduce skew, improve learning,
    and focus on relative performance rather than absolute outliers.</p>

    <p><strong>Business Implication</strong><br>
    Since only a few songs achieve viral success, it's crucial to identify early breakout signals.
    Marketing teams should focus on rapid playlist growth and cross-platform exposure trends.</p>
    """,
    tags=["Right-Skewed", "Log Transformation", "Outlier Analysis", "Spotify"]
)

# 2. Correlation Matrix
display_hover_insight(
    image_path=os.path.join(image_dir, "Correlation Matrix.png"),
    caption="Correlation Matrix of Numerical Features",
    insight_html="""
    <p><strong>Strongest Positive Correlations with Streams</strong><br>
    <strong>in_spotify_playlists → 0.79</strong>, in_spotify_charts → 0.60,
    and in_apple_playlists, in_apple_charts, in_shazam_charts show moderate correlation.
    Platform visibility is the strongest driver of streams.</p>

    <p><strong>Moderate / Negative Correlations</strong><br>
    acousticness_% and instrumentalness_% show mild negative correlation.
    danceability_% and energy_% are mildly positive — more energetic, less acoustic
    songs tend to perform better.</p>

    <p><strong>Low / No Correlation</strong><br>
    speechiness_%, liveness_%, and key_encoded showed little or no correlation with streams.
    These are weak predictors in linear models.</p>

    <p><strong>Business Implication</strong><br>
    Playlist and chart inclusion — especially on Spotify — strongly correlates with success.
    Marketing teams should prioritize playlist placements as the #1 lever.</p>
    """,
    tags=["Correlation", "Feature Selection", "Spotify Playlists", "Multicollinearity"]
)

# 3. Scatterplots — Audio Features vs Streams
display_hover_insight(
    image_path=os.path.join(image_dir, "dance_valence_energy_vs_streams.png"),
    caption="Scatterplots — Audio Features vs. Streams",
    insight_html="""
    <p><strong>Danceability & Energy</strong><br>
    Songs with moderate to high danceability and energy tend to have higher streams.
    The majority of top-streamed songs sit in the <strong>60–80% range</strong> for both.
    However, these features alone aren't enough — they play a supporting role.</p>

    <p><strong>Valence (Positivity)</strong><br>
    The distribution is much wider — some very positive songs are streamed a lot,
    but many aren't. Valence isn't a clear standalone indicator of popularity.</p>

    <p><strong>What This Tells Us</strong><br>
    These features work better as interacting variables in a model. Energy and danceability
    make songs playlist-friendly, but only when backed by platform visibility.</p>

    <p><strong>Business Use-Case</strong><br>
    Marketing teams can promote high-danceability and energy songs in dance, workout,
    or party playlists. A&R teams can use energy profile as an early screening signal.</p>
    """,
    tags=["Danceability", "Energy", "Valence", "Audio Features"]
)

# 4. Boxplot — Streams by Musical Key
display_hover_insight(
    image_path=os.path.join(image_dir, "Streams by Musical Keys (boxplot).png"),
    caption="Boxplot — Streams by Musical Key",
    insight_html="""
    <p><strong>What We Observed</strong><br>
    Some keys like <strong>C# and E</strong> showed a slightly higher median number of streams,
    but overall the variation across keys was not significant.</p>

    <p><strong>Outliers</strong><br>
    A few keys had outlier songs with very high stream counts — but that's likely due to
    artist brand or platform push, not the key itself.</p>

    <p><strong>Takeaway</strong><br>
    Musical key alone doesn't determine popularity. It may have minor influence but shouldn't
    be heavily relied on for playlist or promotion decisions.</p>
    """,
    tags=["Musical Key", "Boxplot", "Low Impact Feature"]
)

# 5. Boxplot — Streams by Mode
display_hover_insight(
    image_path=os.path.join(image_dir, "Streams by Mode (boxplot).png"),
    caption="Boxplot — Streams by Mode (Major / Minor)",
    insight_html="""
    <p><strong>What We Observed</strong><br>
    Songs in <strong>major mode</strong> tend to have slightly higher median streams.
    More viral outliers also exist in major mode.</p>

    <p><strong>Why</strong><br>
    Major mode songs are often perceived as happier or more energetic, which may explain
    their slight advantage in mainstream streaming.</p>

    <p><strong>Takeaway</strong><br>
    Mode is not a strong standalone predictor, but for feel-good or mainstream playlists,
    favoring major key songs might provide a marginal boost.</p>
    """,
    tags=["Major Mode", "Minor Mode", "Boxplot", "Moderate Impact"]
)

# 6. BPM Distribution
display_hover_insight(
    image_path=os.path.join(image_dir, "Distribution (BPM).png"),
    caption="Distribution of BPM (Tempo)",
    insight_html="""
    <p><strong>What We Observed</strong><br>
    Most songs fall between <strong>80 and 140 BPM</strong>, with a peak around 120 BPM.
    This aligns with common tempos for pop, dance, and mainstream genres.</p>

    <p><strong>Fewer Extreme Tempos</strong><br>
    Very fast-paced songs (above 160 BPM) are rare, suggesting they aren't the norm
    for mainstream streaming success.</p>

    <p><strong>Takeaway</strong><br>
    Moderate tempos (~120 BPM) appear to be a sweet spot. A&R teams can use this as
    a baseline when screening tracks for mainstream releases or playlist curation.</p>
    """,
    tags=["BPM", "Tempo", "Pop", "Distribution"]
)

# 7. Average Streams by Release Month
display_hover_insight(
    image_path=os.path.join(image_dir, "Average Streams by release month.png"),
    caption="Average Streams by Release Month",
    insight_html="""
    <p><strong>What We Observed</strong><br>
    <strong>January, May, and September</strong> stand out with higher average stream counts.
    July and November showed slightly lower averages.</p>

    <p><strong>Why This Pattern Exists</strong><br>
    Seasonal listening behavior drives this — New Year activity (Jan), summer breaks (May),
    and festive buildup (Sept) all correlate with higher platform engagement.</p>

    <p><strong>Business Implication</strong><br>
    Release timing matters — especially for first-week performance and playlist push.
    Launching around January or September can provide a natural stream boost.</p>

    <p><strong>A&R / Marketing Takeaway</strong><br>
    Strategize launch windows around high-traffic months. Align marketing budgets and
    playlist campaigns accordingly and prepare content in advance for seasonal spikes.</p>
    """,
    tags=["Release Month", "Seasonality", "Marketing Strategy", "Timing"]
)

# 8. Playlist Count vs Streams
display_hover_insight(
    image_path=os.path.join(image_dir, "in_playlist vs Streams.png"),
    caption="Number of Playlists vs. Streams",
    insight_html="""
    <p><strong>Core Finding</strong><br>
    Across Spotify, Apple Music, and Deezer — <strong>more playlist presence = more streams</strong>.
    The trend is strongest on Spotify where editorial and algorithmic playlists have massive reach.</p>

    <p><strong>Platform Breakdown</strong><br>
    Apple Music shows a similar pattern with slightly more spread. Deezer's trend is weaker,
    likely due to lower dataset representation.</p>

    <p><strong>For the Marketing Team</strong><br>
    Actively work with playlist curators and editorial teams. Invest in metadata optimization,
    social buzz, and early traction — all of which trigger algorithmic playlist inclusion.</p>

    <p><strong>For A&R Teams</strong><br>
    When scouting songs, check performance <em>relative to playlist support</em>. A song doing
    well without playlist backing is organically strong and worth investing in.</p>
    """,
    tags=["Playlists", "Spotify", "Apple Music", "Platform Strategy", "Key Driver"]
)
