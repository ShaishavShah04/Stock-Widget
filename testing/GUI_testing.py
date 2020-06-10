"""
Working with GUI
"""
from tkinter import *

# Creating main window
window = Tk()
window.minsize(1028,720)
window.resizable(False,False)
window.title('Stock Tracker')
window.configure(background = "grey")

# Trying to create search bar
searchframe = Frame(window,height=70,width=500,pady=3,padx=3)
searchframe.grid(row=0 ,columnspan=3)

#searchframe.pack(side=LEFT)
label_ticker = Label(searchframe,text="ENTER TICKER: ")
#label_ticker.grid(rowspan=2,column=2)
label_ticker.pack(side=LEFT,fill=BOTH,expand=True,pady=30)

searchbar = Entry(searchframe,bg="#978E8E")
#searchbar.grid(rowspan =2,column=9)
searchbar.pack(side=LEFT,fill=BOTH,expand=True)

searchbutton = Button(searchframe,text = "SEARCH",bg = 'green',fg='white')
searchbutton.pack(side = LEFT, expand = True, fill = BOTH)


# Running it
window.mainloop()

