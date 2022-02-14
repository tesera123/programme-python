import sqlite3
import requests
from bs4 import BeautifulSoup
import re

"""
def parse_html(var,isbn):
    euro = 0
    reqs = requests.get(var)
    reqs.content
    recherche_titre = BeautifulSoup(reqs.content, 'html.parser')
    title = recherche_titre.find('title')
    title = re.sub('<title>','', str(title))
    title = re.sub('</title>','', str(title))
    title = re.sub(f'({isbn})','^_^', str(title))
    print(title)

    table = recherche_titre.find('span', {'class': 'results-price'})
    euro = table.get_text()
    #euro = re.sub('€','', str(euro))
    #print(euro)
"""



def creation_de_la_bdd(bdd,categorie):
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





def recherche_et_stockage_bdd(var_bdd,decoupe_isbn,categorie,var):
    reqs = requests.get(var)
    reqs.content
    recherche_titre = BeautifulSoup(reqs.content, 'html.parser')
    print(recherche_titre)
    
    title = recherche_titre.find('title')
    title = re.sub('<title>','', str(title))
    title = re.sub('</title>','', str(title))
    title = re.sub(f'({decoupe_isbn})','^_^', str(title))
    print(title)

    table = recherche_titre.find('span', {'class': 'results-price'})
    print(table)
    price = table.get_text()
    euro = price.strip()
    #print(euro)

    connection = sqlite3.connect(var_bdd)
    cursor = connection.cursor()
    data = {"livres" : title, "isbn" : decoupe_isbn, "api" : var, "prix": euro }
    cursor.execute(f'SELECT isbn FROM {categorie}')

    r = cursor.fetchall()
    cursor.execute(f'SELECT isbn FROM {categorie} WHERE isbn = "{decoupe_isbn}"')

    a = cursor.fetchall()
    print("valeur de isbn total",r)
    print("valeur d'un isbn",a)

    if not a:
        print("valeur vide")
        cursor.execute(f"""
        INSERT INTO {categorie}(livres, isbn, prix, api) VALUES(:livres, :isbn, :prix, :api)""", data)
        connection.commit()
    else:
        print("valeur pleine, pas d'incrémentation")
    connection.close()








def supression_entree_sqlite3(categorie,bdd,id):
    conn = sqlite3.connect(bdd)
    cur = conn.cursor()
    sql = f"DELETE FROM {categorie} WHERE id = {id}"
    cur.execute(sql)
    conn.commit()