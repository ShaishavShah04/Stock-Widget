'''
title: GUI for Newsfeed
author: Palaash Kolhe
date created: 2020-06-12
'''

from webscraping import webScrapeURL, getNewsStock
from tkinter import *
import webbrowser

class NewsfeedGUI: # GUI creator for newsfeed
    def __init__(self, window, page):
        self.news = getNewsStock(page) # get news

        self.backgroundColor = 'gray12'
        self.foregroundColor = 'white'


        self.newsFrame = Frame(window, height=374, width=425, bg=self.backgroundColor) # create frame
        self.newsFrame.grid(row=3, column=8, rowspan=3, sticky='s') # create location of GUI in window

        self.titleLabel = Label(self.newsFrame, text="LATEST NEWS", font=('Helvetica', '12', 'bold'), bg=self.backgroundColor, fg=self.foregroundColor, padx=10, pady=10.5) # title
        self.titleLabel.grid(row=0, columnspan=4, sticky='news') # place label in frame

        self.newsArray = [] # stores news info

        for i in range(8):
            self.news_row = self.createnews(i) # create news article
            self.newsArray.append(self.news_row) # add to array
            self.newsArray[i][1].grid_propagate(0)

        for i in range(1,9):
            self.newsFrame.rowconfigure(i, weight=100) # to space the news articles evenly

        self.newsFrame.grid_propagate(0)

    def callback(self, url): # open web browser
        webbrowser.open_new(url)

    def createnews(self,i): # creates label for news article
        publisherLabel = Label(self.newsFrame, text=self.news[i][1], font=('Helvetica', '7', 'bold'),
                               bg=self.backgroundColor, fg=self.foregroundColor, padx=3, pady=2, wraplength=100,
                               justify=LEFT)
        news = Label(self.newsFrame, text=self.news[i][0], font=('Helvetica', '9'), bg=self.backgroundColor,
                     fg=self.foregroundColor, padx=2, pady=2, wraplength=330, justify=LEFT, cursor='hand2')

        news.bind("<Button-1>", lambda e: self.callback(self.news[i][2])) # bind news label to website

        publisherLabel.grid(row=i + 1, column=1, sticky=W) # place label in frame
        news.grid(row=i + 1, column=2, sticky=W)
        return (publisherLabel, news)
