'''
title: GUI for stock info
author: Palaash Kolhe
date created: 2020-06-13
'''

from webscraping import getStockInfo, getLivePrice
from tkinter import *

class StockInfo:
    def __init__(self, window, pageFinviz):
        self.allStockInfoArray = getStockInfo(pageFinviz) # get stock information

        self.background = 'gray12'
        self.foreground = 'white'

        self.stockInfoFrame = Frame(window, height = 250, width=705, pady=10, padx=10, bg=self.background)
        self.stockInfoFrame.grid(row=5, column=1, columnspan=7, sticky='sw', rowspan=2)

        # Arrays with titles and information for stock info
        self.allTitles = ('Ticker: ', 'Index: ', 'Market Cap: ', 'Index: ', 'Dividend %: ', 'P/E Ratio: ', '52 W High: ', '52 W Low: ', 'Perf Week: ', 'Perf Month: ', 'Perf Year: ', 'Perf YTD: ')

        self.allInfo = []
        for i in range(1, len(self.allStockInfoArray)):
            self.allInfo.append(self.allStockInfoArray[i])

        self.titleLabel = Label(self.stockInfoFrame, text=self.allStockInfoArray[0], bg=self.background, fg=self.foreground,
                                font=('Helvetica', '22', 'bold'), justify=LEFT, padx=10, pady=10)
        self.titleLabel.grid(row=1, column=0, sticky=W, columnspan=10)

        infoNum = 0
        column=1

        # auto create grid with all stock info
        for i in range(3):
            for j in range(2, 6):
                label = Label(self.stockInfoFrame, text=self.allTitles[infoNum], bg=self.background, fg=self.foreground, font=('Helvetica', '13', 'bold'), padx=8, pady=8)
                info = Label(self.stockInfoFrame, text=self.allInfo[infoNum], bg=self.background, fg=self.foreground, font=('Helvetica', '13'), pady=8)
                label.grid(row=j, column=column, sticky='w')
                info.grid(row=j, column=column+1, sticky='w')
                label.grid_propagate(0)
                info.grid_propagate(0)
                infoNum += 1
            column += 2

        for i in range(1, 7):
            self.stockInfoFrame.columnconfigure(i, weight=100)

        self.stockInfoFrame.grid_propagate(0)
