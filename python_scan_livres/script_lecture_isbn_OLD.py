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

    #reponse_api = f"https://www.abebooks.fr/servlet/SearchResults?cm_sp=SearchF-_-topnav-_-Results&ds=20&kn={decoupe_isbn}"
    reponse_api = f"https://www.justbooks.fr/search/?keywords={decoupe_isbn}&currency=EUR&destination=fr&mode=isbn&classic=off&lang=fr&st=sh&ac=qr&submit="
    print(reponse_api)

    #parse_html(reponse_api,decoupe_isbn)
    creation_de_la_bdd(bdd,categorie)
    recherche_et_stockage_bdd(bdd,decoupe_isbn,categorie,reponse_api)
    i = i + 1