from math import sin
import numpy as np 

print = ("Введите элементы матрицы")
N = 4
M = 3

i = int(input(""))
j = int(input(""))

sss = []

#Chto_eto_takoe = np.array([i, j])
#Chto_eto_takoe2 = np.array([N, M])

for i in range (M):
    for j in range (N):
        a = []
        a.append(sin(N*(i+1) + M*(j+1)))
    sss.append(a)

for i in range (M):
    for j in range (N):
        if sss [i][j] < 0:
            sss [i][j] = 0 
            print (str(sss[i][j]))
        else:
            print (str(sss[i][j]))
