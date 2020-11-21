from math import sin
import numpy as np 

N = 8
M = 4

MN = np.zeros((M , N))
print(MN)

for i in range(M):
    for j in range(N):
       MN[i][j] = (sin(N*(i+1) + M*(j+1)))
       if MN[i][j] < 0 :
           MN[i][j] = 0 
print (str(MN))

