# RAG-based NLP → SQL Query Generator

A small, production-minded reference implementation of a Retrieval-Augmented Generation pipeline that converts natural language questions to SQL queries grounded on a real database schema.

## Features
- Extracts schema + sample rows from Postgres
- Indexes schema chunks into a FAISS vectorstore
- Uses embeddings (OpenAI or Sentence-Transformers)
- LLM-based SQL generation with strict "use only provided schema" prompt
- Optional safe, read-only SQL execution
- Streamlit demo UI + FastAPI backend

## Quickstart (local)
1. Copy `.env.example` → `.env` and fill values.
2. Create a virtualenv and install deps:
   ```bash
   pip install -r requirements.txt

 # NLP_to-_SQL
