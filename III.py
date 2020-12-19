import matplotlib.pyplot as plt
import numpy as np

def circle_plotter(radius=10):
    x = np.arange(-2*radius, 5*radius, 0.1)
    y = np.arange(-2*radius, 5*radius, 0.1)
    X, Y = np.meshgrid(x, y)
    fxy = X**2 + Y**2
    plt.contour(X, Y, fxy, levels=[radius**2])
    plt.title('lool')
    plt.axis('equal')
    plt.show()
circle_plotter()