"""
Shaishav Shah
Making the graph now using the Matplotlib library
"""
from live_prices import *
import csv

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

import pandas as pd
import numpy as np
import plotly


def makegraph(filename):
    data = pd.read_csv(os.getcwd() + '/StockData/' + filename,
                       names=['Time','Value'],
                       header=None)

def animate(interval,filename='livepricesAMD.csv'):
    with open(os.path.join(os.getcwd()+"/StockData",filename),'r') as f:
        data = f.readlines()
    times = []
    values = []
    for line in data:
        if len(line) > 1:
            x,y = line.split(',')
            times.append(x)
            values.append(y)
    graph.clear()
    graph.plot(times,values)






if __name__ == "__main__":

    style.use('fivethirtyeight')

    fig = plt.figure()
    graph = fig.add_subplot(1,1,1)

    idk = animation.FuncAnimation(fig,animate,interval=1000)

    plt.show()



    # makegraph('livepricesAMD.csv')





