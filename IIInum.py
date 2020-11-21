from const import *
from IInum import *
from numpy import tan, cos, pi, sqrt
T = 200
Epm = 300
Nifigasibe = ((2/(sqrt(pi))) * ((h/(k*T))**(3/2)) * (E**(-Epm/(k*T))) * (Epm**(T/2)))
print (Nifigasibe)