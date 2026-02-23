import streamlit as st


# ==========================================================
# NAVIGATION CONFIGURATION
# ==========================================================

PAGES = {
    "Home": "Home.py",
    "EDA Insights": "pages/EDA_Insights.py",
    "Model Training": "pages/Model Training Information.py",
    "Prediction Tool": "pages/Prediction Tool.py",
    "Project Summary": "pages/Project_Summary.py"
}


# ==========================================================
# CSS STYLING INJECTION
# ==========================================================

def inject_nav_styles():
    """
    Injects all navigation-related CSS.
    Keep ALL visual changes inside this function.
    """

    st.markdown("""
    <style>

    /* ======================================================
       1. LAYOUT CONTROL
    ====================================================== */

    /* Hide Streamlit sidebar */
    section[data-testid="stSidebar"] {
        display: none;
    }

    /* Adjust main padding after sidebar removal */
    section.main > div {
        padding-left: 2rem;
    }


    /* ======================================================
       2. NAV CONTAINER STRUCTURE
    ====================================================== */

    .nav-row {
        margin-bottom: 40px;
    }


    /* ======================================================
       3. BUTTON BASE STYLE
    ====================================================== */

    div.stButton > button {
        border-radius: 30px;
        padding: 10px 24px;
        background: rgba(255,255,255,0.05);
        backdrop-filter: blur(8px);
        color: white;
        font-weight: 500;
        border: 1px solid rgba(255,255,255,0.08);
        transition: all 0.25s ease;
    }


    /* ======================================================
       4. HOVER STATE
    ====================================================== */

    div.stButton > button:hover {
        transform: translateY(-3px);
        background: rgba(255,255,255,0.1);
        box-shadow: 0 6px 25px rgba(255, 0, 200, 0.4);
    }



    /* ======================================================
       5. ACTIVE TAB STATE
    ====================================================== */

    .active-tab div.stButton > button {
        background: rgba(255,255,255,0.08);
        border-bottom: 3px solid transparent;
        border-image: linear-gradient(90deg, #ff00cc, #3333ff) 1;
        text-decoration: underline;
        text-underline-offset: 6px;
        text-decoration-thickness: 2px;
    }


    </style>
    """, unsafe_allow_html=True)


# ==========================================================
# NAV RENDER FUNCTION
# ==========================================================

def render_nav(active_page: str):

    inject_nav_styles()

    # Inject dynamic active button style
    st.markdown(f"""
        <style>
        button[data-testid="baseButton-nav_{active_page}"] {{
            text-decoration: underline;
            text-underline-offset: 6px;
            text-decoration-thickness: 2px;
        }}
        </style>
    """, unsafe_allow_html=True)

    cols = st.columns(len(PAGES))

    for i, (name, path) in enumerate(PAGES.items()):
        with cols[i]:
            if st.button(name, key=f"nav_{name}"):
                st.switch_page(path)
