from huggingface_hub import InferenceClient
from PIL import Image
import io
import os

def generate_resort_image(prompt):
    token = os.getenv("HUGGINGFACE_API_TOKEN")
    if not token:
        raise ValueError("HUGGINGFACE_API_TOKEN not found in .env file.")

    model = os.getenv("HF_IMAGE_MODEL", "stabilityai/stable-diffusion-xl-base-1.0")
    client = InferenceClient(model=model, token=token)

    result = client.text_to_image(prompt)

    # huggingface_hub may return a PIL Image, bytes, or a file-like object depending on version/config.
    if isinstance(result, Image.Image):
        return result
    if isinstance(result, (bytes, bytearray)):
        return Image.open(io.BytesIO(result)).convert("RGB")
    if hasattr(result, "read"):
        return Image.open(io.BytesIO(result.read())).convert("RGB")

    raise TypeError(f"Unexpected image result type: {type(result)}")
