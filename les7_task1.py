import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

t = np.arange(0, 6*np.pi, 0.001)
R = 2

def cycloida():
    x = R*(t - np.sin(t))
    y = R*(1-np.cos(t))
    plt.plot(x, y, color = 'b', label='cycloida')
    plt.xlabel('Coord: x') 
    plt.ylabel('Coord: y')
    plt.axis('equal')
    plt.savefig('task1.png')

def astroida():
    x = R*np.cos(t)**3
    y = R*np.sin(t)**3
    plt.plot(x, y, color = 'b', label='cycloida')
    plt.xlabel('Coord: x') 
    plt.ylabel('Coord: y')
    plt.axis('equal')
    plt.savefig('task1_2.png')

cycloida()
astroida()