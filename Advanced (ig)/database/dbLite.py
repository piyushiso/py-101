import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT
)
""")

cursor.execute("INSERT OR IGNORE INTO students VALUES (1, 'Ram')")

conn.commit()

cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

conn.close()