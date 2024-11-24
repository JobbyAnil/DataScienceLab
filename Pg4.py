import numpy as np

import matplotlib.pyplot as plt

x=np.array([1,6,2,18])

y=np.array([3,12,10,20])

plt.plot(x,y,color ='r',marker ='o',mfc="y",mec='g',ls=':')

plt.xlabel("x-axis")

plt.ylabel("y-axis")

plt.title("Graph")

plt.show()
