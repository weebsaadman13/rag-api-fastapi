# RAG API - Retrieval-Augmented Generation API

A **smart API** built with **FastAPI** that can answer questions based on content from any document type — including PDFs, Word files, images (OCR), .txt, CSVs, and SQLite databases. It uses **vector embeddings** and **LLMs** (OpenAI, Claude, etc.) to generate accurate, context-aware answers.

---

## Features

- Upload and process multiple document types:
  - `.pdf` (text + scanned)
  - `.docx`
  - `.txt`
  - `.jpg` / `.png` (OCR via `pytesseract`)
  - `.csv` / `.db` (via `pandas` / `sqlite3`)
- Text preprocessing with chunking for better embeddings
- Embeddings stored in **FAISS** vector store
- Question answering via `/query` endpoint
- Returns:
  - Context
  - Final Answer
  - Source info (page, file, chunk index)
- Optional:
  - Multimodal queries (text + image)
  - Multi-document queries
  - Dockerized deployment
  - Minimal frontend via Streamlit

---

## Tech Stack

- **Backend:** Python, FastAPI, async/await
- **Vector Storage:** FAISS (or ChromaDB)
- **OCR:** pytesseract, easyocr
- **Document Parsers:** pdfplumber, python-docx, pandas
- **Embeddings:** OpenAI or HuggingFace (`all-MiniLM`)
- **LLM API:** OpenAI GPT, Claude, or HuggingFace Hub
- **Containerization (optional):** Docker
- **Frontend (optional):** Streamlit

---

## Setup

1. **Clone the repo**

```bash
git clone https://github.com/your-username/rag-api-fastapi.git
cd rag-api-fastapi
