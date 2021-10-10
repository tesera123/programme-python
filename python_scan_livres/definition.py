import sqlite3
import requests
from bs4 import BeautifulSoup
import re

def parse_html(variable):
    global result
    reqs = requests.get(variable)
    reqs.content
    recherche_titre = BeautifulSoup(reqs.content, 'html.parser')
    title = recherche_titre.find('title')
    result = re.sub('<title>','', str(title))
    result = re.sub('- Google Livres</title>','', str(result))

def stockage_dans_la_bdd(bdd,line_split,var):
    conn = sqlite3.connect(bdd)
    cursor = conn.cursor()
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {line_split[0]}(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        livres TEXT,
        isbn INTERGER,
        api TEXT
    )
    """)
    data = {"livres" : result, "isbn" : line_split[1], "api" : var}
    cursor.execute(f"""
    INSERT INTO {line_split[0]}(livres, isbn, api) VALUES(:livres, :isbn, :api)""", data)
    conn.commit()