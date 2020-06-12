"""
Shaishav Shah
Making the graph now using the Matplotlib library
This uses all the stuff from live_prices.py...so that file isnt really needed after this
What this code does:
- Directly uses the getliveprice function and plots it.
- Writing it into the csv is not nessasary, but I am writing it for future use


"""
from live_prices import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(i,x_list,y_list,ticker):
    p,t = getLivePrice(ticker)
    write_to_csv(t,p,ticker)
    x_list.append(t)
    y_list.append(float(p)) # It took me 3 hours to figure out why this wasn't working. My data was a string instead of a float
    # Limiting lists to 10 items or else the graph becomes unreadable
    y_list = y_list[-10:]
    x_list = x_list[-10:]
    # Formatting the graph
    graph.clear()
    graph.plot(x_list,y_list)
    # graph.ylim(float(p)-10,float(p)+10)
    plt.xticks(rotation=45, ha='right')
    plt.title('{0} Stock Price'.format(ticker))
    plt.ylabel('Price')


if __name__ == "__main__":
    ticker = 'AMD'
    plt.style.use('dark_background')
    fig = plt.figure()
    graph = fig.add_subplot(1,1,1)
    times = []
    prices = []
    ani = animation.FuncAnimation(fig,animate,fargs=(times,prices,ticker),interval=3000)
    plt.show()






