'''
title: GUI for top stocks
author: Palaash Kolhe
date created: 2020-06-11
'''

from tkinter import *
from webscraping import ScrapeTop, ScrapeDown, webScrapeURL
from GUI import engineGUI

class TopStocksGUI: # top stocks gui
    def __init__(self, window, engine):
        self.engine = engine # import engine as parameter

        page = webScrapeURL("https://finviz.com/") #

        topArray = ScrapeTop(page) # scrape gainer stocks
        bottomArray = ScrapeDown(page) # scrape loser stocks

        self.stocks = [] # array to store stocks

        for i in range(5): # append stocks to self.stocks
            self.stocks.append(topArray[i])
            self.stocks.append(bottomArray[i])

        self.backgroundColor = 'gray12'
        self.foregroundColor = 'white'

        self.topStockFrame = Frame(window, height=346, width=425, bg = self.backgroundColor) # create frame
        self.topStockFrame.grid(row=1, column=8, rowspan=2, sticky='n')

        self.column = 0 # store column number
        self.row = 1 # store row number

        self.titleLabel = Label(self.topStockFrame, text='TOP STOCKS', font=('Helvetica', '12', 'bold'), bg=self.backgroundColor, fg=self.foregroundColor, padx=10, pady=10.5) # create title label
        self.titleLabel.grid(columnspan=7, sticky='news') # place title label

        self.stockBackground = 'gray22'

        for i in range(10): # make stock bar
            self.makeNewsBar(i)

        for i in range(10): # make columns evenly space
            self.topStockFrame.columnconfigure(i, weight=100)

        self.topStockFrame.grid_propagate(0)

    def change(self,stock): # signify stock is being changed due to keypress
        self.engine.currentTicker = stock
        self.engine.changed = True
        self.engine.getGraphClass().values = []
        self.engine.getGraphClass().times = []

    def makeNewsBar(self,i): # make bar
        self.label = Label(self.topStockFrame, text=self.stocks[i][0], font=('Helvetica', '10', 'bold'),
                           bg=self.stockBackground, fg=self.foregroundColor, padx=5, pady=5, cursor='hand2')
        self.label.grid(column=self.column, row=self.row, sticky='news')
        self.label.bind("<Button-1>", lambda e: self.change(self.stocks[i][0])) # make label change current stock on button press
        self.column += 1

        self.label = Label(self.topStockFrame, text='LAST:', font=('Helvetica', '10', 'bold'),
                           bg=self.backgroundColor, fg=self.foregroundColor, padx=5, pady=5)
        self.label.grid(column=self.column, row=self.row, sticky=W)
        self.column += 1

        self.label = Label(self.topStockFrame, text=self.stocks[i][1], font=('Helvetica', '10'),
                           bg=self.backgroundColor, fg=self.foregroundColor, padx=5, pady=5)
        self.label.grid(column=self.column, row=self.row, sticky=W)
        self.column += 1

        self.label = Label(self.topStockFrame, text='CHANGE:', font=('Helvetica', '10', 'bold'),
                           bg=self.backgroundColor, fg=self.foregroundColor, padx=5, pady=5)
        self.label.grid(column=self.column, row=self.row, sticky=W)
        self.column += 1

        if '-' in self.stocks[i][2]: # make colour red or green based on positive or negative
            changeColour = 'red'
        else:
            changeColour = 'green'

        self.label = Label(self.topStockFrame, text=self.stocks[i][2], font=('Helvetica', '10', 'bold'),
                           bg=self.backgroundColor, fg=changeColour, padx=5, pady=5)
        self.label.grid(column=self.column, row=self.row, sticky=W)
        self.column += 1

        self.label = Label(self.topStockFrame, text='VOLUME:', font=('Helvetica', '10', 'bold'),
                           bg=self.backgroundColor, fg=self.foregroundColor, padx=4, pady=5)
        self.label.grid(column=self.column, row=self.row, sticky=W)
        self.column += 1

        self.label = Label(self.topStockFrame, text=self.stocks[i][3], font=('Helvetica', '10'),
                           bg=self.backgroundColor, fg=self.foregroundColor, padx=4, pady=5)
        self.label.grid(column=self.column, row=self.row, sticky=W)
        self.column += 1

        if self.stockBackground == 'gray22': # alternate colours every stock
            self.stockBackground = self.backgroundColor
        else:
            self.stockBackground = 'gray22'

        self.row += 1
        self.column = 0