from fastapi import FastAPI
from app.api import ingest, query

app = FastAPI(title="AI Knowledge Assistant")

app.include_router(ingest.router, prefix="/api")
app.include_router(query.router, prefix="/api")

@app.get("/")
def health():
    return {"status": "AI service running"}
