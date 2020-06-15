'''
title: GUI for stock info
author: Palaash Kolhe
date created: 2020-06-13
'''

from webscraping import getStockInfo, getLivePrice
from tkinter import *

class StockInfo:
    def __init__(self, window, pageFinviz):
        self.name, self.title, self.index, self.change, self.markCap =  getStockInfo(pageFinviz)

        self.background = 'gray12'
        self.foreground = 'white'

        self.stockInfoFrame = Frame(window, height = 250, width=705, pady=10, padx=10, bg=self.background)
        self.stockInfoFrame.grid(row=5, column=1, columnspan=7, sticky='sw', rowspan=2)

        self.titleLabel = Label(self.stockInfoFrame, text=self.title, bg=self.background, fg=self.foreground, font=('Helvetica', '22', 'bold'), justify=LEFT, padx=10, pady=10)
        self.titleLabel.grid(row=1, column=1, sticky=W, columnspan=7)

        self.nameLabel = Label(self.stockInfoFrame, text='Ticker: ' + self.name, bg=self.background, fg=self.foreground, font=('Helvetica', '13'), padx=10, pady=10)
        self.nameLabel.grid(row=2, column=1)

        self.indexLabel = Label(self.stockInfoFrame, text=self.index)
        self.indexLabel.grid(row=2, column=4)

        self.changeLabel = Label(self.stockInfoFrame, text=self.change)
        self.changeLabel.grid(row=2, column=5)

        self.markCapLabel = Label(self.stockInfoFrame, text=self.markCap)
        self.markCapLabel.grid(row=2, column=6)

        self.stockInfoFrame.grid_propagate(0)

