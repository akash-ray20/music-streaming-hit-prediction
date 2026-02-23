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

    .nav-active button {
        background: linear-gradient(90deg, #ff00cc, #3333ff) !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 0 15px rgba(255, 0, 200, 0.6);
    }

    .nav-active button::after {
        content: "";
        display: block;
        margin: 6px auto 0 auto;
        width: 60%;
        height: 3px;
        background: linear-gradient(90deg, #ff00cc, #3333ff);
        border-radius: 5px;
    }

    </style>
    """, unsafe_allow_html=True)


# ==========================================================
# NAV RENDER FUNCTION
# ==========================================================

def render_nav(active_page: str):

    st.markdown("""
    <style>
    .nav-container {
        display: flex;
        justify-content: space-between;
        gap: 20px;
        margin-bottom: 40px;
    }

    .nav-item {
        padding: 10px 24px;
        border-radius: 30px;
        background: rgba(255,255,255,0.05);
        color: white;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.2s ease;
    }

    .nav-item:hover {
        background: rgba(255,255,255,0.1);
        transform: translateY(-2px);
    }

    .nav-active {
        background: linear-gradient(90deg, #ff00cc, #3333ff);
        box-shadow: 0 0 15px rgba(255,0,200,0.6);
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="nav-container">', unsafe_allow_html=True)

    for name, path in PAGES.items():

        active_class = "nav-item nav-active" if name == active_page else "nav-item"

        if st.button(name, key=f"nav_{name}"):
            st.switch_page(path)

        # Purely visual pill
        st.markdown(
            f'<div class="{active_class}">{name}</div>',
            unsafe_allow_html=True
        )

    st.markdown('</div>', unsafe_allow_html=True)


