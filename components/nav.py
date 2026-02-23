import streamlit as st

def render_nav(active_page: str):

    # ---------- STYLING ----------
    st.markdown("""
    <style>

    /* Hide Sidebar */
    section[data-testid="stSidebar"] {
        display: none;
    }

    section.main > div {
        padding-left: 2rem;
    }

    /* Navigation Row */
    .nav-row {
        margin-bottom: 40px;
    }

    /* Button Base */
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

    div.stButton > button:hover {
        transform: translateY(-3px);
        background: rgba(255,255,255,0.1);
        box-shadow: 0 6px 25px rgba(255, 0, 200, 0.4);
    }

    /* Active Tab */
    .active-tab div.stButton > button {
        background: linear-gradient(90deg, #ff00cc, #3333ff);
        box-shadow:
            0 0 15px rgba(255, 0, 200, 0.6),
            0 0 25px rgba(51, 51, 255, 0.4);
    }

    </style>
    """, unsafe_allow_html=True)

    pages = {
        "Home": "Home.py",
        "EDA Insights": "pages/EDA_Insights.py",
        "Model Training": "pages/Model Training Information.py",
        "Prediction Tool": "pages/Prediction Tool.py",
        "Project Summary": "pages/Project_Summary.py"
    }

    cols = st.columns(len(pages))

    for i, (name, path) in enumerate(pages.items()):
        with cols[i]:

            container_class = "active-tab" if name == active_page else ""
            st.markdown(f'<div class="{container_class}">', unsafe_allow_html=True)

            if st.button(name, key=f"nav_{name}"):
                st.switch_page(path)

            st.markdown('</div>', unsafe_allow_html=True)
