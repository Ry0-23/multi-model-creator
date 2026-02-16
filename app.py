import streamlit as st
import os
from dotenv import load_dotenv
from utils.llm_handler import generate_hospitality_content
from utils.image_handler import generate_resort_image

# Load environment variables
load_dotenv()

# Page Config
st.set_page_config(page_title="GAI-48: Hospitality Creator", layout="wide", initial_sidebar_state="collapsed")

# ─── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300&family=DM+Sans:wght@300;400;500&display=swap');

/* ── Reset & Base ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"] {
    background-color: #0d0d0d !important;
    color: #e8e0d5 !important;
    font-family: 'DM Sans', sans-serif;
    font-weight: 300;
}

[data-testid="stAppViewContainer"] > .main {
    background-color: #0d0d0d !important;
}

[data-testid="stHeader"] {
    background-color: #0d0d0d !important;
    border-bottom: 1px solid #1e1e1e;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background-color: #111111 !important;
    border-right: 1px solid #1e1e1e !important;
}

[data-testid="stSidebar"] * {
    color: #b0a898 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 300 !important;
}

[data-testid="stSidebar"] .stSelectbox label {
    font-size: 0.7rem !important;
    letter-spacing: 0.15em !important;
    text-transform: uppercase !important;
    color: #5a5550 !important;
}

/* ── Main container ── */
.block-container {
    max-width: 1100px !important;
    padding: 3rem 2.5rem !important;
}

/* ── Header ── */
.site-header {
    display: flex;
    align-items: baseline;
    gap: 1rem;
    margin-bottom: 0.25rem;
}

.site-title {
    font-family: 'Cormorant Garamond', serif;
    font-weight: 300;
    font-size: 2.6rem;
    color: #e8e0d5;
    letter-spacing: -0.01em;
    line-height: 1;
}

.site-badge {
    font-size: 0.65rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #5a5550;
    font-weight: 400;
    padding: 0.2rem 0.6rem;
    border: 1px solid #2a2a2a;
    border-radius: 2px;
}

.site-divider {
    height: 1px;
    background: linear-gradient(to right, #2a2a2a 60%, transparent);
    margin: 1.5rem 0 2.5rem;
}

/* ── Input label ── */
.input-label {
    font-size: 0.68rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #5a5550;
    margin-bottom: 0.5rem;
    display: block;
}

/* ── Streamlit input override ── */
[data-testid="stTextInput"] > div > div > input {
    background: #111111 !important;
    border: 1px solid #2a2a2a !important;
    border-radius: 3px !important;
    color: #e8e0d5 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.95rem !important;
    font-weight: 300 !important;
    padding: 0.75rem 1rem !important;
    transition: border-color 0.2s ease !important;
}

[data-testid="stTextInput"] > div > div > input:focus {
    border-color: #c9a96e !important;
    box-shadow: none !important;
    outline: none !important;
}

[data-testid="stTextInput"] > div > div > input::placeholder {
    color: #3a3530 !important;
}

[data-testid="stTextInput"] label {
    display: none !important;
}

/* ── Button ── */
[data-testid="stButton"] > button {
    background: transparent !important;
    border: 1px solid #c9a96e !important;
    color: #c9a96e !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.7rem !important;
    font-weight: 400 !important;
    letter-spacing: 0.2em !important;
    text-transform: uppercase !important;
    padding: 0.65rem 1.8rem !important;
    border-radius: 2px !important;
    transition: all 0.25s ease !important;
    margin-top: 0.5rem !important;
}

[data-testid="stButton"] > button:hover {
    background: #c9a96e !important;
    color: #0d0d0d !important;
}

/* ── Section headers ── */
h3, .stSubheader {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 1.4rem !important;
    font-weight: 300 !important;
    color: #e8e0d5 !important;
    letter-spacing: 0.02em !important;
    margin-bottom: 1rem !important;
}

/* ── Narrative text ── */
[data-testid="stText"], .stMarkdown p, .stWrite {
    font-size: 0.9rem !important;
    line-height: 1.8 !important;
    color: #b0a898 !important;
}

/* ── Image ── */
[data-testid="stImage"] img {
    border-radius: 3px !important;
    border: 1px solid #1e1e1e !important;
    width: 100% !important;
}

[data-testid="stImage"] > div > div > p {
    font-size: 0.68rem !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    color: #3a3530 !important;
    margin-top: 0.5rem !important;
    text-align: center !important;
}

/* ── Spinner ── */
[data-testid="stSpinner"] > div > div {
    border-top-color: #c9a96e !important;
}

[data-testid="stSpinner"] p {
    color: #5a5550 !important;
    font-size: 0.78rem !important;
    letter-spacing: 0.08em !important;
}

/* ── Alerts ── */
[data-testid="stAlert"] {
    background: #111111 !important;
    border: 1px solid #2a2a2a !important;
    border-radius: 3px !important;
    color: #b0a898 !important;
    font-size: 0.85rem !important;
}

/* ── Column gap ── */
[data-testid="column"] {
    padding: 0 1rem !important;
}

/* ── Selectbox ── */
[data-testid="stSelectbox"] > div > div {
    background: #111111 !important;
    border: 1px solid #2a2a2a !important;
    border-radius: 3px !important;
    color: #b0a898 !important;
    font-size: 0.85rem !important;
}

/* ── Result section separator ── */
.result-divider {
    height: 1px;
    background: #1e1e1e;
    margin: 2rem 0;
}

/* ── Style tag in sidebar ── */
.sidebar-tag {
    font-size: 0.65rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #3a3530;
    margin-bottom: 1.5rem;
    display: block;
}

/* Hide streamlit branding & default elements */
#MainMenu, footer, [data-testid="stDeployButton"] { display: none !important; }
[data-testid="stDecoration"] { display: none !important; }
.stTextInput > label { display: none !important; }
</style>
""", unsafe_allow_html=True)

# ─── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<span class="sidebar-tag">Configuration</span>', unsafe_allow_html=True)
    st.markdown('<span class="input-label">Architectural Style</span>', unsafe_allow_html=True)
    style_preset = st.selectbox(
        "Architectural Style",
        ["Modern", "Rustic", "Futuristic", "Eco-friendly"],
        label_visibility="collapsed"
    )

# ─── Header ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="site-header">
    <span class="site-title">Multi-Modal Hospitality Creator</span>
    <span class="site-badge">GAI-48 · Group 12D4</span>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="site-divider"></div>', unsafe_allow_html=True)

# ─── Main Input ───────────────────────────────────────────────────────────────
st.markdown('<span class="input-label">Concept</span>', unsafe_allow_html=True)
concept = st.text_input(
    "concept",
    placeholder="e.g., A luxury treehouse resort in Kerala",
    label_visibility="collapsed"
)

if st.button("Generate Concept"):
    if not concept:
        st.warning("Please enter a concept to continue.")
    else:
        st.markdown('<div class="result-divider"></div>', unsafe_allow_html=True)

        with st.spinner("Consulting AI Architects…"):
            description, image_prompt = generate_hospitality_content(concept, style_preset)

        col1, col2 = st.columns([1, 1], gap="large")

        with col1:
            st.subheader("Visualization")
            with st.spinner("Rendering concept art…"):
                if not image_prompt:
                    st.error("Image prompt not generated — LLM call may have failed.")
                else:
                    try:
                        image = generate_resort_image(image_prompt)
                        st.image(image, caption="AI-Generated Concept Art")
                    except Exception as e:
                        st.error(f"Image generation failed: {e}")

        with col2:
            st.subheader("Narrative")
            if isinstance(description, str) and description.startswith("Error:"):
                st.error(description)
            else:
                st.write(description)