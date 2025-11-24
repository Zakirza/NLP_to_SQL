# retriever.py
from utils import chunk_text, clean_text
from embedder import get_embedding

def prepare_docs(schema: dict):
    docs = []
    idx = 0
    for table, info in schema.items():
        base = f"TABLE: {table}\nCOLUMNS: " + ", ".join(
            [c['name'] + ':' + c['type'] for c in info['columns']]
        )
        chunks = chunk_text(clean_text(base))
        for c in chunks:
            docs.append({
                "id": idx,
                "text": c,
                "meta": {"table": table, "columns": info["columns"]}
            })
            idx += 1
    return docs

def retrieve(query: str, store):
    q_emb = get_embedding(query)
    hits = store.search(q_emb, k=6)
    schema_text = ""
    for meta, dist in hits:
        cols = ", ".join([c["name"] for c in meta["columns"]])
        schema_text += f"{meta['table']}: {cols}\n"
    return schema_text
