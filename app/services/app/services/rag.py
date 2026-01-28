from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from app.services.embeddings import load_embeddings

vector_db = None

def ingest_file(path: str):
    global vector_db

    loader = TextLoader(path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(docs)

    embeddings = load_embeddings()
    vector_db = FAISS.from_documents(chunks, embeddings)

def query_rag(question: str) -> str:
    if not vector_db:
        return "No documents ingested yet."

    llm = ChatOpenAI(temperature=0)
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vector_db.as_retriever()
    )
    return qa.run(question)
