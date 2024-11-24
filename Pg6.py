import numpy as np

import matplotlib.pyplot as plt

x=np.array([23,13,10])

y=np.array([10,20,7])

plt.plot(x)

plt.plot(y)

plt.legend(["orange", "grape"], loc="upper right")

plt.title(“FRUIT SALES”)

plt.show()
