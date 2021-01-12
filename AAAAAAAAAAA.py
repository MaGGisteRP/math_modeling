import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

e = 2.7182818284 

fig, ax = plt.subplots()
anim_object, = plt.plot([],[], '-', Lw = 2)
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)

x,y = [], []

def update(frame):
    x.append(np.sin(frame)) * (e**np.cos(frame) - 2*np.cos(4*frame) + (np.sin(frame/12))**5))
    y.append(np.cos(frame)) * (e**np.cos(frame) - 2*np.cos(4*frame) + (np.sin(frame/12))**5))
    anim_object.set_data(x,y)
    return anim_object,

anim = FuncAnimation(fig, update, frames = np.arange(0, 12*np.pi, 0.01),
anim.save('aaaaaaaaaaaa.gif')