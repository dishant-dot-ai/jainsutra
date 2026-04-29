"""Extract Anuttarovavai.pdf to plain UTF-8 text.

Matches the convention used in scripture/Aagama/sutrakritang/source — a flat
Source folder holding the PDF alongside its plain-text counterpart.

Usage:
    python3 extract_pdf.py
"""

from pathlib import Path

import fitz  # PyMuPDF

HERE = Path(__file__).resolve().parent
PDF = HERE / "Anuttarovavai.pdf"
OUT = HERE / "anuttarovavai_text.txt"


def extract() -> None:
    doc = fitz.open(PDF)
    parts = []
    for i, page in enumerate(doc, start=1):
        text = page.get_text("text")
        parts.append(f"\n\n========== PAGE {i} ==========\n\n{text}")
    OUT.write_text("".join(parts), encoding="utf-8")
    print(f"Extracted {len(doc)} pages -> {OUT}")


if __name__ == "__main__":
    extract()
