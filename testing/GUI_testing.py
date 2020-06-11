"""
Copy of palaash's GUI since its better. I will continue to work on it tho
"""

from tkinter import *

window = Tk()
window.minsize(1028, 720)
window.title("Stock App")
window.configure(background = "black")

# common variables
searchBarBackground = 'gray12'
searchBarForeground = 'white'


# Search bar Stuff
#
def submitClick():
    ticker = searchBar.get()
    print(ticker)
#
searchBarFrame = Frame(window, height = 55, width = 600, pady = 5, padx = 5, bg=searchBarBackground)
searchBarFrame.grid(row=0, columnspan=3)

tickerLabel = Label(searchBarFrame, text="Enter Ticker: ", font=('Helvetica', '12', 'bold'), bg=searchBarBackground, fg=searchBarForeground)
tickerLabel.pack(side=LEFT, fill=BOTH, expand=True, pady=5, padx=20)

searchBar = Entry(searchBarFrame, bg='gray22', width=45, fg=searchBarForeground, font=('Helvetica', '12', 'bold'), borderwidth=0)
searchBar.pack(side=LEFT, expand=True, fill=BOTH)

searchButton = Button(searchBarFrame, command=submitClick, bg='gray16', fg=searchBarForeground, text='Search', font=('Helvetica', '12', 'bold'), borderwidth=0, width=10)
searchButton.pack(side=LEFT, expand=True, fill=BOTH)

window.mainloop()

