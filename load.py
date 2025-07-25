import pdfplumber
import unicodedata

with pdfplumber.open("data/HSC26-Bangla1st-Paper.pdf") as pdf:
    raw_text = "\n".join([p.extract_text() for p in pdf.pages if p.extract_text()])

normalized_text = unicodedata.normalize("NFC", raw_text)

with open("output_bangla.txt", "w", encoding="utf-8") as f:
    f.write(normalized_text)

