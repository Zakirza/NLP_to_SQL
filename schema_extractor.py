# schema_extractor.py
import os
import mysql.connector
import json
from dotenv import load_dotenv
from urllib.parse import urlparse, unquote

load_dotenv()

DB_URL = os.getenv("DATABASE_URL")
if not DB_URL:
    raise ValueError("DATABASE_URL not set in .env (expected format mysql://user:pass@host:port/dbname)")

def parse_database_url(url: str):
    # use urllib to parse reliably
    parsed = urlparse(url)
    if parsed.scheme != "mysql":
        raise ValueError("DATABASE_URL must start with mysql://")
    user = parsed.username or ""
    password = parsed.password or ""
    host = parsed.hostname or "localhost"
    port = parsed.port or 3306
    db = parsed.path.lstrip("/") or ""
    # decoded password (handles %40, %3A etc.)
    return user, unquote(password), host, port, db

def get_conn():
    user, password, host, port, db = parse_database_url(DB_URL)
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        port=port,
        database=db
    )

def extract_schema(sample_rows=3):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SHOW TABLES;")
    tables = [row[0] for row in cur.fetchall()]
    
    schema = {}
    for table in tables:
        cur.execute(f"DESCRIBE `{table}`;")
        columns = [{"name": c[0], "type": c[1]} for c in cur.fetchall()]

        cur.execute(f"SELECT * FROM `{table}` LIMIT {sample_rows};")
        rows = cur.fetchall()

        schema[table] = {
            "columns": columns,
            "samples": rows
        }

    cur.close()
    conn.close()
    return schema
