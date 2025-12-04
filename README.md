# RAG-based NLP → SQL Query Generator

Convert **natural language questions** into **accurate SQL queries** using a Retrieval-Augmented Generation (RAG) pipeline powered by FastAPI, Streamlit, FAISS Vector Store, and Ollama LLM.

---

## Demo Videos

### FastAPI Swagger Demo  
![FastAPI Demo](demo_1.gif)

### Streamlit UI Demo  
![Streamlit Demo](output_videos/streamm.gif)

---

## Overview

This project converts **human natural language** into **SQL queries** using an intelligent Retrieval-Augmented Generation (RAG) architecture.

The system:
- Understands the database schema  
- Retrieves relevant tables/columns using embeddings  
- Generates accurate SQL using an LLM (Ollama LLaMA 3)

---

## Features

- Schema extraction from MySQL  
- Semantic search using FAISS  
- SQL generation using Ollama LLM  
- REST API using FastAPI  
- Interactive UI using Streamlit  
- End-to-end NLP → SQL pipeline  

---

## Architecture  

**User Query → Embeddings → FAISS Vector Store → Retrieved Schema → LLM Prompt → SQL Query**

---

## Components

- Schema Extractor  
- Embedder (MiniLM embeddings)  
- FAISS Vector Store  
- Retriever  
- SQL Generator (Ollama LLaMA 3)  
- FastAPI Backend  
- Streamlit Frontend  

---

## Project Structure

```

├── app.py                 # FastAPI backend
├── streamlit_app.py       # Frontend UI
├── schema_extractor.py    # DB schema ingestion
├── embedder.py            # Embeddings + FAISS
├── sql_generator.py       # LLM prompt + SQL generation
├── vector_store.faiss     # Vector store file
├── requirements.txt       # Dependencies
├── .env                   # Environment variables
└── README.md              # Documentation

````

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/nlp-to-sql.git
cd nlp-to-sql
````

### 2. Create a virtual environment

```bash
python -m venv nlp_env
source nlp_env/Scripts/activate       # Windows
# OR
source nlp_env/bin/activate           # Linux/macOS
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```
DATABASE_URL=mysql://user:password@localhost:3306/yourdb
OLLAMA_BASE_URL=http://localhost:11434
MODEL_NAME=llama3
```

---

## Step 1: Ingest Schema & Build Vector Store

Start FastAPI backend:

```bash
uvicorn app:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

Run the endpoint:

```
POST /ingest_schema
```

This will:

* Extract database schema
* Generate embeddings
* Build FAISS vector store

Index saved as:

```
vector_store.faiss
```

---

## Step 2: Start Streamlit UI

```bash
streamlit run streamlit_app.py
```

### Example queries:

* “Show all employees earning more than 50,000”
* “Get department names and total employees”
* “List orders placed in the last 7 days”

---

## LLM Used

This project uses **Ollama LLaMA 3**.

Start Ollama:

```bash
ollama run llama3
```

You can change the model inside `.env`:

```
MODEL_NAME=llama3
```

---

## Example Query

**Input:**
*Show total salary grouped by department.*

**Output SQL:**

```sql
SELECT department, SUM(salary)
FROM employees
GROUP BY department;
```

---

## Future Improvements

* Schema visualization
* Multi-table join reasoning
* Execute SQL in UI
* PostgreSQL + MongoDB support
* User login + history tracking

---

## License

MIT License

---

## Author

Mohd Zakir

```


