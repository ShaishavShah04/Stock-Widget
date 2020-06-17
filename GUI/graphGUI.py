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
from matplotlib.figure import Figure
import matplotlib.animation as animation


class GraphGUI:
    def __init__(self,window,fig,graph):
        self.bg = 'gray22'
        self.GraphFrame = Frame(window,height=300,width=700, bg = self.bg)
        self.GraphFrame.grid(row=1,column=1, rowspan=3, sticky=S)
        self.ticker = 'SPY'
        self.hfont = {'fontname':'Helvetica'}
        self.TitleBackground = 'gray12'
        self.TitleForeground = 'white'
        #self.Title = Label(self.GraphFrame,text="{0} Price".format(self.ticker),font=self.font,bg=self.TitleBackground, fg=self.TitleForeground)
        #self.Title.grid(row=2,column=1,rowspan=3,sticky=S)
        self.times = []
        self.values = []
        self.fig = fig
        self.graph = graph

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

    def animate(self,i, x_list, y_list,ticker,window):
        p, t = getLivePrice(ticker)
        p = p.replace(",","")
        write_to_csv(t, p, ticker)
        x_list.append(t)
        y_list.append(float(p))  # It took me 3 hours to figure out why this wasn't working. My data was a string instead of a float
        # Limiting lists to 10 items or else the graph becomes unreadable
        # Formatting the graph
        self.graph.clear()
        self.graph.plot(x_list[-10:], y_list[-10:],'y-')

        if len(x_list)%5==0:
            try: # Making the graph readable
                difference = abs(y_list[-1] - y_list[-2])
                print(difference)
                if difference != 0:
                    difference *= 15
                    plt.ylim(float(p) - difference, float(p) + difference)
            except:
                print('10p')
                plt.ylim(float(p)-(float(p)*0.1),float(p)+(float(p)*0.1))

        plt.xticks(rotation=20, ha='right')
        plt.title('{0} Stock Price - Last Price: {1}'.format(ticker,str(p)))
        plt.ylabel('Price')

        if window.changed:
            window.changed = False


    def changeTicker(self,ticker):
        self.ticker = ticker
