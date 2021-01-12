import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
obj, = plt.plot([],[],'o',color='r',label='box')
plt.axis('equal')
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)

def box0(a,b,c,d):
    x0 = 
