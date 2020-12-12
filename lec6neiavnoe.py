import matplotlib.pyplot as plt
import numpy as np

def circle_plotter(radius = 10):
    x =np.arange(-2*radius, 2*radius, 0.1)
    y =np.arange(-2*radius, 2*radius, 0.1)
    rad = np.linspace(0,10,120)
    x, y = np.meshgrid(x,y)
    fxy = x**2 + y**2
    plt.contour(x, y, fxy, levels = rad**2)
    plt.axis('equal')
    plt.show()
circle_plotter()