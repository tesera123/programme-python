import sqlite3
import requests
from bs4 import BeautifulSoup
import re



def creation_de_la_bdd(bdd,categorie):
    global cursor
    global conn
    conn = sqlite3.connect(bdd)
    cursor = conn.cursor()
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {categorie}(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        livres TEXT,
        isbn INTERGER,
        prix INTERGER,
        api TEXT
    )
    """)
    conn.close()

def supression_entree_sqlite3(categorie,bdd,id):
    conn = sqlite3.connect(bdd)
    cur = conn.cursor()
    sql = f"DELETE FROM {categorie} WHERE id = {id}"
    cur.execute(sql)
    conn.commit()
    conn.close()