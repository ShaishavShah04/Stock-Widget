from tkinter import *
from webscraping import getLivePrice, webScrapeURL

class SearchBarGUI:
    def __init__(self, window,engine):
        self.searchBarBackground = 'gray12'
        self.searchBarForeground = 'white'

        self.enteredTicker = 'SPY'

        # Frame
        self.searchBarFrame = Frame(window, height = 55, width = 600, pady = 5, bg=self.searchBarBackground)
        self.searchBarFrame.grid(row=1, column=1, columnspan=7, sticky='n')

        # Label, Input, And Submit
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
            page = webScrapeURL('https://ca.finance.yahoo.com/quote/{0}'.format((self.searchBar.get()).upper()))
            t,p = getLivePrice(page)
            self.enteredTicker = (self.searchBar.get()).upper()
            self.engine.currentTicker = self.enteredTicker
            self.engine.changed = True
            self.engine.getGraphClass().values = []
            self.engine.getGraphClass().times = []
            self.searchBar.delete(0, END)
        except:
            self.errorMessage()

    def errorMessage(self):
        errorBox = Tk()
        errorBox.wm_title('You don\'t know stock!')
        errorBox.minsize(300,100)
        errorBox.resizable(False,False)
        errorBox.configure(bg='#1c1c1c')
        #
        message = Label(errorBox,text="Stock not found, Sorry!",bg='#1c1c1c',fg='#FFFFFF')
        message.pack(side='top',fill=X)
        #
        b = Button(errorBox,text="I will enter a better stock", command = errorBox.destroy, bg='#1c1c1c',fg='#FFFFFF')
        b.pack(side='bottom',fill=X)

        on = True
        def off():
            global on
            on = False

        errorBox.protocol('WM_DELETE_WINDOW', off)

        # try:
        while on:
            errorBox.update_idletasks()
            errorBox.update()
        #except:
        #    off()


    #Getter
    def getTicker(self):
        return self.enteredTicker
