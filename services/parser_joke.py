import random
import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint


def parser(url):
    r = requests.get(URL)
    soup = bs(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [i.text for i in anekdots]


def joke():
    global joker
    if not len(joker):
        joker = parser(URL)
    random.shuffle(joker)
    jok = joker[0]
    del joker[0]
    return jok

URL = 'https://www.anekdot.ru/last/good/'
joker = parser(URL)

if __name__ == '__main__':
    while len(joker):
        pprint(joke())
        print(len(joker))



