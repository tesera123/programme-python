import os
import requests
import json
import requests as req
import re
import sqlite3
from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup
#rom definition import recherche_et_stockage_bdd


var_json = 'lecture_php.json'

def parse_html(var):
    reqs = requests.get(var)
    reqs.content
    print(reqs.content)
    recherche_titre = BeautifulSoup(reqs.content, 'html.parser')
    title = recherche_titre.find('meta name="description"')


   # title = re.sub('<title>','', str(title))
   # title = re.sub('</title>','', str(title))
    print(title)
    #title = re.sub(f'({isbn})','^_^', str(title))

isbn = "978-2-82033-831-0"
reponse_api = f"https://www.abebooks.fr/servlet/SearchResults?sts=t&cm_sp=SearchF-_-home-_-Results&cm_sp=SearchF-_-home-_-Results&an=&tn=&kn={isbn}"
parse_html(reponse_api)




"""
with open(var_json, 'w') as f:
    json.dump(data, f)

json_data = open(var_json).read()
data = json.loads(json_data)
print(data.keys())
test = data['items']
for elt in test:
    var = elt['volumeInfo']['infoLink']

    parse_html(var)
"""