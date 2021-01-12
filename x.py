import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

e = 2.7182818284 

fig, ax = plt.subplots()
anim_object, = plt.plot([],[], '-', Lw = 2)
ax.set_xlim(-20,20)
ax.set_ylim(-20,20)

x,y = [], []

def update(frame):
    x.append(np.sin(frame) * (e**np.cos(frame) - 2*np.cos(4*frame) + (np.sin(frame/12))**5))
    y.append(np.cos(frame) * (e**np.cos(frame) - 2*np.cos(4*frame) + (np.sin(frame/12))**5))
    anim_object.set_data(x,y)
    return anim_object,

anim = FuncAnimation(fig, update(), frames = np.arange(0, 2*np.pi, 0.01),inerval = 100)
anim.save('aaaaaaaaaaaa.gif')

#x,y = [], []

#def update2(frame):
   # x.append(16*(np.sin(frame)**3))
    #y.append(13*np.cos(frame)-5*np.cos(2*frame)-2*np.cos(frame*3)-np.cos(frame*4))
    #anim_object.set_data(x,y)
    #return anim_object,

#anim = FuncAnimation(fig, update, frames = np.arange(0, 2*np.pi, 0.01),inerval = 100)
#anim.save('sev.gif')