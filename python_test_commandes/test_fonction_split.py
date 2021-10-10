import os
import requests
import json
import requests as req
import re
import sqlite3

from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup

a_string = 'test1,test2,test3'
split_string = a_string.split(",")
print(split_string[0],split_string[1],split_string[2])