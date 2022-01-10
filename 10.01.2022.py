import requests
from bs4 import BeatifulSoup
lapa = requests.get("http://vilanuvidusskola.blogspot.com/%22)
print(lapa)
print(lapa.content)


soup = BeatifulSoup(lapa.content, 'html.parser')
print(soup.prettify())