from fastapi import FastAPI, UploadFile, File
import uuid 
import os 
from loaders import load_document
from chunking import chunk_text
from vector_store import create_vector_store
from rag import generate_answer
from pydantic import BaseModel
from typing import Optional

class QueryRequest(BaseModel):
    question: str

app = FastAPI()
VECTOR_DB = None

UPLOAD_DIR = 'uploads'
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get('/')
def health_check():
    return {'msg': 'api is running fine'}

@app.post('/upload')
async def upload_file(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    file_path = os.path.join(UPLOAD_DIR, f"{file_id}_{file.filename}")

    with open(file_path, "wb") as f:
        f.write(await file.read())

    extracted_text = load_document(file_path)
    chunks = chunk_text(extracted_text)

    metadata = [{"source": file.filename}] * len(chunks)

    global VECTOR_DB
    VECTOR_DB = create_vector_store(chunks, metadata)

    return {
        "message": "File is uploaded successfully",
        "file_id": file_id,
        "filename": file.filename,
        "total_chunks": len(chunks),
        "chunk_preview": chunks[0][:300] if chunks else ""
    }

@app.post("/query")
def query_rag(req: QueryRequest):
    if VECTOR_DB is None:
        return {"error": "No documents uploaded yet"}

    docs = VECTOR_DB.similarity_search(req.question, k=4)
    answer = generate_answer(req.question, docs)

    return {
        "question": req.question,
        "answer": answer,
        "sources": [d.metadata for d in docs]
    }
