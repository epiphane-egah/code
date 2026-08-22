"""
Docs-style sidebar demo, similar to GitBook/Docusaurus nav.

Install requirements first:
    pip install streamlit streamlit-option-menu
Run with:
    streamlit run sidebar_demo.py
"""

import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Docs Sidebar Demo", layout="wide")

# ---------------------------------------------------------------------------
# 1. Global CSS: dark navy sidebar background + section-title styling
#    (top-level "DE Zoomcamp" / "DE Zoomcamp 2024" rows in the screenshot)
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
    /* Sidebar background */
    section[data-testid="stSidebar"] {
        background-color: #2b2d52;
    }

    /* Section header rows (non-clickable groupings) */
    .sidebar-section {
        color: #d7d9f5;
        font-size: 15px;
        font-weight: 600;
        padding: 6px 4px 6px 4px;
        margin-top: 4px;
    }
    .sidebar-subsection {
        color: #d7d9f5;
        font-size: 15px;
        font-weight: 600;
        padding: 4px 4px 4px 20px;
        margin-top: 2px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# 2. Sidebar content
# ---------------------------------------------------------------------------
with st.sidebar:
    # Top-level, non-nested "header" rows (like "DE Zoomcamp")
    st.markdown('<div class="sidebar-section">💻 DE Zoomcamp</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-section">🧙 DE Zoomcamp 2024</div>', unsafe_allow_html=True)

    # Indented, clickable nav items (the numbered modules) using option_menu
    selected = option_menu(
        menu_title=None,               # no title, just the list
        options=[
            "Course Overview",
            "Module 1 Introduction & Prereq",
            "Module 2 Workflow Orchestration",
            "Workshop 1 Data Ingestion",
            "Module 3 Data Warehouse and BI",
            "Module 4 Analytics Engineering",
            "Module 5 Batch Processing",
            "Workshop 2 Stream Processing",
            "Module 6 Stream Processing",
            "Course Project",
            "Datasets",
            "Certificate",
            "FAQ",
            "Contact",
            "About",
        ],
        icons=[
            "book", "1-circle-fill", "2-circle-fill", "tools",
            "3-circle-fill", "4-circle-fill", "5-circle-fill", "tools",
            "6-circle-fill", "trophy", "save", "scroll",
            "question-circle", "envelope", "image",
        ],
        menu_icon=None,
        default_index=10,  # highlight "Datasets" like the screenshot
        styles={
            "container": {"padding": "0!important", "background-color": "#2b2d52"},
            "icon": {"color": "#d7d9f5", "font-size": "16px"},
            "nav-link": {
                "font-size": "15px",
                "color": "#d7d9f5",
                "text-align": "left",
                "margin": "2px 0px",
                "padding-left": "20px",   # indentation to mimic nested items
                "--hover-color": "#3a3d6b",
            },
            "nav-link-selected": {
                "background-color": "#454880",  # highlighted active row
                "color": "#ffffff",
                "font-weight": "600",
            },
        },
    )

# ---------------------------------------------------------------------------
# 3. Main page content reacts to the sidebar selection
# ---------------------------------------------------------------------------
st.title(selected)
st.write(f"You selected: **{selected}**")