#fffffffffffffffff press f
a = int(input())
b = int(input())
if(b != 0 and a % b == 0):
  print("Делится, остаток: ", a % b, " Частное: ", a // b)
elif(b == 0): print("division by zero")
else: print("Не делится, остаток: ", a % b, " Частное: ", a // b)
#kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkapatxar
a = int(input())
b = int(input())
c = int(input())
x1 = -b/2 + (b**2 - 4*a*c)**0.5
x2 = -b/2 - (b**2 - 4*a*c)**0.5
print(x1, '\n', x2)
