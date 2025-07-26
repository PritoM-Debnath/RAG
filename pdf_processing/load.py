import pdfplumber
from PIL import Image
import pytesseract
import os

# Set tesseract path manually (only needed on Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # <-- change this path

PDF_PATH = "../data/HSC26-Bangla1st-Paper.pdf"
OUTPUT_PATH = "../data/da-ta.txt"

# Extract each page as image, run OCR in Bangla
ocr_text = []

with pdfplumber.open(PDF_PATH) as pdf:
    for i, page in enumerate(pdf.pages):
        print(f"Processing page {i+1}")
        image = page.to_image(resolution=300).original
        text = pytesseract.image_to_string(image, lang='ben')
        ocr_text.append(text)

# Save result
os.makedirs("../data", exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write("\n\n".join(ocr_text))

print(f"OCR complete. Output saved to: {OUTPUT_PATH}")
