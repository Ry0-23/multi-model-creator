import streamlit as st
import os
from dotenv import load_dotenv
from utils.llm_handler import generate_hospitality_content
from utils.image_handler import generate_resort_image

# Load environment variables
load_dotenv()

# Page Config
st.set_page_config(page_title="GAI-48: Hospitality Creator", layout="wide")

# Header
st.title("🏨 Multimodal Hospitality Creator")
st.markdown("**Project GAI-48 | Group 12D4**")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("Project Controls")
    st.info("Ensure GOOGLE_API_KEY and HUGGINGFACE_API_TOKEN are set in .env")
    style_preset = st.selectbox("Architectural Style", ["Modern", "Rustic", "Futuristic", "Eco-friendly"])

# Main Input
concept = st.text_input("Enter your Hospitality Concept:", placeholder="e.g., A luxury treehouse resort in Kerala")

if st.button("Generate Concept"):
    if not concept:
        st.warning("Please enter a concept first.")
    else:
        with st.spinner("consulting AI Architects (Gemini)..."):
            # Call LLM
            description, image_prompt = generate_hospitality_content(concept, style_preset)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("Concept Visualization")
            with st.spinner("Rendering Visuals (Hugging Face)..."):
                if not image_prompt:
                    st.error("Image prompt not generated (LLM call likely failed).")
                else:
                    try:
                        image = generate_resort_image(image_prompt)
                        st.image(image, caption="Generated Concept Art")
                    except Exception as e:
                        st.error(f"Image generation failed: {e}")
        
        with col2:
            st.subheader("Project Narrative")
            if isinstance(description, str) and description.startswith("Error:"):
                st.error(description)
            else:
                st.write(description)
