from bs4 import BeautifulSoup

import requests

r  = requests.get("https://www.freepeople.com/")

data = r.text
print data

soup = BeautifulSoup(data, features="html.parser")

for link in soup.select("meta[itemprop='url']"):
    print link.get('content')
