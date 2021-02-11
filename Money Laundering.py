import requests
from bs4 import BeautifulSoup

# opening a file in write mode
val = input("Which company would you like to search ")
f = open("{}.txt".format("Money Laundering"), "w")
f_title = open("{}.txt".format(val), 'w')

def request_data(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, "html.parser")
    return soup

# create a list of all pages of search results
url_list = []
for i in range(2):
    text = "{}".format(i)
    urls = 'https://www.fincen.gov/search/node?keys=money%20laundering&page=' + text
    url_list.append(urls)

title_list = []
for urls in url_list:
    soup = request_data(urls)

    for links in soup.find_all('a'):
        data = links.get('href')
        if data != None:
            if "www.fincen" in data:
                f.write(data)
                f.write("\n")

    for title in soup.find_all('title'):
        print(title.get_text())




