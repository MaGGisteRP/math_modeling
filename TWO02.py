import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
anim_boject, = plt.plot([],[], '-', Lw = 2)
plt.axis('equal')
ax.set_xlim(-2*np.pi, -2*np.pi)
ax.set_ylim(-2*np.pi, -2*np.pi)
def circle(r0, t0):
    lol = np.arange(0, 2*np.pi, 0.01)
    r = r0 * t0
    x = r*np.cos(lol)
    y = r*np.sin(lol)
    return x, y
def update(frame):
    anim_boject.set_data(circle(0.1, frame))
anim = FuncAnimation(fig, update, frames = 500, interval = 30)
anim.save('circle_move.gif')