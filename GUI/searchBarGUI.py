from tkinter import *

class SearchBarGUI:
    def __init__(self, window):
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

    # Submit button:
    def submitClick(self):
        self.enteredTicker = (self.searchBar.get()).upper()
        return self.enteredTicker

    #Getter
    def getTicker(self):
        return self.enteredTicker


if __name__ == "__main__":
    from GUI import engineGUI
    window = engineGUI.Engine()
    search = SearchBarGUI(window.window)
    window.window.mainloop()