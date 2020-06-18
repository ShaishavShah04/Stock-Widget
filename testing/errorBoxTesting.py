from tkinter import *

errorWindow = Tk()
errorWindow.wm_title("Error")
errorWindow.geometry("250x100")
errorWindow.resizable(False, False)
errorWindow.configure(bg='gray20')

enteredTicker = 'kfekfoe'

message = Label(errorWindow, text='No results found for "{ticker}"'.format(ticker=enteredTicker), fg='white', bg='gray20', font=('Helvetica', '13'), justify=CENTER, padx=10, pady=10)
message.pack(side='top', expand=Y)

button = Button(errorWindow, text='OK', command=errorWindow.destroy, bg='gray38', fg='white', width=15, height=1, borderwidth=0, font=('Helvetica', '10', 'bold'))
button.pack(side='bottom', expand=Y)

message.rowconfigure(0, weight=100)
message.rowconfigure(1, weight=100)
message.columnconfigure(0, weight=100)

errorWindow.grid_propagate(0)

if __name__ == '__main__':
    errorWindow.mainloop()