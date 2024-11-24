import numpy as np

n=int(input("Enter the size of an array:"));

arr=[]

for i in range (n):

 x = list(map(int,input().split()))

 arr.append(x)

d=np.linalg.det(arr)

print("Determinant")

print(int(round(d)))
