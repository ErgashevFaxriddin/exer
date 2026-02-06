import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users (
    name TEXT
)
""")

conn.commit()

def add_user(name):
    c.execute("INSERT INTO users VALUES (?)", (name,))

    conn.commit()
