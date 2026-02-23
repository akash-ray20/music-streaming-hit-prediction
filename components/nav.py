import streamlit as st

def render_nav(active_page: str):

    # ---------- STYLING ----------
    st.markdown("""
    <style>
    .nav-container {
        display: flex;
        justify-content: center;
        gap: 14px;
        margin-bottom: 35px;
    }

    div.stButton > button {
        border-radius: 30px;
        padding: 10px 24px;
        background: linear-gradient(145deg, #1a1f2b, #111827);
        color: white;
        font-weight: 500;
        border: none;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
        transition: all 0.25s ease;
    }

    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(255, 0, 200, 0.4);
    }

    .active-tab div.stButton > button {
        background: linear-gradient(90deg, #ff00cc, #3333ff);
        box-shadow: 0 6px 30px rgba(255, 0, 200, 0.6);
    }

    </style>
    """, unsafe_allow_html=True)

    # ---------- NAVIGATION ----------
    pages = {
        "Home": "Home.py",
        "EDA Insights": "pages/EDA_Insights.py",
        "Model Training": "pages/Model_Training_Information.py",
        "Prediction Tool": "pages/Prediction_Tool.py",
        "Project Summary": "pages/Project_Summary.py"
    }

    cols = st.columns(len(pages))

    for i, (name, path) in enumerate(pages.items()):
        with cols[i]:
            container_class = "active-tab" if name == active_page else ""
            st.markdown(f'<div class="{container_class}">', unsafe_allow_html=True)

            if st.button(name):
                st.switch_page(path)

            st.markdown('</div>', unsafe_allow_html=True)