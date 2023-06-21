import requests
from bs4 import BeautifulSoup

url = 'https://webflow.com'

page = requests.get(url)

soup = BeautifulSoup(page.text, features='html.parser')
divs = soup.find_all("div", {"class": "intro-logos_wrapper"})
for div in divs:
    for element in div.find_all("img"):
        print(element['src'])
