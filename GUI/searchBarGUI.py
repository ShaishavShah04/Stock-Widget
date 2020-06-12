
from tkinter import *

class SearchBarGUI:
    def __init__(self, window):
        self.searchBarBackground = 'gray12'
        self.searchBarForeground = 'white'

        self.searchBarFrame = Frame(window, height = 55, width = 600, pady = 5, bg=self.searchBarBackground)
        self.searchBarFrame.grid(row=1, column=1, columnspan=3, sticky='n')
        self.searchBarFrame.columnconfigure(0, weight=2)
