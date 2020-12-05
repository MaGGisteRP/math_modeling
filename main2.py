
def summm(a):
    z = len(a) 
    s = 0
    for i in range(z):
        c = s + a[i]
        s = c
    x = c/z
    return x
 
summm([1,2,3,4])