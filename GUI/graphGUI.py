"""
Shaishav Shah
Trying to create a graph GUI
"""
from tkinter import *
import matplotlib
from live_prices import *
matplotlib.use("TkAgg") # Backend of Matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib.animation as animation


class GraphGUI:
    def __init__(self,window,fig,graph):
        self.bg = 'gray22'
        self.GraphFrame = Frame(window,height=300,width=700, bg = self.bg)
        self.GraphFrame.grid(row=1,column=1, rowspan=3, sticky=S)
        self.ticker = 'AMD'
        self.font = ('Helvetica', '12', 'bold')
        self.hfont = {'fontname':'Helvetica'}
        self.times = []
        self.values = []
        self.fig = fig
        self.graph = graph

        # graph.plot([1,2,3,4,5,6],[1,4,9,16,25,36])
        #
        canvas = FigureCanvasTkAgg(self.fig,self.GraphFrame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1,column=1)
        #canvas.get_tk_widget().pack(side=TOP,fill=BOTH,expand=False)
        self.GraphFrame.grid_propagate(0)

        """ Very flashy. Will add later if needed
        chartOptions = NavigationToolbar2Tk(canvas,self.GraphFrame)
        chartOptions.update()
        canvas._tkcanvas.pack(side=TOP,fill=BOTH,expand=False)
        """ # For an interactive graph but its very buggy so am not using it

    def animate(self,i, x_list, y_list,ticker):

        p, t = getLivePrice(ticker)
        write_to_csv(t, p, ticker)
        x_list.append(t)
        y_list.append(float(p))  # It took me 3 hours to figure out why this wasn't working. My data was a string instead of a float
        # Limiting lists to 10 items or else the graph becomes unreadable
        y_list = y_list[-10:]
        x_list = x_list[-10:]
        # Formatting the graph
        self.graph.clear()
        self.graph.plot(x_list, y_list,'y-')
        if len(y_list) >= 2 and len(y_list) % 3 == 0:  # Making the graph readable
            difference = abs(y_list[-1] - y_list[-2])
            print(difference)
            if difference != 0:
                difference *= 15
                plt.ylim(float(p) - difference, float(p) + difference)

        #plt.xticks(rotation=45, ha='right')
        #plt.title('{0} Stock Price'.format(ticker),**self.hfont)
        #plt.ylabel('Price',**self.hfont)

    def changeTicker(self,ticker):
        self.ticker = ticker
