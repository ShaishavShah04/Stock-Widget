'''
title: GUI for Window
authors: Palaash & Shaishav
date created: 2020-06-11
'''

from tkinter import *
from GUI import topStocksGUI
from GUI import searchBarGUI
from GUI import graphGUI
from GUI import newsGUI
from GUI import stockinfo
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import rcParams
import matplotlib.pyplot as plt
from webscraping import *


class Engine:
    def __init__(self):
        self.window = Tk()
        self.window.minsize(1028, 720)
        self.window.title("Stock Trader")
        self.window.configure(bg="#1c1c1c")
        self.window.resizable(False, False)
        self.currentTicker = 'SPY'
        #

        # Search
        self.searchBar = searchBarGUI.SearchBarGUI(self.window)
            # Checking for updates

        # Top Stocks
        self.topStocks = topStocksGUI.TopStocksGUI(self.window)

        # Graph -- Much of the graph config has to be done here since the variables have to be accessed in this file.
            # Colors

        rcParams['axes.labelcolor'] = 'white'
        rcParams['xtick.color'] = 'white'
        rcParams['axes.titleweight'] = "bold"
        rcParams['ytick.color'] = 'white'
        rcParams['text.color'] = 'white'

        # Stock info
        self.stockTicker = 'AAPL' ### TO BE CHANGED LATER
        self.urlFinviz = "https://finviz.com/quote.ashx?t={0}".format(self.stockTicker) # URL FOR FINVIZ
        self.urlYahoo = 'https://ca.finance.yahoo.com/quote/{0}'.format(self.stockTicker) # URL FOR YAHOO FINANCE

        self.pageFinviz = webScrapeURL(self.urlFinviz)
        self.pageYahoo= webScrapeURL(self.urlYahoo)

            # Configs
        self.fig = plt.figure(figsize=(7, 3), dpi=100)
        self.fig.patch.set_facecolor("#1c1c1c")
        self.graph = self.fig.add_subplot(1, 1, 1)
        self.graph.set_facecolor('#454444')

            # Gui
        self.graphGUI =  graphGUI.GraphGUI(self.window,self.fig,self.graph)

        # News
        self.newsfeed = newsGUI.NewsfeedGUI(self.window, self.currentTicker)
        self.newsfeed = newsGUI.NewsfeedGUI(self.window, self.pageFinviz)

        # Stock info GUI
        self.stockInfo = stockinfo.StockInfo(self.window, self.pageFinviz)

    # Modify Methods #
    def createGraphVars(self):
        pass

    def changeTicker(self,ticker):
        self.currentTicker = ticker
        self.graphGUI.ticker = ticker

    # Accessor Methods #
    def getWindow(self):
        return self.window
    def getGraphClass(self):
        return self.graphGUI
    def getTicker(self):
        return self.currentTicker


if __name__ == "__main__":
    ## Static Data
    window = Engine()
    # Check for change in searchbar
    # Animate
    ani = animation.FuncAnimation(window.fig,window.getGraphClass().animate,fargs=(window.getGraphClass().times, window.getGraphClass().values,window.currentTicker),interval=2000)
    window.window.mainloop()

