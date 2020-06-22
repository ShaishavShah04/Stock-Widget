"""
Shaishav Shah
Trying to create a graph GUI

"""
from tkinter import *
import matplotlib
from live_prices import write_to_csv, getLivePrice
matplotlib.use("TkAgg") # Backend of Matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt

class GraphGUI:
    def __init__(self,window,fig,graph):
        self.GraphFrame = Frame(window,height=300,width=700, bg = 'grey22')
        self.GraphFrame.grid(row=1,column=1, rowspan=3, sticky=S)
        self.ticker = 'SPY'
        self.hfont = {'fontname':'Helvetica'}
        self.TitleBackground = 'gray12'
        self.TitleForeground = 'white'
        self.times = [] # Arrays for the time and values
        self.values = []
        self.fig = fig
        self.graph = graph


        # Drawing the graph on a Tkinter canvas
        canvas = FigureCanvasTkAgg(self.fig,self.GraphFrame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1,column=1)
        self.GraphFrame.grid_propagate(0)

    def animate(self,i, x_list, y_list,ticker,window):
        p, t = getLivePrice(ticker)
        p = p.replace(",","")
        write_to_csv(t, p, ticker)
        x_list.append(t)
        y_list.append(float(p))  # It took me 3 hours to figure out why this wasn't working. My data was a string instead of a float
        # Limiting lists to 10 items or else the graph becomes unreadable
        # Formatting the graph
        self.graph.clear()
        self.graph.plot(x_list[-10:], y_list[-10:],'y-') # Limiting graph list to 10 for the scrolling effect.

        if len(x_list)%5==0: # Changing the upper and lower bounds of the graph to make it look nice
            try: # Making the graph readable
                difference = abs(y_list[-1] - y_list[-2])
                if difference != 0:
                    difference *= 15
                    plt.ylim(float(p) - difference, float(p) + difference)
            except:
                plt.ylim(float(p)-(float(p)*0.1),float(p)+(float(p)*0.1)) # If the above method doesn't work, just add a 10% price change on the graph

        plt.xticks(rotation=20, ha='right')
        plt.title('{0} Stock Price - Last Price: {1}'.format(ticker,str(p)))
        plt.ylabel('Price')

        if window.changed:
            window.changed = False


    def changeTicker(self,ticker):
        self.ticker = ticker
