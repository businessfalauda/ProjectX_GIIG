# storage.py – Simple SQLite storage helper
import sqlite3, datetime, os

DB_PATH = "projectx_data.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS rss_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            title TEXT,
            fetched_at TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS news_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            title TEXT,
            fetched_at TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_rows(table, rows):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.executemany(
        f"INSERT INTO {table}(source,title,fetched_at) VALUES (?,?,?)",
        [(r[0], r[1], datetime.datetime.utcnow().isoformat()) for r in rows]
    )
    conn.commit()
    conn.close()
