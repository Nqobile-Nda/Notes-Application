import sqlite3

def database_connection():
    conn = sqlite3.connect("notes.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    return conn, cur


def create_notes_table():
    conn, cur = database_connection()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS notes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    content TEXT NOT NULL
    )
    """)

    conn.close()


def create_note(name, content):
    conn, cur = database_connection()

    cur.execute("""
    INSERT INTO notes(name, content) VALUES(?,?)
    """, (name, content))

    conn.commit()
    conn.close()