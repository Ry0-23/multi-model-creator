import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

def generate_hospitality_content(concept, style):
    # 1. Configure Gemini
    api_key = os.getenv("zaSyCLRcp5rPUwA7VpzeJscaWpoV_4vqhQxSc")
    if not api_key:
        return "Error: GOOGLE_API_KEY not found in .env file.", ""
    
    genai.configure(api_key=api_key)
    model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
    model = genai.GenerativeModel(model_name)

    # 2. Create the prompt for the Narrative
    narrative_prompt = f"Write a professional and descriptive 100-word narrative for a {style} {concept} hospitality project. Focus on atmosphere and design."
    
    # 3. Create the prompt for Image Generation (to be used by your Image API)
    image_prompt = f"High quality architectural photo of a {style} {concept}, photorealistic, 8k, cinematic lighting, interior design magazine style"

    try:
        response = model.generate_content(narrative_prompt)
        return response.text, image_prompt
    except Exception as e:
        return f"Error calling Gemini API: {str(e)}", ""
