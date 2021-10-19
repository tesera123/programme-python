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
conn = sqlite3.connect('bdd_livres.db')
bdd = 'bdd_livres.db'
cur = conn.cursor()

#sql = "DELETE FROM MANGA WHERE id = 5"
#sql = "Select * from MANGA order by livres asc"
sql = "SELECT prix REPLACE(prix,'€','') FROM MANGA"

cur.execute("update MANGA set prix=replace(prix,'€','test')")


#cur.execute(sql)



#res = cur.fetchall()
#for line in res:
#  print(line)


#conn.commit()