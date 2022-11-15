import urllib.request
from bs4 import BeautifulSoup

datos = urllib.request.urlopen('https://docs.python.org/3/').read().decode()

soup = BeautifulSoup(datos)
tags = soup('a')

for tag in tags:
    print(tag.get('href'))