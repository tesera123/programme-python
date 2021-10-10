import os
import requests
import json
import requests as req
import re

from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup

chemin_repertoire_git = os.getcwd()
chemin_windows = f"{chemin_repertoire_git}\python_scan_livres"
os.chdir(chemin_windows) 
arr = os.listdir('.')

api_key = "AIzaSyDQCmVtPm4rWhmRrIvonLuy8SS3-rjJQO0"

file = open('livres.txt', "r")
lines = file.readlines()

with open('livres.txt', 'r') as f:
    for line in f:
    #for line in lines:
        print(line)
        if "[MANGA]" in line :
            w = open('title.txt', "a")
            w.write('\n')
            w.write(line)
            w.write('\n')
        elif "[DC]" in line :
            w = open('title.txt', "a")
            w.write('\n')
            w.write(line)
            w.write('\n')
        else:
            reponse_api = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{line}&key={api_key}"
            res = requests.get(reponse_api)
            data = res.json()
            #data = res.json()
            #clé api google AIzaSyDQCmVtPm4rWhmRrIvonLuy8SS3-rjJQO0
            with open('json.json', 'w') as f:
                json.dump(data, f)

            json_data = open(r'json.json').read()
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

            w = open('title.txt', "a")
            w.write(str(result))
            w.write('\n')
        line = file.readline()
    file.close()