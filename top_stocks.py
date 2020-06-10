"""
Shaishav Shah
This is for the Top stocks section in the GUI
Will Scan the Top 5 Stocks that have gained %, and 5 that has dropped %
"""

from bs4 import BeautifulSoup
import requests
import os.path, os

class TopStocks:
    def __init__(self):
        self._url = "https://finviz.com/"
        self.agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'} # This is needed since without this, I get "403 - Forbidden: Access is denied"
        self.response = requests.get(self._url,headers=self.agent)
        self._up = []
        self._down = []

    # Modify Methods

    def ScrapeTop(self):
        website = BeautifulSoup(self.response.content,'html.parser')
        all_stocks = website.find_all('table',class_ = 't-home-table')[0]
        for line in all_stocks.find_all('tr'):
            self._up.append(line.find('td').text)
        # First element is the word 'TICKER', therefore must be removed
        self._up.pop(0)

    def ScapeDown(self):
        website = BeautifulSoup(self.response.content, 'html.parser')
        all_stocks = website.find_all('table', class_='t-home-table')[1]
        for line in all_stocks.find_all('tr'):
            self._down.append(line.find('td').text)
        # First element is the word 'TICKER', therefore must be removed
        self._down.pop(0)
    # Getter

    def getTop(self):
        return self._up

    def getDown(self):
        return self._down




if __name__ == "__main__":
    top = TopStocks()
    top.ScrapeTop()
    top.ScapeDown()

    print(top.getTop())
    print(top.getDown())





