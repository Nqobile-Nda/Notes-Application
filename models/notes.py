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
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    time_created TEXT NOT NULL,
    time_edited NOT NULL
    )
    """)

    conn.close()


def load_notes():
    conn, cur = database_connection()
    cur.execute("SELECT * FROM notes")
    catalog = [dict(row) for row in cur.fetchall()]

    conn.close()
    return catalog



def create_note(title, content, time_created, time_edited):
    conn, cur = database_connection()

    cur.execute("""
    INSERT INTO notes(title, content, time_created, time_edited) VALUES(?,?,?,?)
    """, (title, content, time_created, time_edited))

    conn.commit()
    conn.close()