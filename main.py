from numpy import *
 
def l1(r):
    return 4/3 * pi * r**3
 
def l2(a,b,c):
    return a*b*c
 
def l3(a,b,c,n):
    w = (a+b+c)/2
    e = 3/4*(sqrt(w * (w-a) * (w-b) * (w-c)))*OH
    return 3/4*(sqrt(p * (w-a) * (w-b) * (w-c)))*OH
    print (e)
 
figyra = input("1)Шар; 2)Прямоугольный парралелепипед; 3)Объем тетраэдра: ")
if figyra == '1':
    rad = float(input("Радиус: "))
    print("Объем шара: %.2f" % l1(rad))
elif figyra == '2':
    r = float(input("Длина: "))
    t = float(input("Ширина: "))
    y = float(input("Высота: "))
    print("Прямоугольный парралелепипедa: %.2f" % l2(r,t,y))
elif figyra == '3':
    AB = float(input("Первая сторона: "))
    BC = float(input("Вторая сторона: "))
    CA = float(input("Третья сторона: "))
    OH = float(input("Высота: "))
    print("Объем тетраэдра: %.2f" % l3(AB,BC,CA,OH))