
from tkinter import *

class SearchBarGUI:
    def __init__(self, window):
        self.searchBarBackground = 'gray12'
        self.searchBarForeground = 'white'

        self.enteredTicker = None

        # Frame
        self.searchBarFrame = Frame(window, height = 55, width = 600, pady = 5, bg=self.searchBarBackground)
        self.searchBarFrame.grid(row=1, column=1, columnspan=3, sticky='n')
        self.searchBarFrame.columnconfigure(0, weight=2)

        # Label, Input, And Submit
        self.tickerLabel = Label(self.searchBarFrame, text="Enter Ticker: ", font=('Helvetica', '12', 'bold'),bg=self.searchBarBackground, fg=self.searchBarForeground)
        self.tickerLabel.pack(side=LEFT, fill=BOTH, expand=True, pady=5, padx=20)
        self.searchBar = Entry(self.searchBarFrame, bg='gray22', width=45, fg=self.searchBarForeground,font=('Helvetica', '12', 'bold'), borderwidth=0)
        self.searchBar.pack(side=LEFT, expand=True, fill=BOTH)
        self.searchButton = Button(self.searchBarFrame, command=self.submitClick, bg='gray16', fg=self.searchBarForeground, text='Search',font=('Helvetica', '12', 'bold'), borderwidth=0, width=10)
        self.searchButton.pack(side=LEFT, expand=True, fill=BOTH)

    # Submit button:
    def submitClick(self):
        self.enteredTicker = self.searchBar.get()

    #Getter
    def getTicker(self):
        return self.enteredTicker


if __name__ == "__main__":
    from GUI import windowGUI
    window = windowGUI.Window()
    search = SearchBarGUI(window.window)
    window.window.mainloop()