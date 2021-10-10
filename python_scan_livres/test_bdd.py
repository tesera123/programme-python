import sqlite3

conn = sqlite3.connect('ma_base.db')

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS BDD_livres(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     livres TEXT,
     isbn INTERGER,
     api TEXT
)
""")
data = {"livres" : "my hero academia", "isbn" : 30, "api" : "test"}
cursor.execute("""
INSERT INTO BDD_livres(livres, isbn, api) VALUES(:livres, :isbn, :api)""", data)
conn.commit()