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

        self.backgroundColor = 'grey'

        self.topStockFrame = Frame(window, height=360, width=428, pady = 5, padx = 5, bg = self.backgroundColor)
        self.topStockFrame.pack(side=TOP, fill='none', anchor='e')

    def getStocks(self):
        return self.stocks

if __name__ == "__main__":
    window = windowGUI.Window()
    topStocks = TopStocksGUI(window.window)
    window.window.mainloop()
