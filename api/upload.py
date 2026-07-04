from fastapi import APIRouter, UploadFile, File
import shutil
import os

from rag.indexer import index_pdf

router = APIRouter()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files are allowed"}

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    chunks = index_pdf(file_path)
    stats = index_pdf(file_path)
    
    return {
        "message": "Document indexed successfully",
        "filename": file.filename,
        "pages": stats["pages"],
        "chunks_created": stats["chunks"]
    }
    