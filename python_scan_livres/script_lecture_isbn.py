import os
import requests
import json
import requests as req
import re
import sqlite3

from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup


#chemin_classique
chemin_repertoire_git = os.getcwd()
chemin_windows = f"{chemin_repertoire_git}\python_scan_livres"
var_fichier = "livres.txt"
os.chdir(chemin_windows) 
arr = os.listdir('.')
api_key = "AIzaSyDQCmVtPm4rWhmRrIvonLuy8SS3-rjJQO0"
conn = sqlite3.connect('ma_base.db')
file = open('livres.txt', "r")

with open("livres.txt", 'r') as f:
    for line in f:
    #for line in lines:
        print(line)
        line_split = line.split("-")
        print(line_split)

        reponse_api = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{line_split[1]}&key={api_key}"
        res = requests.get(reponse_api)
        data = res.json()

        with open('lecture_php.json', 'w') as f:
            json.dump(data, f)

        json_data = open(r'lecture_php.json').read()
        data = json.loads(json_data)
        print(data.keys())
        test = data['items']
        for elt in test:
            var = elt['volumeInfo']['infoLink']

        reqs = requests.get(var)
        reqs.content
        recherche_titre = BeautifulSoup(reqs.content, 'html.parser')
        title = recherche_titre.find('title')
        print(title)
        result = re.sub('<title>','', str(title))
        result = re.sub('- Google Livres</title>','', str(result))
        print(result)

        conn = sqlite3.connect('ma_base.db')
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


        line = file.readline()
    file.close()