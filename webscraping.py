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

def getNewsStock(page):
    newsArray = []
    for data in page.findAll("div", {"class": "news-link-container"}): # searches for news class in entire page
        newsText = data.findAll(text=True) # returns all text and publisher
        newsLink = data.find('a').get('href') # search for links
        newsArray.append([newsText[0], newsText[1], newsLink]) # append to array to be used to find news sources
    return newsArray


if __name__ == '__main__':
    applePage = webScrapeURL("https://finviz.com/quote.ashx?t=AAPL")
    news = getNewsStock(applePage)
    for i in range(len(news)):
        print(news[i])


