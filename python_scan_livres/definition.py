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

def creation_de_la_bdd(bdd,line_split):
    global cursor
    global conn
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
    conn.close()

def recherche_et_stockage_bdd(var_bdd):
    global cursor
    global var_verif
    connection = sqlite3.connect(var_bdd)
    cursor = connection.cursor()
    
    MANGA = "SELECT isbn FROM MANGA"
    DC = "select isbn from DC"
    MARVEL = "select isbn from MARVEL"
    recherche = [MANGA,DC,MARVEL] 

    for i in recherche:
        print(i)
        stmt = "SHOW TABLES"
        print(stmt)
        cursor.execute(stmt)
        result = con.fetchone()
        if result:
            print("la table {i} existe bien")
        else:
            print("la table n'existe pas")

def stockage_dans_la_bdd(line_split,var):
    data = {"livres" : result, "isbn" : line_split[1], "api" : var}
    cursor.execute(f"""
    INSERT INTO {line_split[0]}(livres, isbn, api) VALUES(:livres, :isbn, :api)""", data)
    conn.commit()

def recherche_dans_bdd(var_bdd,var_isbn):
    global var_verification
    var_verification = "NEGATIF"
    conn = sqlite3.connect(var_bdd)
    curseur = conn.cursor()

    MANGA = "SELECT isbn FROM MANGA"
    DC = "select isbn from DC"
    MARVEL = "select isbn from MARVEL"
    recherche = [MANGA,DC,MARVEL] 

    for var_recherche in recherche:
        try:
            resultat = curseur.execute(var_recherche)
            print(resultat)
            found = cursor.rowcount
        except:
            break
        if not found:
            break
        else:
            for row in resultat:
                #print(row[0])
                if row[0] == var_isbn:
                    print("livre déja present dans la bdd")
                    var_verification = "POSITIF"
                    break
    return var_verification
    conn.close()