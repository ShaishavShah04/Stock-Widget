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


class Engine:
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
        rcParams['axes.titleweight'] = "bold"
        rcParams['axes.titlecolor'] = 'white'
        rcParams['ytick.color'] = 'white'
            # Configs
        self.fig = plt.figure(figsize=(7, 3), dpi=100)
        self.fig.patch.set_facecolor("#1c1c1c")
        self.graph = self.fig.add_subplot(1, 1, 1)
        self.graph.set_facecolor('#454444')
            # Gui
        self.graphGUI =  graphGUI.GraphGUI(self.window,self.fig,self.graph)
        # News
        self.newsfeed = newsGUI.NewsfeedGUI(self.window, 'AAPL')

    # Modify Methods #
    def createGraphVars(self):
        pass

    # Accessor Methods #
    def getWindow(self):
        return self.window
    def getGraphClass(self):
        return self.graphGUI



if __name__ == "__main__":
    ## Static Data
    window = Engine()
    # Animate
    ani = animation.FuncAnimation(window.fig,window.getGraphClass().animate,fargs=(window.getGraphClass().times, window.getGraphClass().values,window.getGraphClass().ticker ),interval=2000)
    window.getWindow().mainloop()

