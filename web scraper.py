import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os

if __name__ == '__main__':

def dossier():
    os.chdir("C://Users//amoumenmok//Desktop//Web-Scrapper-master")
    dossier()
    url='https://lelscanv.com/lecture-en-ligne-one-piece'


def Navigate(url):
    if url != "Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListeLiens = RecupListeLiens(soup)

return [soup, ListeLiens]


def RecupListeLiens(soup):
    ListeLiens = []

for item in Img:
    if 'src' in item.attrs:
        ListeLiens.append(item['src'])
    return ListeLiens


def Next(soup):
    NextUrl = ""
    A = soup.findAll('a')
    L = []

for a in A:
    if 'class' in a.attrs and a['class'] == ['btn','next_page']:
        NextUrl = a['href']

    if NextUrl == "":
        NextUrl = "Fin du Manga"
        print(NextUrl)

    return NextUrl


def ClasseDownload(item):
    bool = False
    bool = 'class' in item.attrs and (item['class'] == ['page-break'])
    return bool
