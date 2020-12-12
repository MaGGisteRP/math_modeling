import matplotlib.pyplot as plt
import numpy as np

plt.plot([1,8,3],[5,7,10],label='fignya')
plt.plot([1,8,3,7,5],[5,7,10,6,8],label='fignya_2')
plt.legend()
plt.show()
plt.savefig('pic_1.png')