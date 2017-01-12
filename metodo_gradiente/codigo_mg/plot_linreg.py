#! /usr/bin/python

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def plot_linreg(X,Y,a,b,interactive=False):
    if interactive:
        plt.ion
    r = np.linspace(0,30,1000)
    plt.scatter(X,Y, marker='x',color='r')
    plt.plot(r, map(lambda x: a*x +b, r) , color='b')
    plt.ylabel("Precio en $10000", fontsize=12)
    plt.xlabel("Poblacion en 10000es", fontsize=12)
    plt.xlim([4,25])
    if interactive:
        plt.plot(r, map(lambda x: 1.1930*x -3.8957, r) , color='c')
        plt.pause(0.01)
        plt.clf()
    else:
        plt.show()


