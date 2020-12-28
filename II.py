import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots() #создание пространства и подпространства
anim_object, = plt.plot([],[],'-',lw=2) # объект анимации
xdata, ydata = [], [] #координаты объекта анимации
ax.set_xlim(0,2*np.pi)
ax.set_xlim(-1,1)
def update(frame):
    xdata.append(frame) # рассщёт координаты x
    ydata.append(np.sin(frame)) # рассщёт координаты y
    anim_object.set_data(xdata, ydata) #передача координат
    return anim_object,
ani = FuncAnimation(fig,update,frames = np.arange(0, 2*np.pi, 0.1),interval=100)
ani.save('II_animation.gif')

