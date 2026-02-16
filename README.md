# 🏨 GAI-48 · Multimodal Hospitality Creator

> *Describe a vision. Watch it come to life.*

A multimodal AI application that transforms a single hospitality concept into a full architectural narrative and photorealistic concept art — powered by **Google Gemini** and **Hugging Face Diffusion Models**, built with **Streamlit**.

---

```
╔══════════════════════════════════════════════════════════════╗
║   Input a concept  →  LLM generates narrative + prompt      ║
║   Prompt is passed →  Diffusion model renders concept art    ║
║   Both outputs     →  Displayed side-by-side in the UI      ║
╚══════════════════════════════════════════════════════════════╝
```

---

## ✦ Features

- **✍️ Concept Narration** — Gemini crafts a detailed project narrative from your prompt
- **🖼️ Concept Visualization** — Hugging Face diffusion model renders architectural concept art
- **🏛️ Style Presets** — Choose from Modern, Rustic, Futuristic, or Eco-friendly aesthetics
- **⚡ Real-time Generation** — Spinner feedback during both LLM and image generation steps
- **🎨 Minimal Dark UI** — Custom-themed Streamlit interface with editorial typography

---

## 🗂 Project Structure

```
gai-48-hospitality-creator/
│
├── app.py                   ← Main Streamlit application
├── .env                     ← Environment variables (not committed)
├── .env.example             ← Template for required env vars
├── requirements.txt         ← Python dependencies
│
├── utils/
│   ├── llm_handler.py       ← Gemini API · content + prompt generation
│   └── image_handler.py     ← Hugging Face API · image generation
│
└── README.md
```

---

## ⚙️ Setup & Installation

### 1 · Clone the repository

```bash
git clone https://github.com/your-username/gai-48-hospitality-creator.git
cd gai-48-hospitality-creator
```

### 2 · Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 3 · Install dependencies

```bash
pip install -r requirements.txt
```

### 4 · Configure environment variables

```bash
cp .env.example .env
```

Open `.env` and fill in your keys:

```env
GEMINI_API_KEY=your_google_gemini_api_key_here
HF_API_TOKEN=your_huggingface_api_token_here
```

> 🔑 **Get your keys:**
> - Gemini API → [aistudio.google.com](https://aistudio.google.com)
> - Hugging Face → [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

### 5 · Run the app

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 🔐 Environment Variables

| Variable | Description | Required |
|---|---|---|
| `GEMINI_API_KEY` | Google Gemini API key for LLM calls | ✅ Yes |
| `HF_API_TOKEN` | Hugging Face API token for image generation | ✅ Yes |

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | Streamlit + Custom CSS |
| **LLM** | Google Gemini (via `google-generativeai`) |
| **Image Generation** | Hugging Face Inference API |
| **Env Management** | `python-dotenv` |
| **Language** | Python 3.9+ |

---

## 🚀 Usage

1. Launch the app with `streamlit run app.py`
2. *(Optional)* Open the sidebar to choose an **Architectural Style**
3. Type your hospitality concept in the input field
   ```
   e.g. "A luxury treehouse resort nestled in the rainforests of Kerala"
   e.g. "A minimalist cliffside retreat in the Amalfi Coast"
   e.g. "A futuristic underwater hotel near the Maldives"
   ```
4. Click **Generate Concept**
5. Wait for the narrative and concept art to render side-by-side

---

## 📋 Requirements

```txt
streamlit
google-generativeai
requests
Pillow
python-dotenv
```

> Generate a full `requirements.txt` with: `pip freeze > requirements.txt`

---

## ⚠️ Known Limitations

- Image generation time depends on Hugging Face Inference API availability and model load
- Gemini free-tier has rate limits; responses may slow under heavy usage
- The app currently does not persist generated outputs between sessions

---

## 👥 Team

| Role | Details |
|---|---|
| **Project** | GAI-48 · Generative AI Applications |
| **Group** | 12D4 |

---

## 📄 License

This project was developed as part of an academic assignment. All rights reserved by the respective contributors.

---

<div align="center">

*Built with curiosity, caffeine, and a lot of API calls.*

`GAI-48` · `Group 12D4` · `Multimodal AI`

</div>
