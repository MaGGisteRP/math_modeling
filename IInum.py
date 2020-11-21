from const import *
from numpy import tan, cos, pi, sqrt
g = 9.81
Hi = 100
B = pi/6 
A = pi/3
speed = sqrt((g*Hi*(tan(B)**2))/(2*(cos(A)**2)*(1-(tan(B))*(tan(A)))))
print (speed)