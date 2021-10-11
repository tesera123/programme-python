import os
import sqlite3

chemin_repertoire_git = os.getcwd()
chemin_windows = f"{chemin_repertoire_git}\python_scan_livres"
os.chdir(chemin_windows) 
arr = os.listdir('.')

conn = sqlite3.connect('ma_base.db')
file = open('livres.txt', "r")

variable = 9791032704820
curseur = conn.cursor()

manga = "SELECT isbn FROM MANGA"
DC = "select isbn from DC"
marvel = "select isbn from MARVEL"
recherche = [manga,DC]

for var_recherche in recherche:
    resultat = curseur.execute(var_recherche)
    for row in resultat:
        print(row[0])
conn.close()

"""""
resultat = curseur.execute(manga)

for row in resultat:
    print(row[0],row[1])


for row in resultat:
    valeur = row[2]
    print("ID :",row[0])
    print("livres :",row[1])
    print("isbn :",row[2])
    print("api :",row[3])
    print("--------------------------")
    if valeur == variable:
        print("variable déja présente dans la bdd")
        break
"""

conn.close()
