'''
title: GUI for stock info
author: Palaash Kolhe
date created: 2020-06-13
'''

from webscraping import getStockInfo, getLivePrice
from tkinter import *

class StockInfo:
    def __init__(self, window, pageFinviz):
        self.name, self.title, self.index, self.change, self.markCap, self.dividend, self.PE, self.wHigh, self.wLow =  getStockInfo(pageFinviz)

        self.background = 'gray12'
        self.foreground = 'white'

        self.stockInfoFrame = Frame(window, height = 250, width=705, pady=10, padx=10, bg=self.background)
        self.stockInfoFrame.grid(row=5, column=1, columnspan=7, sticky='sw', rowspan=2)

        self.titleLabel = Label(self.stockInfoFrame, text=self.title, bg=self.background, fg=self.foreground, font=('Helvetica', '22', 'bold'), justify=LEFT, padx=10, pady=10)
        self.titleLabel.grid(row=1, column=1, sticky=W, columnspan=7)

        self.nameLabel = Label(self.stockInfoFrame, text='Ticker: ' + self.name, bg=self.background, fg=self.foreground, font=('Helvetica', '13'), padx=10, pady=8)
        self.nameLabel.grid(row=2, column=1, sticky='w')

        self.indexLabel = Label(self.stockInfoFrame, text='Index: ' + self.index, bg=self.background, fg=self.foreground, font=('Helvetica', '13'), padx=10, pady=8)
        self.indexLabel.grid(row=3, column=1, sticky='w')

        self.changeLabel = Label(self.stockInfoFrame, text='Change: ' + self.change, bg=self.background, fg=self.foreground, font=('Helvetica', '13'), padx=10, pady=8)
        self.changeLabel.grid(row=4, column=1, sticky='w')

        self.markCapLabel = Label(self.stockInfoFrame, text='Market Cap: ' + self.markCap, bg=self.background, fg=self.foreground, font=('Helvetica', '13'), padx=10, pady=8)
        self.markCapLabel.grid(row=5, column=1, sticky='w')

        self.dividendLabel = Label(self.stockInfoFrame, text='Dividend %: ' + self.dividend, bg=self.background,
                                  fg=self.foreground, font=('Helvetica', '13'), padx=10, pady=8)
        self.dividendLabel.grid(row=2, column=2, sticky='w')

        self.PELabel = Label(self.stockInfoFrame, text='P/E Ratio: ' + self.PE, bg=self.background,
                                   fg=self.foreground, font=('Helvetica', '13'), padx=10, pady=8)
        self.PELabel.grid(row=3, column=2, sticky='w')

        self.wHighLabel = Label(self.stockInfoFrame, text='52 W High: ' + self.wHigh, bg=self.background,
                             fg=self.foreground, font=('Helvetica', '13'), padx=10, pady=8)
        self.wHighLabel.grid(row=4, column=2, sticky='w')

        self.wLowLabel = Label(self.stockInfoFrame, text='52 W Low: ' + self.wLow, bg=self.background,
                             fg=self.foreground, font=('Helvetica', '13'), padx=10, pady=8)
        self.wLowLabel.grid(row=5, column=2, sticky='w')

        self.stockInfoFrame.grid_propagate(0)

