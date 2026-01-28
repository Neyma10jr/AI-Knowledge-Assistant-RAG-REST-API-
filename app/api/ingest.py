from fastapi import APIRouter, UploadFile, File
import os

from app.services.rag import ingest_file

router = APIRouter()
DATA_DIR = "data/docs"
os.makedirs(DATA_DIR, exist_ok=True)

@router.post("/ingest")
async def ingest_document(file: UploadFile = File(...)):
    path = os.path.join(DATA_DIR, file.filename)
    with open(path, "wb") as f:
        f.write(await file.read())

    ingest_file(path)
    return {"message": "Document ingested successfully"}
