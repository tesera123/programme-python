import os
import requests
import json
from os import listdir
from bs4 import BeautifulSoup
from requests.api import request

# ***************** CHEMIN DE BASE ***************** 
chemin_repertoire_git = os.getcwd()
chemin_windows = f"{chemin_repertoire_git}\python_scan_livres"
os.chdir(chemin_windows) 
arr = os.listdir('.')

# ***************** clé et fichier de reference ***************** 
var_json = 'lecture_php2.json'



url = "https://www.amazon.com/s?i=stripbooks&rh=p_66%3A9782809417913"

header = {"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())