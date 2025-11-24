import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral"  # or llama3

def generate_sql(schema_text: str, question: str) -> str:
    prompt = f"""
You are an expert SQL generator.
Given the database schema and a user question, produce ONLY the SQL query.
Do NOT provide explanations.

SCHEMA:
{schema_text}

QUESTION:
{question}

Return ONLY valid SQL.
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    result = response.json()

    return result.get("response", "")
