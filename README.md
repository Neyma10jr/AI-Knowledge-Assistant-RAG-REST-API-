# AI Knowledge Assistant

A production-style AI application built using Python, FastAPI, and LangChain that enables document-based question answering using Retrieval-Augmented Generation (RAG).

## Features
- Document ingestion and chunking
- Vector similarity search with FAISS
- LLM-powered question answering
- REST APIs for ingestion and querying

## Tech Stack
- Python
- FastAPI
- LangChain
- OpenAI
- FAISS

## Use Case
Enterprise knowledge assistants, internal documentation search, AI-powered helpdesks.
how to run:
pip install -r requirements.txt
uvicorn app.main:app --reload

