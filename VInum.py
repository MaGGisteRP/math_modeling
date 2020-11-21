from random import random
ok = 8
mi = 7
pristo_kidem_snus = []
for i in range(ok):
    chasto_ne_ponimaia_vkus = []
    for j in range(mi):
        chasto_ne_ponimaia_vkus.append(round(random()*2))
    pristo_kidem_snus.append(chasto_ne_ponimaia_vkus)
    print(chasto_ne_ponimaia_vkus)
 
c1 = int(input("Перый: ")) 
c2 = int(input("Второй: "))

for i in range(ok):
    ok[i][c1], ok[i][c2] = ok[i][c2], ok[i][c1]
    print(ok[i])