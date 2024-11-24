import matplotlib.pyplot as plt

x=[]

y=[]

f=open("sales.txt")

next(f)

for row in f:

row=row.split(' ')

x.append(int(row[0]))

y.append(int(row[1]))

plt.xlabel("Temperature in degree celsius")

plt.ylabel("Sales")

plt.title(“Sales vs Temperature”)

plt.plot(x,y)

plt.show()
