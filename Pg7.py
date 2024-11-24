import numpy as np

import matplotlib.pyplot as plt

x=np.array(["Java","python","Php","Javascript","c#","Cpp"])

y=np.array([5,17.6,8.8,8,7.7,6.7])

plt.bar(x,y,color="r")

plt.title("Languages vs Popularity")

plt.xlabel("Programming languages")

plt.ylabel("popularity")

plt.show()
