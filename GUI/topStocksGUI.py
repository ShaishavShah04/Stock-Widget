'''
title: GUI for top stocks
author: Palaash Kolhe
date created: 2020-06-11
'''

from tkinter import *
from webscraping import ScrapeTop, ScrapeDown, webScrapeURL
from GUI import windowGUI

class TopStocksGUI:

    def __init__(self, window):
        page = webScrapeURL("https://finviz.com/")

        topArray = ScrapeTop(page)
        bottomArray = ScrapeDown(page)

        self.stocks = []

        for i in range(5):
            self.stocks.append(topArray[i])
            self.stocks.append(bottomArray[i])

        self.backgroundColor = 'gray12'
        self.foregroundColor = 'white'

        self.topStockFrame = Frame(window, height=360, width=425, pady = 5, bg = self.backgroundColor)
        self.topStockFrame.grid(row=1, column=8)

        self.column = 0
        self.row = 1

        for i in range(10):
            self.label = Label(self.topStockFrame, text=self.stocks[i][0], font=('Helvetica', '12', 'bold'), bg='gray22', fg=self.foregroundColor, padx=5, pady=5)
            self.label.grid(column=self.column, row=self.row)
            self.column += 1

            self.label = Label(self.topStockFrame, text='CHANGE:', font=('Helvetica', '12', 'bold'), bg='gray22', fg=self.foregroundColor, padx=5, pady=5)
            self.label.grid(column=self.column, row=self.row)
            self.column += 1

            self.label = Label(self.topStockFrame, text=self.stocks[i][2], font=('Helvetica', '12', 'bold'), bg='gray22', fg=self.foregroundColor, padx=5, pady=5)
            self.label.grid(column=self.column, row=self.row)
            self.column += 1

            self.row += 1
            self.column = 0


        self.topStockFrame.columnconfigure(1, weight=1)

        self.topStockFrame.grid_propagate(0)

    def getStocks(self):
        return self.stocks

if __name__ == "__main__":
    window = windowGUI.Window()
    topStocks = TopStocksGUI(window.window)
    window.window.mainloop()
