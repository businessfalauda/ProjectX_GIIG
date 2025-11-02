# storage.py
import sqlite3, os

DB_PATH = os.getenv("DB_PATH", "projectx.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""CREATE TABLE IF NOT EXISTS statements(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        platform TEXT,
        entity TEXT,
        text TEXT,
        url TEXT,
        fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized:", DB_PATH)
