"""
Shaishav Shah
Making the graph now using the Matplotlib library
This uses all the stuff from live_prices.py...so that file isnt really needed after this
What this code does:
- Directly uses the getliveprice function and plots it.
- Writing it into the csv is not nessasary, but I am writing it for future use

 - 600 * 400

"""
from live_prices import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate2(i,x_list,y_list,ticker):
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
    print(len(y_list)%10)
    if len(y_list) >= 2 and len(y_list)%3 == 0: # Making the graph readable
        difference = abs(y_list[-1] - y_list[-2])
        print(difference)
        if difference != 0:
            difference *= 15
            plt.ylim(float(p)-difference,float(p)+difference)

    plt.xticks(rotation=45, ha='right')
    plt.title('{0} Stock Price'.format(ticker))
    plt.ylabel('Price')


if __name__ == "__main__":
    ticker = 'AAPL'
    fig = plt.figure()
    fig.patch.set_facecolor('#ff0000')
    graph = fig.add_subplot(1,1,1)
    graph.set_facecolor('#0F0F0F')
    times = []
    prices = []
    ani = animation.FuncAnimation(fig,animate2,fargs=(times,prices,ticker),interval=1500)
    plt.show()






