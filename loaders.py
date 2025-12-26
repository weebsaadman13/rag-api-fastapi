import pdfplumber
import docx
import pandas as pd
import sqlite3
from pathlib import Path
from ocr_utils import ocr_image_file

def load_document(file_path: str) -> str:
    ext = Path(file_path).suffix.lower()

    if ext == ".pdf":
        text = load_pdf(file_path)
        if not text.strip():  # scanned PDF fallback
            return ocr_image_file(file_path)
        return text

    elif ext in [".jpg", ".png", ".jpeg"]:
        return ocr_image_file(file_path)

    elif ext == ".docx":
        return load_docx(file_path)

    elif ext == ".txt":
        return load_txt(file_path)

    elif ext == ".csv":
        return load_csv(file_path)

    elif ext == ".db":
        return load_sqlite(file_path)

    else:
        raise ValueError(f"Unsupported file type: {ext}")


def load_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def load_docx(path):
    document = docx.Document(path)
    return "\n".join([p.text for p in document.paragraphs])

def load_txt(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def load_csv(path):
    df = pd.read_csv(path)
    return df.to_string()

def load_sqlite(path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()

    text = ""
    for table_name in tables:
        table = table_name[0]
        df = pd.read_sql(f"SELECT * FROM {table}", conn)
        text += f"\nTable: {table}\n"
        text += df.to_string()

    conn.close()
    return text
