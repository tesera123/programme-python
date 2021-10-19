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
var_fichier = "livres.txt"
os.chdir(chemin_windows) 
arr = os.listdir('.')


# ***************** clé et fichier de reference ***************** 
api_key = "AIzaSyDQCmVtPm4rWhmRrIvonLuy8SS3-rjJQO0"
conn = sqlite3.connect('ma_base.db')
file = open('livres.txt', "r")
bdd = 'ma_base.db'
var_json = 'lecture_php.json'

print("rentré le type de livre")
categorie = input()
print("rentré le livre (si plusieurs, mettre un séparateur ',')")
livres = input()



with open("livres.txt", 'r') as f:
    for line in f:
        line_split = line.split("-")

        reponse_api = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{line_split[1]}&key={api_key}"
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
        creation_de_la_bdd(bdd,line_split)
        recherche_et_stockage_bdd(bdd,line_split,var)

        line = file.readline()
    file.close()
os.remove("lecture_php.json")