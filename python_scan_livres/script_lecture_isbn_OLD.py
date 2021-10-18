import os
import json
import requests
import sqlite3

from os import listdir
from bs4 import BeautifulSoup
from definition import *
# ***************** CHEMIN DE BASE ***************** 
chemin_repertoire_git = os.getcwd()
chemin_windows = f"{chemin_repertoire_git}\python_scan_livres"
os.chdir(chemin_windows) 
arr = os.listdir('.')


# ***************** clé et fichier de reference ***************** 
api_key = "AIzaSyDQCmVtPm4rWhmRrIvonLuy8SS3-rjJQO0"
conn = sqlite3.connect('ma_base.db')
bdd = 'ma_base.db'
var_json = 'lecture_php.json'

print("rentrer le type de livre")
categorie = input()
print("rentrer le livre (si plusieurs, mettre un séparateur ',')")
livres = input()

lst = livres.split(",")
lst_count = len(lst)
i = 0

while i < lst_count:

    decoupe_isbn = lst[i]
    print(decoupe_isbn)

    reponse_api = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{decoupe_isbn}&key={api_key}"
    print(reponse_api)
    res = requests.get(reponse_api)
    data = res.json()

    with open(var_json, 'w') as f:
        json.dump(data, f)

    json_data = open(var_json).read()
    data = json.loads(json_data)
    print(data.keys())
    test = data['items']
    for elt in test:
        var = elt['volumeInfo']['infoLink']

    parse_html(var)
    creation_de_la_bdd(bdd,categorie)
    recherche_et_stockage_bdd(bdd,decoupe_isbn,categorie,var)
    i = i + 1

os.remove("lecture_php.json")