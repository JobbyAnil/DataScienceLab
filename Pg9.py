import numpy as np

importmatplotlib.pyplot as plt

x=["Java","Python","Php","Javascript","c#","Cpp"]

y=np.array([22.2,17.6,8.8,8,7.7,6.7])

plt.pie(y,labels=x)

plt.title("Popularity of programming languages")

plt.show()
