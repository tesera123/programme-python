import sqlite3
import requests
from bs4 import BeautifulSoup
import re
import json

def parse_html(var):
    global result
    reqs = requests.get(var)
    reqs.content
    recherche_titre = BeautifulSoup(reqs.content, 'html.parser')
    title = recherche_titre.find('title')
    result = re.sub('<title>','', str(title))
    result = re.sub('- Google Livres</title>','', str(result))

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
        api TEXT
    )
    """)
    conn.close()

def recherche_et_stockage_bdd(var_bdd,decoupe_isbn,categorie,var):
    global cursor
    global var_verif
    connection = sqlite3.connect(var_bdd)
    cursor = connection.cursor()
    data = {"livres" : result, "isbn" : decoupe_isbn, "api" : var}
    cursor.execute(f'SELECT isbn FROM {categorie}')
    r = cursor.fetchall()
    cursor.execute(f'SELECT isbn FROM {categorie} WHERE isbn = "{decoupe_isbn}"')
    a = cursor.fetchall()
    print("valeur de isbn total",r)
    print("valeur d'un isbn",a)

    if not a:
        print("valeur vide")
        cursor.execute(f"""
        INSERT INTO {line_split[0]}(livres, isbn, api) VALUES(:livres, :isbn, :api)""", data)
        connection.commit()
    else:
        print("valeur pleine, pas d'incrémentation")
    connection.close()


def stockage_dans_la_bdd(line_split,var,var_bdd):
    conn = sqlite3.connect(var_bdd)
    cursor = conn.cursor()
    data = {"livres" : result, "isbn" : line_split[1], "api" : var}
    cursor.execute(f"""
    INSERT INTO {line_split[0]}(livres, isbn, api) VALUES(:livres, :isbn, :api)""", data)
    conn.commit()
    conn.close()