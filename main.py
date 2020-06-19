'''
title: main.py
authors: Palaash Kolhe & Shaishav Shah
date created: 2020-06-19
'''

from GUI import engineGUI
import matplotlib.animation as animation

if __name__ == '__main__':
    #
    on = True
    def updateOn():
        global on
        on = False

    #
    window = engineGUI.Engine()
    # Animate
    ani = animation.FuncAnimation(window.fig, window.getGraphClass().animate, fargs=(
    window.getGraphClass().times, window.getGraphClass().values, window.getTicker(), window), interval=2000,
                                  cache_frame_data=False)
    # Running it

    window.getWindow().protocol('WM_DELETE_WINDOW', updateOn)  # To not get Error when window is closed

    while on:
        window.window.update_idletasks()
        window.window.update()
        if window.changed:
            window.updateEverything()
            ani.__init__(window.fig, window.getGraphClass().animate, fargs=(
            window.getGraphClass().times, window.getGraphClass().values, window.getTicker(), window), interval=2000,
                         cache_frame_data=False)