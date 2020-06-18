'''
title: GUI for top stocks
author: Palaash Kolhe
date created: 2020-06-11
'''

from tkinter import *
from webscraping import ScrapeTop, ScrapeDown, webScrapeURL
from GUI import engineGUI

class TopStocksGUI:
    def __init__(self, window,engine):

        self.engine= engine

        page = webScrapeURL("https://finviz.com/")

        topArray = ScrapeTop(page)
        bottomArray = ScrapeDown(page)

        self.stocks = []

        for i in range(5):
            self.stocks.append(topArray[i])
            self.stocks.append(bottomArray[i])

        self.backgroundColor = 'gray12'
        self.foregroundColor = 'white'

        self.topStockFrame = Frame(window, height=346, width=425, bg = self.backgroundColor)
        self.topStockFrame.grid(row=1, column=8, rowspan=2, sticky='n')

        self.column = 0
        self.row = 1

        self.titleLabel = Label(self.topStockFrame, text='TOP STOCKS', font=('Helvetica', '12', 'bold'), bg=self.backgroundColor, fg=self.foregroundColor, padx=10, pady=10.5)
        self.titleLabel.grid(columnspan=7, sticky='news')

        stockBackground = 'gray22'

        for i in range(10):
            self.makeNewsBar(i,stockBackground)

        self.topStockFrame.grid_propagate(0)

    def change(self,stock):
        self.engine.currentTicker = stock
        self.engine.changed = True
        self.engine.getGraphClass().values = []
        self.engine.getGraphClass().times = []

    def makeNewsBar(self,i,stockBackground):
        self.label = Label(self.topStockFrame, text=self.stocks[i][0], font=('Helvetica', '10', 'bold'),
                           bg=stockBackground, fg=self.foregroundColor, padx=5, pady=5)
        self.label.grid(column=self.column, row=self.row, sticky='news')
        self.label.bind("<Button-1>", lambda e: self.change(self.stocks[i][0]))
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

        if '-' in self.stocks[i][2]:
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

        if stockBackground == 'gray22':
            stockBackground = self.backgroundColor
        else:
            stockBackground = 'gray22'

        self.row += 1
        self.column = 0



    def getStocks(self):
        return self.stocks

if __name__ == "__main__":
    window = engineGUI.Engine()
    topStocks = TopStocksGUI(window.window)
    window.window.mainloop()
