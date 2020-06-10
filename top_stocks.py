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

    # Getter Method

    def getTop(self):
        website = BeautifulSoup(self.response.content,'html.parser')
        all_stocks = website.find_all('table',class_ = 't-home-table')[0]
        for line in all_stocks.find_all('tr'):
            print(line.text)
            print('\n')
        #top_stocks = all_stocks.find_all(class_ = 'table-light-cp-row')
        #print(top_stocks)





if __name__ == "__main__":
    top = TopStocks()
    top.getTop()


