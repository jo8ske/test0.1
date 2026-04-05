import pytesseract
from PIL import Image

def extract_text(path: str) -> str:
    img = Image.open(path)
    return pytesseract.image_to_string(img)
