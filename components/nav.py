import streamlit as st

def render_nav(active_page: str):

    # ---------- STYLING ----------
    st.markdown("""
    <style>

    /* --- Hide Sidebar Completely --- */
    section[data-testid="stSidebar"] {
        display: none;
    }

    section.main > div {
        padding-left: 2rem;
    }

    /* --- Ribbon Wrapper --- */
    .ribbon-wrapper {
        display: flex;
        justify-content: center;
        margin-bottom: 45px;
    }

    /* --- Glass Ribbon Container --- */
    .ribbon {
        display: flex;
        gap: 18px;
        padding: 14px 32px;
        border-radius: 50px;
        backdrop-filter: blur(14px);
        background: rgba(255, 255, 255, 0.05);
        box-shadow:
            0 8px 32px rgba(0,0,0,0.45),
            inset 0 0 40px rgba(255, 0, 200, 0.05);
        border: 1px solid rgba(255,255,255,0.08);
        position: relative;
    }

    /* --- Subtle Neon Accent Line --- */
    .ribbon::before {
        content: "";
        position: absolute;
        top: -1px;
        left: 25%;
        width: 50%;
        height: 2px;
        background: linear-gradient(90deg, #ff00cc, #00f2ff);
        border-radius: 50px;
        filter: blur(4px);
    }

    /* --- Button Base --- */
    div.stButton > button {
        border-radius: 30px;
        padding: 10px 22px;
        background: transparent;
        color: white;
        font-weight: 500;
        border: none;
        transition: all 0.25s ease;
    }

    /* --- Hover Effect --- */
    div.stButton > button:hover {
        transform: translateY(-3px);
        background: rgba(255,255,255,0.08);
    }

    /* --- Active Tab --- */
    .active-tab div.stButton > button {
        background: linear-gradient(90deg, #ff00cc, #3333ff);
        box-shadow:
            0 0 15px rgba(255, 0, 200, 0.6),
            0 0 25px rgba(51, 51, 255, 0.4);
    }

    </style>
    """, unsafe_allow_html=True)

    # ---------- NAVIGATION PAGES ----------
    pages = {
        "Home": "Home.py",
        "EDA Insights": "pages/EDA_Insights.py",
        "Model Training": "pages/Model Training Information.py",
        "Prediction Tool": "pages/Prediction Tool.py",
        "Project Summary": "pages/Project_Summary.py"
    }

    # ---------- RIBBON LAYOUT ----------
    st.markdown('<div class="ribbon-wrapper"><div class="ribbon">', unsafe_allow_html=True)

    cols = st.columns(len(pages))

    for i, (name, path) in enumerate(pages.items()):
        with cols[i]:
            container_class = "active-tab" if name == active_page else ""
            st.markdown(f'<div class="{container_class}">', unsafe_allow_html=True)

            if st.button(name, key=f"nav_{name}"):
                st.switch_page(path)

            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True)
