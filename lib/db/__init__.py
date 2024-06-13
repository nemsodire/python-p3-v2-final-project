import sqlite3

DATABASE_URL = "legal_system.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE_URL)
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lawyer (
            id INTEGER PRIMARY KEY,
            name VARCHAR,
            specialty VARCHAR,
            created_at TIMESTAMP
    )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cases (
            id INTEGER PRIMARY KEY,
            title VARCHAR,
            description TEXT,
            lawyer_id INTEGER,
            status VARCHAR,
            created_at TIMESTAMP
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS client (
            id INTEGER PRIMARY KEY,
            name VARCHAR,
            contact_info VARCHAR,
            lawyer_id INTEGER,
            created_at TIMESTAMP
        )
    """)
    conn.commit()
    
from .config import get_db_connection
