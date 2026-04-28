import fitz
import pytesseract
from PIL import Image
import io
import os
import sys

PDF = "Dashvaikalik Sutra.pdf"
OUT = "Dashvaikalik Sutra.ocr.txt"
PROGRESS = "ocr.progress"

doc = fitz.open(PDF)
total = len(doc)
print(f"OCR'ing {total} pages...")

start = 0
if os.path.exists(PROGRESS):
    with open(PROGRESS) as f:
        start = int(f.read().strip())
    print(f"Resuming from page {start+1}")

mode = "a" if start > 0 else "w"
with open(OUT, mode, encoding="utf-8") as out:
    for i in range(start, total):
        page = doc[i]
        pix = page.get_pixmap(dpi=300)
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        text = pytesseract.image_to_string(img, lang="guj+san+eng")
        out.write(f"\n\n========== PAGE {i+1} ==========\n\n{text}")
        out.flush()
        with open(PROGRESS, "w") as p:
            p.write(str(i+1))
        if (i+1) % 5 == 0:
            print(f"  page {i+1}/{total}", flush=True)

print("Done.")
