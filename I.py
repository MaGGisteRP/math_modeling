import matplotlib.pyplot as plt

x = [1,5,5,1,1]
y = [1,1,5,5,1]

plt.plot(x,y,color='r',label='luchte',marker="o",ms=5)
plt.axis('equal')

plt.show()