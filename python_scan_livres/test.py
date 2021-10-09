import os
from os import listdir
from os.path import isfile, join

# récupérer le chemin du répertoire courant
chemin_repertoire_git = os.getcwd()
file = f"{chemin_repertoire_git}\livres.txt"
print (file)


fichiers = [f for f in listdir(chemin_repertoire_git) if isfile(join(chemin_repertoire_git, f))]

print (fichiers)