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
from GUI import stockinfoGUI
from matplotlib import rcParams
import matplotlib.pyplot as plt
from webscraping import *


class Engine:
    def __init__(self):

        # The basics of creating a window here... Nothing fancy
        self.window = Tk()
        self.window.minsize(1028, 720)
        self.window.title("Stock Trader")
        self.window.configure(bg="#1c1c1c")
        self.window.resizable(False, False) # Keeping it non-resizeable so it doesn't alter how the content will look
        self.currentTicker = 'SPY' # Default stock shown
        self.changed = False # To identify if the stock has been changed
        #

        # Search
        self.searchBar = searchBarGUI.SearchBarGUI(self.window,self)

        # Top Stocks
        self.topStocks = topStocksGUI.TopStocksGUI(self.window,self)

        # Graph -- Much of the graph config has to be done here since the variables have to be accessed in this file.

            # Colors

        rcParams['axes.labelcolor'] = 'white'
        rcParams['xtick.color'] = 'white'
        rcParams['axes.titleweight'] = "bold"
        rcParams['ytick.color'] = 'white'
        rcParams['text.color'] = 'white'

            # Configs
        self.fig = plt.figure(figsize=(7, 3), dpi=100) # Basically a 700x300 i,age
        self.fig.patch.set_facecolor("#1c1c1c")
        self.graph = self.fig.add_subplot(1, 1, 1)
        self.graph.set_facecolor('#454444')

            # Gui
        self.graphGUI =  graphGUI.GraphGUI(self.window,self.fig,self.graph)

        # Stock info
        self.urlFinviz = "https://finviz.com/quote.ashx?t={0}".format(self.currentTicker) # URL FOR FINVIZ
        self.urlYahoo = 'https://ca.finance.yahoo.com/quote/{0}'.format(self.currentTicker) # URL FOR YAHOO FINANCE

        self.pageFinviz = webScrapeURL(self.urlFinviz)
        self.pageYahoo= webScrapeURL(self.urlYahoo)

        self.newsfeed = newsGUI.NewsfeedGUI(self.window, self.pageFinviz)

        # Stock info GUI
        self.stockInfo = stockinfoGUI.StockInfo(self.window, self.pageFinviz)

    # Modify Methods #

    def changeTicker(self,ticker): # Self-explanatory
        self.currentTicker = ticker
        self.graphGUI.ticker = ticker

    def updateEverything(self): # Re-Init stuff which changes based on stocks
        self.newsfeed.__init__(self.window,webScrapeURL("https://finviz.com/quote.ashx?t={0}".format(self.currentTicker)))
        self.stockInfo.__init__(self.window,webScrapeURL("https://finviz.com/quote.ashx?t={0}".format(self.currentTicker)))

    # Accessor Methods #

    def getWindow(self):
        return self.window
    def getGraphClass(self):
        return self.graphGUI
    def getTicker(self):
        return self.currentTicker