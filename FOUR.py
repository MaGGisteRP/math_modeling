import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
obj, = plt.plot([],[],'o',color='r',label='Ball')

x, y = [],[]

a = 0.16
b = 0.19

def xf(n):
    if n>0:
        return  (xf(n-1)**2) - (yf(n-1)**2) + a
    return 0.1


def yf(n):
    if n>0:
        return 2*xf(n-1)*xf(n-1) + b
    return 0.1
def func(n):
    print("\r\t\r", n)
    x.append( xf(n) )
    y.append( yf(n) )
    obj.set_data(x,y)


ani = FuncAnimation(fig, func, frames=np.arange(0,25,1), interval = 100)
ani.save("skfks.gif")
