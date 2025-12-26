
# RAG API - Retrieval‑Augmented Generation API

A **smart API** built with **FastAPI** that can answer questions based on content from various document types — including PDFs, Word files, text, CSV/SQLite, and images (OCR) — using vector embeddings and LLMs.

---

## 📌 Features

- Upload and process:
  - `.pdf` (including scanned with OCR)
  - `.docx`
  - `.txt`, `.csv`, `.db`
  - Image files (`.jpg`, `.png`)
- Text chunking for better embedding quality
- Embeddings stored in FAISS vector store
- `/upload` endpoint for file ingestion
- `/query` endpoint for natural language questions
- Returns context, answer, and source info
- Docker support for easy setup  
*(based on your repository structure)*:contentReference[oaicite:1]{index=1}

---

## 🧰 Tech Stack

- **Python** + **FastAPI**
- **FAISS** vector store
- **OCR:** `pytesseract`
- **Parsers:** `pdfplumber`, `python‑docx`, `pandas`
- **Embeddings & LLM:** OpenAI or similar
- **Containerization:** Docker  
*(files: `main.py`, `rag.py`, `vector_store.py`, `ocr_utils.py`)*:contentReference[oaicite:2]{index=2}

---

## 🚀 Step‑by‑Step Setup

### 1) Clone the Repository

```bash
git clone https://github.com/weebsaadman13/rag-api-fastapi.git
cd rag-api-fastapi
