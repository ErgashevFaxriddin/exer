# import sqlite3
#
# conn = sqlite3.connect('data.db')
# c = conn.cursor()
#
# c.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     name TEXT
# )
# """)
#
# conn.commit()
#
# def add_user(name):
#     c.execute("INSERT INTO users VALUES (?)", (name,))
#
#     conn.commit()



import sqlite3

conn = sqlite3.connect('data2.db')
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS students(
    name TEXT,
    age INTEGER
)
""")

conn.commit()

def add_student(name, age):
    c.execute("INSERT INTO students VALUES (?, ?)", (name,age))


















