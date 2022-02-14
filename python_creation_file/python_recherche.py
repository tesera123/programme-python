import os
import glob, os

os.chdir('D:/test')

import os

path ="D:\\test"


for root, dirs, files in os.walk(path):
	for file in files:
		if(file.endswith(".cer")):
			print(os.path.join(root,file))




for file in glob.iglob("*.cer" ):
    path = os.path.realpath(file)
    os.chdir('D:/certif')
    print(path)
    chaine = file
    lst = chaine.split('.')
    lst.reverse()
    print(lst)
    count = len(lst)
    i = 0

    while i < count:
        var_recherche = lst[i]
        if var_recherche == "fr" or "com":
            var_recherche= lst[i+1] + "." + lst[i]
            i = i+1

        if os.path.isdir(var_recherche):
            print("le fichier existe")

        else:
            print("creation du fichier")
            os.mkdir(var_recherche)

        os.chdir(var_recherche)
        i = i + 1

    if lst[0] == "fr" or "com":
        lst[0] = lst[1] + '.' + lst[0] 
        del lst[1]

    var_chaine = "/".join(lst)
    print(var_chaine)

