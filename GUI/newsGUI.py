'''
title: GUI for Newsfeed
author: Palaash Kolhe
date created: 2020-06-12
'''

from webscraping import webScrapeURL, getNewsStock
from tkinter import *

class NewsfeedGUI:
    def __init__(self, window, ticker):
        self.url = "https://finviz.com/quote.ashx?t={0}".format(ticker)
        self.page = webScrapeURL(self.url)
        self.news = getNewsStock(self.page)

        self.backgroundColor = 'gray16'
        self.foregroundColor = 'white'

        self.newsFrame = Frame(window, height=374, width=425, bg=self.backgroundColor)
        self.newsFrame.grid(row=2, column=8)

        self.titleLabel = Label(self.newsFrame, text="LATEST NEWS", font=('Helvetica', '12', 'bold'), bg=self.backgroundColor, fg=self.foregroundColor, padx=10, pady=10.5)
        self.titleLabel.grid(columnspan=8, sticky='news')

        self.newsFrame.grid_propagate(0)

