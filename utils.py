# utils.py
import re
from typing import List

def clean_text(s: str) -> str:
    return re.sub(r'\s+', ' ', s).strip()

def chunk_text(text: str, max_tokens: int = 200, overlap: int = 30):
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = words[i:i + max_tokens]
        chunks.append(" ".join(chunk))
        i += max_tokens - overlap
    return chunks
