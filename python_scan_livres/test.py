import os
import requests
import json
import sqlite3
from os import listdir
from bs4 import BeautifulSoup
from requests.api import request


# ***************** CHEMIN DE BASE ***************** 
chemin_repertoire_git = os.getcwd()
chemin_windows = f"{chemin_repertoire_git}\python_scan_livres"
os.chdir(chemin_windows) 
arr = os.listdir('.')

# ***************** clé et fichier de reference ***************** 
conn = sqlite3.connect('ma_base.db')
bdd = 'ma_base.db'
var_json = 'lecture_php.json'
cur = conn.cursor()

sql = "DELETE FROM DC WHERE id = 7"
cur.execute(sql)
conn.commit()