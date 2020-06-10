'''
title: Webscraping Functions File
authors: Palaash Kolhe & Shaishav Shah
date created: 2020-06-10
'''

from bs4 import BeautifulSoup
import requests

def webScrapeURL(url):
    agent = {"User-Agent":"Mozilla/5.0"} # specifies what user-agent to search as
    response = requests.get(url, headers = agent) # using requests module to get the content
    entirePage = BeautifulSoup(response.content, 'html.parser') # converts content into html code
    return entirePage


if __name__ == '__main__':
    applePage = webScrapeURL("https://finviz.com/quote.ashx?t=AAPL")


