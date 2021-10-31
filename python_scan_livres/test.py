import os
import requests
import json
import sqlite3
from os import listdir
from bs4 import BeautifulSoup
from requests.api import request
import numpy as np

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
#sql = "SELECT prix REPLACE(prix,'€','') FROM MANGA"
#cur.execute("ALTER TABLE MANGA DROP COLUMN prix2")
#cur.execute("ALTER TABLE MANGA ADD COLUMN prix2 interger")
#cur.execute("ALTER TABLE MANGA RENAME TO TempOldTable;")
#cur.execute("UPDATE MANGA SET prix = REPLACE(prix, '€', 'a')")

cur.execute("SELECT COUNT (*) FROM MANGA")
rowcount = cur.fetchone()[0]
print (type(rowcount))


i = 0
price = 0
temp = 0
while i < rowcount:
    cur.execute('SELECT prix FROM MANGA')
    lecture = cur.fetchall()
    #print(lecture)
    modif = list(lecture[i])
    #modife = modif.replace("€","")
    modife = [item.replace('€', '') for item in modif]
    print(modif)


    test = 0 + valeur

    #var = np.array(modife,dtype=float)
    print(test)
    i = i+1



#cur.execute(sql)



#res = cur.fetchall()
#for line in res:
#  print(line)


#conn.commit()