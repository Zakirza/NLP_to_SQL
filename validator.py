# validator.py
import os
import mysql.connector
import sqlparse
from dotenv import load_dotenv
from urllib.parse import urlparse, unquote

load_dotenv()

DB_URL = os.getenv("DATABASE_URL")
if not DB_URL:
    raise ValueError("DATABASE_URL not set in .env")

def parse_database_url(url: str):
    parsed = urlparse(url)
    user = parsed.username or ""
    password = parsed.password or ""
    host = parsed.hostname or "localhost"
    port = parsed.port or 3306
    db = parsed.path.lstrip("/") or ""
    return user, unquote(password), host, port, db

def get_conn():
    user, password, host, port, db = parse_database_url(DB_URL)
    return mysql.connector.connect(host=host, port=port, user=user, password=password, database=db)

def execute_safe(sql):
    if not sql or not sql.strip().lower().startswith("select"):
        return {"error": "Only SELECT queries are allowed"}

    conn = get_conn()
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    cols = [c[0] for c in cur.description]
    cur.close()
    conn.close()

    return {"columns": cols, "rows": rows}
