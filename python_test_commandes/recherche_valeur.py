import os
import requests
import json
import requests as req
import re
import sqlite3
from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup
from definition import recherche_et_stockage_bdd

bdd = "ma_base.db"
chemin_repertoire_git = os.getcwd()
chemin_windows = f"{chemin_repertoire_git}\python_scan_livres"
var_fichier = "livres.txt"
os.chdir(chemin_windows) 
arr = os.listdir('.')

conn = sqlite3.connect(bdd)

recherche_et_stockage_bdd(bdd)