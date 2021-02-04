import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
url = "https://finance.yahoo.com"
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text,"html.parser")
print("The title of the website is: ")
for title in soup.find_all('title'):
    print(title.get_text())

page = requests.get("https://finance.yahoo.com/quote/TSLA/history?p=TSLA")
soup = BeautifulSoup(page.content,"html.parser")
c = soup.find_all('title')
print(c)

page = requests.get("https://finance.yahoo.com/quote/TSLA?p=TSLA")
soup = BeautifulSoup(page.text, 'html.parser')
data = soup.find_all("tbody")
try:
    table1 = data[0].find_all('tr')
except:
    table1 = None

try:
    table2 = data[1].find_all('tr')
except:
    table2 = None

l = {}
u = list()

for i in range(0, len(table1)):
    try:
        table1_td = table1[i].find_all('td')
    except:
        table1_td = None

    l[table1_td[0].text] = table1_td[1].text

    u.append(l)
    l = {}

for i in range(0, len(table2)):
    try:
        table2_td = table2[i].find_all('td')
    except:
        table2_td = None

    l[table2_td[0].text] = table2_td[1].text

    u.append(l)
    l = {}

print(u)




page = requests.get("https://finance.yahoo.com/quote/TSLA/history?p=TSLA")
soup = BeautifulSoup(page.text, 'html.parser')
data = soup.find_all("tbody")

try:
    table3 = data[0].find_all('tr')
except:
    table3 = None

l1 = {}
u1 = list()

for i in range(0, len(table3)):
    try:
        table3_td = table3[i].find_all('td')
    except:
        table3_td = None

    l[table3_td[0].text] = table3_td[1].text

    u1.append(l)
    l1 = {}
print(u1)