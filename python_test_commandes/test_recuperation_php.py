
# importing the modules
import requests
from bs4 import BeautifulSoup
  
# target url
url = 'http://books.google.fr/books?id=3LP2zQEACAAJ&dq=isbn:9791032706770&hl=&source=gbs_api'
  
# making requests instance
reqs = requests.get(url)
reqs.content
  
