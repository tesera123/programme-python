import os
  


chaine = "test.cnav.fr"

print(chaine)

lst = chaine.split(".")

print(lst)
lst.reverse()

print(lst)

lst_count = len(lst)

lecture = ""
base = "fr"
i = 0

while i < lst_count:
    print(lst[i])
    if lst[i] == "fr":
        print("attention il y a fr")
        base = lst[i]
    else:  
        lecture = base + "\" + lst[i]
        print(lecture)

    i = i+1
    


"""""
# Directory
directory = "GeeksforGeeks"
  
parent_dir = "D:/Pycharm projects/"
  

path = os.path.join(parent_dir, directory)

os.mkdir(path)
print("Directory '% s' created" % directory)
"""""