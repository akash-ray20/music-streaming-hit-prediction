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
       4. HOVER STATE — only for inactive tabs
    ====================================================== */

    .inactive-tab div.stButton > button:hover {
        transform: translateY(-3px);
        background: rgba(255,255,255,0.1);
        box-shadow: 0 6px 25px rgba(255, 0, 200, 0.4);
        cursor: pointer;
    }


    /* ======================================================
       5. ACTIVE TAB STATE
    ====================================================== */

    .active-tab div.stButton > button {
        background: rgba(255, 0, 204, 0.12);
        border: 1px solid rgba(255, 0, 204, 0.35);
        box-shadow: 0 0 14px rgba(255, 0, 204, 0.25);
        color: #ff99ee;
        font-weight: 700;
        cursor: default;
        transform: none;
    }

    /* Kill hover effect on active tab */
    .active-tab div.stButton > button:hover {
        transform: none;
        background: rgba(255, 0, 204, 0.12);
        box-shadow: 0 0 14px rgba(255, 0, 204, 0.25);
        cursor: default;
    }


    </style>
    """, unsafe_allow_html=True)


# ==========================================================
# NAV RENDER FUNCTION
# ==========================================================

def render_nav(active_page: str):

    inject_nav_styles()

    cols = st.columns(len(PAGES))

    for i, (name, path) in enumerate(PAGES.items()):
        with cols[i]:
            is_active = name == active_page
            wrapper_class = "active-tab" if is_active else "inactive-tab"
            
            st.markdown(f'<div class="{wrapper_class}">', unsafe_allow_html=True)
            
            if st.button(name, key=f"nav_{name}"):
                if not is_active:
                    st.switch_page(path)
            
            st.markdown('</div>', unsafe_allow_html=True)
