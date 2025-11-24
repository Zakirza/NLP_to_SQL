# vector_store.py
import os
import faiss
import numpy as np
import pickle
from embedder import batch_embeddings

INDEX_PATH = os.getenv("VECTORSTORE_PATH", "./vectorstore/faiss_index")
META_PATH = INDEX_PATH + ".pkl"

class FaissVectorStore:
    def __init__(self, dim=384):
        self.dim = dim
        # store metadatas as dict: id -> meta
        self.metadatas = {}
        self._load()

    def _load(self):
        if os.path.exists(INDEX_PATH):
            self.index = faiss.read_index(INDEX_PATH)
            if os.path.exists(META_PATH):
                with open(META_PATH, "rb") as f:
                    self.metadatas = pickle.load(f)
        else:
            quantizer = faiss.IndexFlatL2(self.dim)
            # IndexIDMap expects int64 ids
            self.index = faiss.IndexIDMap(quantizer)

    def _save(self):
        os.makedirs(os.path.dirname(INDEX_PATH), exist_ok=True)
        faiss.write_index(self.index, INDEX_PATH)
        with open(META_PATH, "wb") as f:
            pickle.dump(self.metadatas, f)

    def add(self, docs):
        # docs: list of {"id": int, "text": str, "meta": {...}}
        texts = [d["text"] for d in docs]
        ids = np.array([int(d["id"]) for d in docs], dtype=np.int64)
        embeddings = np.array(batch_embeddings(texts)).astype("float32")
        # ensure shapes align
        if embeddings.shape[0] != ids.shape[0]:
            raise ValueError("Embeddings count and IDs count mismatch")

        self.index.add_with_ids(embeddings, ids)
        for d in docs:
            self.metadatas[int(d["id"])] = d["meta"]
        self._save()

    def search(self, query_embedding, k=5):
        q = np.array([query_embedding]).astype("float32")
        D, I = self.index.search(q, k)
        results = []
        for idx, dist in zip(I[0], D[0]):
            if idx == -1:
                continue
            meta = self.metadatas.get(int(idx))
            results.append((meta, float(dist)))
        return results
