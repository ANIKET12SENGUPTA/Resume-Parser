import fitz  # PyMuPDF
import re


def extract_text(pdf_path: str) -> str:
    """
    Extract text from a PDF with fallbacks for different layouts.
    """

    text_chunks = []

    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:

                page_text = page.get_text("text")

                if not page_text.strip():
                    blocks = page.get_text("blocks")
                    blocks = sorted(blocks, key=lambda b: (b[1], b[0]))
                    page_text = " ".join(block[4] for block in blocks if block[4].strip())

                page_text = re.sub(r'\s+', ' ', page_text)

                text_chunks.append(page_text.strip())

        full_text = "\n".join(text_chunks)
        return full_text

    except Exception:
        return ""