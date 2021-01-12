import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def one(R = 10):
    T = np.arange(0, 2*np.pi, 0.01)
    x = R(T - np.sin**3*(T))
    y = R(T-np.cos**3*(T))
    plt.plot(x, y, lw=1)
    plt.axis('equal')
    plt.show()


def two(r=5):
    t = np.arange(0, 2*np.pi, 0.01)
    X = r*np.cos(t)**3
    Y = r*np.sin(t)**3
    plt.plot(X, Y, lw=1)
    plt.axis('equal')
    plt.show()
