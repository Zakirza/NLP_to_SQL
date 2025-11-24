# streamlit_app.py
import streamlit as st
import requests
import os

API = os.getenv("API_URL", "http://localhost:8000")

st.title("RAG NLP → SQL Generator (Ollama + FAISS + MySQL)")

if st.button("Ingest Schema"):
    r = requests.post(f"{API}/ingest_schema")
    st.success(r.json())

question = st.text_area("Enter your question:")

if st.button("Generate SQL"):
    r = requests.post(f"{API}/nl2sql", json={"question": question, "execute": False})
    data = r.json()
    st.code(data["sql"], language="sql")
