import os
import glob, os

chemin_repertoire = os.getcwd()

print(chemin_repertoire)

chaine = "test.vip.bonjour.lassuranceretraite.fr"
lst = chaine.split('.')
lst.reverse()
print(lst)
count = len(lst)
i = 0

while i < count:
    var_recherche = lst[i]
    if var_recherche == "fr":
        var_recherche= lst[i+1] + "." + lst[i]
        i = i+1

    if os.path.isdir(var_recherche):
        print("le fichier existe")

    else:
        print("creation du fichier")
        os.mkdir(var_recherche)

    os.chdir(var_recherche)
    i = i + 1

if lst[0] == "fr":
    lst[0] = lst[1] + '.' + lst[0] 
    del lst[1]

var_chaine = "/".join(lst)
print(var_chaine)


os.chdir("/mydir")
for file in glob.glob("*.txt"):
    print(file)