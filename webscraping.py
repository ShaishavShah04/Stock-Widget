'''
title: Webscraping Functions File
authors: Palaash Kolhe & Shaishav Shah
date created: 2020-06-10
'''

from bs4 import BeautifulSoup
import requests
from datetime import datetime
import os, os.path,csv


def webScrapeURL(url):
    agent = {"User-Agent":"Mozilla/5.0"} # specifies what user-agent to search as
    response = requests.get(url, headers = agent) # using requests module to get the content
    entirePage = BeautifulSoup(response.content, 'html.parser') # converts content into html code
    return entirePage

def getLivePrice(page): # Getting the live prices and a time
    #url = 'https://ca.finance.yahoo.com/quote/{0}'.format(ticker) # The url used
    #response = requests.get(url) # Using requests module to get the content
    #yahoo_price_html = BeautifulSoup(response.content,'html.parser') # Converting content into html code
    tag_with_price_and_time = page.find_all(class_ = 'My(6px) Pos(r) smartphone_Mt(6px)')[0] # This is the class I need to search through, obtained through inspect element in chrome
    price = tag_with_price_and_time.find_all('span')[0].text # Price is in the 1st span element, therefore this works
    time = datetime.now().strftime("%H:%M:%S")
    return price,time

def ScrapeTop(page):
    # website = BeautifulSoup(self.response.content,'html.parser')
    array =[]
    all_stocks = page.find_all('table',class_ = 't-home-table')[0]
    for line in all_stocks.find_all('tr'):
        array.append(line.find('td').text)
    # First element is the word 'TICKER', therefore must be removed
    array.pop(0)
    return array

def ScapeDown(page):
    #website = BeautifulSoup(self.response.content, 'html.parser')
    array = []
    all_stocks = page.find_all('table', class_='t-home-table')[1]
    for line in all_stocks.find_all('tr'):
        array.append(line.find('td').text)
    # First element is the word 'TICKER', therefore must be removed
    array.pop(0)
    return array


if __name__ == '__main__':
    applePage = webScrapeURL("https://finviz.com/quote.ashx?t=AAPL")


