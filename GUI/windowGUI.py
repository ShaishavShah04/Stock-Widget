'''
title: GUI for Window
authors: Palaash & Shaishav
date created: 2020-06-11
'''

from tkinter import *
from GUI import topStocksGUI
from GUI import searchBarGUI

class Window:
    def __init__(self):
        self.window = Tk()
        self.window.minsize(1028, 720)
        self.window.title("Stock Trader")
        self.window.configure(bg="black")
        self.window.resizable(False, False)

        searchBar = searchBarGUI.SearchBarGUI(self.window)
        topStocks = topStocksGUI.TopStocksGUI(self.window)

    # Accessor Methods #
    def getWindow(self):
        return self.window

if __name__ == "__main__":
    window = Window()
    window.window.mainloop()

