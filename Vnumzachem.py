from math import sin
import numpy as np 

N = 5
M = 4

MN = np.zeros((M , N))
print(MN)

for i in range(M):
    for j in range(N):
       MN[i][j] = (sin(N*(i+1) + M*(j+1)))
       if MN[i][j] < 0 :
           MN[i][j] = 0 
print(MN)
# for i in range(M):
#     l = []
#     for j in range(N)
#     l.append(round(random()*2))
#     prosto_kidem_snus.append(l)
#     print(l)


lol1 = int(input("Перый: ")) 
lol2 = int(input("Второй: ")) 

MN[:,lol1], MN[:,lol2] = MN[:,lol2], MN[:,lol1]
print(MN[:,lol1])
print(MN)
