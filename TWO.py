import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
obj, = plt.plot([],[],'o',color='r',label='Ball')
plt.axis('equal')
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)


def circlepainter(r0, T):
    lol = np.arange(0,np.pi,0.01)
    R=r0*T
    x = np.cos(lol)*R
    y = np.sin(lol)*R
    return x,y 
    
def anim(frame):
    obj.set_data(circlepainter)



ani = FuncAnimation(fig, anim, frames=np.arange(0, 2*np.pi, 0.01), interval = 100 )
ani.save("skfks.gif")