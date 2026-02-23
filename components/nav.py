import streamlit as st


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

PAGES = {
    "Home": "Home.py",
    "EDA Insights": "pages/EDA_Insights.py",
    "Model Training Information": "pages/Model Training Information.py",
    "Prediction Tool": "pages/Prediction Tool.py",
    "Project Summary": "pages/Project_Summary.py",
}


# ==========================================================
# CSS INJECTION
# ==========================================================

def inject_nav_styles():
    """
    Injects stable navigation styling.
    Does NOT break layout.
    """

    st.markdown(
        """
        <style>

        /* Hide Streamlit sidebar completely */
        section[data-testid="stSidebar"] {
            display: none !important;
        }

        /* Remove extra left padding caused by sidebar */
        section.main > div {
            padding-left: 2rem;
            padding-right: 2rem;
        }

        /* Button base style */
        div.stButton > button {
            border-radius: 30px;
            padding: 10px 24px;
            background: rgba(255,255,255,0.05);
            color: white;
            font-weight: 500;
            border: 1px solid rgba(255,255,255,0.08);
            transition: all 0.2s ease;
        }

        /* Hover effect */
        div.stButton > button:hover {
            background: rgba(255,255,255,0.1);
            transform: translateY(-2px);
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


# ==========================================================
# NAVIGATION RENDER
# ==========================================================

def render_nav(active_page: str):
    """
    Renders stable top navigation.
    active_page parameter retained for future use,
    but not used for styling to preserve layout integrity.
    """

    inject_nav_styles()

    cols = st.columns(len(PAGES))

    for i, (name, path) in enumerate(PAGES.items()):
        with cols[i]:
            if st.button(name, key=f"nav_{name}"):
                st.switch_page(path)
