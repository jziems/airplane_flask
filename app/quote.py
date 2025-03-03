#!/usr/bin/env python

import os
from bs4 import BeautifulSoup
import json
import random
from fake_useragent import FakeUserAgent, UserAgent
from playwright.sync_api import sync_playwright

class Quotes:

    def __init__(self):
        if os.path.isfile('quotes.json'):
            with open('quotes.json', 'r') as fin:
                self.quotes = json.load(fin)
        else:
            self.quotes = []
            fua = FakeUserAgent(platforms=["desktop"])
            ua = fua.random
            browser = sync_playwright().start().chromium.launch()
            context = browser.new_context(user_agent=ua)
            page = context.new_page()
            try:
                page.goto("http://www.imdb.com/title/tt0080339/quotes?tab=qt&ref_=tt_trv_qu")
            except:
                raise
            html = page.content().encode()
            context.close()
            browser.close()

            soup=BeautifulSoup(html, 'html.parser')

            for div in soup.find_all('div', {"class": "cpRasK"}):
                lis = [ f"{li.text}<br><br>" for li in div.find_all(name="li") ]
                self.quotes.append('\n'.join(lis))


    def __del__(self):
        if not os.path.isfile('quotes.json'):
            with open('quotes.json', 'w') as fout:
                json.dump(self.quotes, fout, indent=4)

    def random(self):
        return self.quotes[random.randint(0, len(self.quotes)-1)]

if __name__ == "__main__":
    print(Quotes().random())
