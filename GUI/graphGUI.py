"""
Shaishav Shah
Trying to create a graph GUI
"""
import tkinter as tk
from tkinter import *
import matplotlib
from make_graph import *
matplotlib.use("TkAgg") # Backend of Matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation


class GraphGUI:
    def __init__(self,window):
        self.bg = 'snow'
        self.GraphFrame = Frame(window,height=800,width=700, bg = self.bg)
        self.GraphFrame.grid(row=1,column=1, rowspan=3, sticky=S)
        self.ticker = None
        self.font = ('Helvetica', '12', 'bold')
        #
        fig = Figure(figsize=(7,4), dpi=100)
        graph = fig.add_subplot(1,1,1)
        graph.plot([1,2,3,4,5,6],[1,4,9,16,25,36])
        #
        canvas = FigureCanvasTkAgg(fig,self.GraphFrame)
        canvas.draw()
        #canvas.get_tk_widget().grid(row=1,column=1)
        canvas.get_tk_widget().pack(side=TOP,fill=BOTH,expand=False)
        self.GraphFrame.grid_propagate(0)

        # For interactive graph
        """ Very flashy. Will add later if needed
        chartOptions = NavigationToolbar2Tk(canvas,self.GraphFrame)
        chartOptions.update()
        canvas._tkcanvas.pack(side=TOP,fill=BOTH,expand=False)
        """