from fastapi import APIRouter
from pydantic import BaseModel

from app.services.rag import query_rag

router = APIRouter()

class Query(BaseModel):
    question: str

@router.post("/ask")
def ask_question(q: Query):
    answer = query_rag(q.question)
    return {"answer": answer}
