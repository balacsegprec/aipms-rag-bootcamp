import pdfplumber


def load_pdf(file_path):
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    if not text.strip():
        raise ValueError("No text extracted from PDF.")

    return text


def split_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0

    text = text.strip()

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        if chunk.strip():
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks