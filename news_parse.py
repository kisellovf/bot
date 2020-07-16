import requests
from bs4 import BeautifulSoup as BS

r = requests.get('https://stopgame.ru/review/new/stopchoice')

html = BS(r.content, 'html.parser')

for el in html.select('.item'):
    title = html.select('.caption > a')
    print(title[0].text)
