import os
import requests
import json

from os import listdir
from os.path import isfile, join


chemin_repertoire_git = os.getcwd()
chemin_windows = f"{chemin_repertoire_git}\python_scan_livres"
os.chdir(chemin_windows) 
arr = os.listdir('.')

api_key = "AIzaSyDQCmVtPm4rWhmRrIvonLuy8SS3-rjJQO0"

file = open('livres.txt', "r")
lines = file.readlines()

for line in lines:
    print(line)
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
        print(elt['volumeInfo']['title'])
        var = elt['volumeInfo']['title']

    ecriture_titre = open('title.txt', "a")
    ecriture_titre.write(elt['volumeInfo']['title'])
    ecriture_titre.write('\n')
    line = file.readline()
file.close()