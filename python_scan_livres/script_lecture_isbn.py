import os
import requests
import json
import requests as req
import re
import sqlite3

from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup
from definition import stockage_dans_la_bdd,parse_html,recherche_dans_bdd

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

        parse_html(var)
        recherche_dans_bdd('ma_base.db',line_split[1])
        stockage_dans_la_bdd('ma_base.db',line_split,var)
        
        line = file.readline()
    file.close()
os.remove("lecture_php.json")