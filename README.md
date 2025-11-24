
```markdown
# 🚀 RAG-based NLP → SQL Query Generator  
Convert **natural language questions** into **accurate SQL queries** using a **Retrieval-Augmented Generation (RAG)** pipeline powered by FastAPI, Streamlit, FAISS Vector Store, and Ollama LLM.

---

## 🎥 Demo Videos

### 🔹 FastAPI Swagger Demo  
![FastAPI Demo](demo_1.gif)

### 🔹 Streamlit UI Demo  
![Streamlit Demo](output_videos/streamm.gif)

---

## 📌 Overview

This project converts **human natural language** into **SQL queries** using an intelligent RAG architecture.  
The system understands database schema, retrieves relevant table/column information using embeddings, and generates accurate SQL using an LLM.

### ✅ Features
- 📄 Schema extraction from MySQL  
- 🧠 Semantic search using FAISS  
- 🤖 SQL generation using Ollama LLM  
- 🔌 REST API using FastAPI  
- 🖥️ Interactive UI using Streamlit  
- ⚡ End-to-end NLP → SQL pipeline  

---

## 🏗️ Architecture

```

User Query → Embeddings → FAISS Vector Store → Retrieved Schema → LLM Prompt → SQL Query

```

### 🧩 Components
- **Schema Extractor** → Reads DB schema + sample rows  
- **Embedder** → Converts schema to embeddings (MiniLM)  
- **Vector Database (FAISS)** → Stores embeddings  
- **Retriever** → Finds top relevant columns/tables  
- **Generator** → LLaMA 3 via Ollama produces SQL  
- **API** → FastAPI backend  
- **UI** → Streamlit interface  

---

## 📂 Project Structure

```

├── app.py                # FastAPI backend
├── streamlit_app.py      # Frontend UI
├── schema_extractor.py   # DB schema ingestion
├── embedder.py           # Embeddings + FAISS
├── sql_generator.py      # LLM prompt + SQL generation
├── vector_store.faiss    # Vector store file
├── .env                  # Environment variables
└── README.md             # Documentation

````

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/nlp-to-sql.git
cd nlp-to-sql
````

### 2️⃣ Create virtual environment

```bash
python -m venv nlp_env
source nlp_env/Scripts/activate   # Windows
# or
source nlp_env/bin/activate       # Linux / macOS
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file:

```
DATABASE_URL=mysql://user:password@localhost:3306/yourdb
OLLAMA_BASE_URL=http://localhost:11434
MODEL_NAME=llama3
```

---

## 🧩 Step 1: Ingest Schema & Build Vector Store

Run FastAPI backend:

```bash
uvicorn app:app --reload
```

Open:
➡️ [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Then click:

```
POST /ingest_schema
```

This will:

* Extract database schema
* Generate embeddings
* Build FAISS vector store

Your vector DB will be saved as:

```
vector_store.faiss
```

---

## 🎯 Step 2: Start Streamlit UI

```bash
streamlit run streamlit_app.py
```

Now you can ask natural language questions like:

* *"Show all employees earning more than 50,000"*
* *"Get department names and total employees"*
* *"List orders placed in the last 7 days"*

---

## 🧠 LLM Used

This project uses **Ollama LLaMA 3** by default.

Start Ollama:

```bash
ollama run llama3
```

Change model in `.env`:

```
MODEL_NAME=llama3
```

---

## 📝 Example Query

**Input:**

```
Show total salary grouped by department.
```

**Output SQL:**

```sql
SELECT department, SUM(salary)
FROM employees
GROUP BY department;
```

---

## 🔮 Future Improvements

* Schema relationship visualization
* Multi-table join reasoning
* Execute SQL directly from UI
* Support PostgreSQL, MongoDB
* Authentication & user history tracking

---

## 📜 License

MIT License

---

## 👨‍💻 Author

**Mohd Zakir**

If you need:

* A project logo
* Architecture diagram
* Deployment (Docker, Railway, Render, HuggingFace Spaces)

Just let me know!

```
