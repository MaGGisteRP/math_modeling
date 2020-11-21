from const import *
import numpy as np

print ('Введите начальные координаты тела для x0 и для y0 ')
x0 = int(input("x0: "))
y0 = int(input('y0: '))
print ('Введите начальную скорость тела')
V0 = int(input('V0: '))

t = 5
x = (x0 + V0*t)
y = (y0 + V0*t + (-9.8*t**2)/2)

Afiget = np.array([t, x, y])
print (Afiget)