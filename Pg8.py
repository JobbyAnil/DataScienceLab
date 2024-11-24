import numpy as np

import matplotlib.pyplot as plt

x=np.array([88,92,18,89,100,80,60,100,80,34])

y=np.array([35,79,79,48,100,88,32,45,20,30])

plt.title('Scatter Plot: Mathematics vs Science')

plt.grid(True)

plt.scatter(x,y)

plt.xlabel("Maths mark")

plt.ylabel("Science mark")

plt.title("MARKS")

plt.show()
