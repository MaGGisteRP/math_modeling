def myfun(a=1,b=0):
    x1 = 3*a - b
    x2 = 3*a + b
    return x1, x2
tmp = myfun(4,3)
print(tmp[0])
print (myfun()[1])