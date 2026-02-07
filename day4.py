import sqlite3

conn = sqlite3.connect('data4.db')
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS Teachers(
    name TEXT,
    age INTEGER,
    subject TEXT
)
""")
conn.commit()

def add_teacher(name, age, subject):
    c.execute('INSERT INTO Teachers VALUES(?, ?, ?)', (name, age, subject))
    conn.commit()