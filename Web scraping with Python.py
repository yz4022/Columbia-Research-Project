from urllib.request import urlopen
import requests
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        return None

    title = getTitle("https://finance.yahoo.com/quote/%5EIXIC?p=%5EIXIC")
    if title == None:
        print("Title could not be found.")
    else:
        print(title)


url = "https://finance.yahoo.com"
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text,"html.parser")
print("The title of the website is: ")
for title in soup.find_all('title'):
    print(title.get_text())