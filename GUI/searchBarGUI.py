"""
Shaishav Shah
The search bar is in this file
"""

from tkinter import *
from webscraping import getLivePrice, webScrapeURL

class SearchBarGUI:
    def __init__(self, window, engine):

        self.searchBarBackground = 'gray12'
        self.searchBarForeground = 'white'
        self._enteredTicker = 'SPY'

        # Frame
        self.searchBarFrame = Frame(window, height = 55, width = 600, pady = 5, bg=self.searchBarBackground)
        self.searchBarFrame.grid(row=1, column=1, columnspan=7, sticky='n')

        # Label, Input, And Submit fields
        self.tickerLabel = Label(self.searchBarFrame, text="Enter Ticker: ", font=('Helvetica', '12', 'bold'),bg=self.searchBarBackground, fg=self.searchBarForeground)
        self.tickerLabel.grid(row=1, column=1, sticky='news', pady=5, padx=(20, 5))
        self.tickerLabel.grid_propagate(0)

        self.searchBar = Entry(self.searchBarFrame, bg='gray22', width=46, fg=self.searchBarForeground,font=('Helvetica', '12', 'bold'), borderwidth=0)
        self.searchBar.grid(row=1, column=3, sticky='news')
        self.searchBar.grid_propagate(0)

        self.searchButton = Button(self.searchBarFrame, command=self.submitClick, bg='gray16', fg=self.searchBarForeground, text='Search',font=('Helvetica', '12', 'bold'), borderwidth=0, width=15)
        self.searchButton.grid(row=1, column=5, sticky='news')
        self.searchButton.grid_propagate(0)

        # Engine Shadow
        self.engine = engine

    # Submit button:
    def submitClick(self):
        try:
            # Checks to see if stock is real
            page = webScrapeURL('https://ca.finance.yahoo.com/quote/{0}'.format((self.searchBar.get()).upper()))
            t,p = getLivePrice(page)


            # Changes ticker in the engine and reset values
            self._enteredTicker = (self.searchBar.get()).upper()
            self.engine.currentTicker = self._enteredTicker
            self.engine.changed = True
            self.engine.getGraphClass().values = []
            self.engine.getGraphClass().times = []

            # Clear the search bar
            self.searchBar.delete(0, END)

        except: # Any sort of error which occurs, the program will print that the stock / entered ticker was invalid

            self.errorMessage()

    def errorMessage(self): # Seperate Pop-Up window which makes the Error Box
        on = True
        def off():
            global on
            on = False

        errorWindow = Tk()
        errorWindow.wm_title("Error")
        errorWindow.geometry("350x100")
        errorWindow.resizable(True, False)
        errorWindow.configure(bg='gray20')

        message = Label(errorWindow, text='No results found for "{ticker}"'.format(ticker=self.searchBar.get()), fg='white', bg='gray20', font=('Helvetica', '13'), justify=CENTER, padx=10, pady=10)
        message.pack(side='top', expand=Y)
        button = Button(errorWindow, text='OK', command=errorWindow.destroy, bg='gray38', fg='white', width=15, height=1, borderwidth=0, font=('Helvetica', '10', 'bold'))
        button.pack(side='bottom', expand=Y)

        message.rowconfigure(0, weight=100)
        message.rowconfigure(1, weight=100)
        message.columnconfigure(0, weight=100)

        message.grid_propagate(0)
        # errorWindow.grid_propagate(0)

        errorWindow.protocol('WM_DELETE_WINDOW', off)

        # try:
        while on:
            try:
                errorWindow.update_idletasks()
                errorWindow.update()
            except:
                off()
