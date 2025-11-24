
# app.py (top)
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

from schema_extractor import extract_schema
from vector_store import FaissVectorStore
from retriever import prepare_docs, retrieve
from sql_generator import generate_sql
from validator import execute_safe

store = FaissVectorStore(dim=384)
app = FastAPI()
...


class Query(BaseModel):
    question: str
    execute: bool = False

@app.post("/ingest_schema")
def ingest():
    try:
        schema = extract_schema()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to extract schema: {e}")
    docs = prepare_docs(schema)
    store.add(docs)
    return {"status": "Schema ingested", "tables": list(schema.keys())}


@app.post("/nl2sql")
def nl2sql(body: Query):
    schema_text = retrieve(body.question, store)
    sql = generate_sql(schema_text, body.question)

    if body.execute:
        result = execute_safe(sql)
        return {"sql": sql, "result": result}

    return {"sql": sql}
