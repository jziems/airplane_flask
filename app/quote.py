#!/usr/bin/env python

import os
import requests
from bs4 import BeautifulSoup
import json
import random
from io import BytesIO

class Quotes:

    def __init__(self):
        if os.path.isfile('quotes.json'):
            with open('quotes.json', 'r') as fin:
                self.quotes = json.load(fin)
        else:
            self.quotes = []
            html=requests.get('http://www.imdb.com/title/tt0080339/trivia?tab=qt&ref_=tt_trv_qu', headers={'User-Agent': 'Mozilla'})
            soup=BeautifulSoup(html.text, 'html.parser')
            for div in soup.findAll('div', {"class": "sodatext"}):
                # buf = BytesIO()
                # for p in div.findAll('p'):
                #     if p:
                #         character = p.find('span', {"class": "character"})
                #         if character:
                #             buf.write("{0}: {1} ".format(character.text, p.text.strip()[len(character.text)+2:]).encode())
                #         else:
                #             buf.write(" {0} ".format(p.text.strip()).encode())
                # self.quotes.append(buf.getvalue().decode())
                self.quotes.append(repr(div))
            with open('quotes.json', 'w') as fout:
                json.dump(self.quotes, fout, indent=4)

    def __del__(self):
        if os.path.isfile('quotes.json'):
            os.remove('quotes.json')

    def random(self):
        return self.quotes[random.randint(0, len(self.quotes)-1)]

if __name__ == "__main__":
    print(Quotes().random())
