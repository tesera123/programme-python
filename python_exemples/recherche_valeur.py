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


def parse_html(var,isbn):
    global result
    reqs = requests.get(var)
    reqs.content
    recherche_titre = BeautifulSoup(reqs.content, 'html.parser')
    title = recherche_titre.find('title')
    title = re.sub('<title>','', str(title))
    title = re.sub('</title>','', str(title))
    title = re.sub(f'({isbn})','^_^', str(title))
    print(title)

    table = recherche_titre.find('span', {'class': 'results-price'})
    price = table.get_text()
    real_price = price.strip()
    print(real_price)

isbn = "9791032704028"
parse_html(f"https://www.justbooks.fr/search/?keywords={isbn}&currency=EUR&destination=fr&mode=isbn&classic=off&lang=fr&st=sh&ac=qr&submit=",isbn)