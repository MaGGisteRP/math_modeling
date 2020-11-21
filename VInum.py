from random import random
ok = 8
mi = 4
prosto_kidem_snus = []
for i in range(ok):
    chasto_ne_ponimaia_vkus = []
    for j in range(mi):
        chasto_ne_ponimaia_vkus.append(round(random()*2))
    prosto_kidem_snus.append(chasto_ne_ponimaia_vkus)
    print(chasto_ne_ponimaia_vkus)
 
lol1 = int(input("Перый: ")) 
lol2 = int(input("Второй: ")) 

for i in range(ok):
    ok[i][lol1]= ok[i][lol2]
    print(ok[i])