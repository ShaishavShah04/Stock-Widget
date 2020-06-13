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
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import rcParams
import matplotlib.pyplot as plt


class Window:
    def __init__(self):
        self.window = Tk()
        self.window.minsize(1028, 720)
        self.window.title("Stock Trader")
        self.window.configure(bg="#1c1c1c")
        self.window.resizable(False, False)
        # Search
        self.searchBar = searchBarGUI.SearchBarGUI(self.window)
        # Top Stocks
        self.topStocks = topStocksGUI.TopStocksGUI(self.window)

        # Graph -- Much of the graph config has to be done here since the variables have to be accessed in this file.
            # Colors
        rcParams['axes.labelcolor'] = 'white'
        rcParams['xtick.color'] = 'white'
        rcParams['ytick.color'] = 'white'
            # Configs
        self.fig = Figure(figsize=(7, 3), dpi=100)
        self.fig.patch.set_facecolor("#1c1c1c")
        self.graph = self.fig.add_subplot(1, 1, 1)
        self.graph.set_facecolor('#454444')
        self.graphGUI =  graphGUI.GraphGUI(self.window,self.fig,self.graph)
        plt.xticks(rotation=45, ha='right')
        plt.title('{0} Stock Price'.format(self.graphGUI.ticker))
        plt.ylabel('Price')

        # News
        self.newsfeed = newsGUI.NewsfeedGUI(self.window, 'AAPL')

    # Modify Methods #


    # Accessor Methods #
    def getWindow(self):
        return self.window
    def getGraphClass(self):
        return self.graphGUI

if __name__ == "__main__":
    ## Static Data

    ##
    window = Window()
    # Animate
    ani = animation.FuncAnimation(window.fig,window.getGraphClass().animate,fargs=(window.getGraphClass().times, window.getGraphClass().values,window.getGraphClass().ticker ),interval=2000)
    window.getWindow().mainloop()

