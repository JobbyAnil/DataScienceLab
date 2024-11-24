import numpy as np

size = int(input("Enter the size of the square matrix: "))

matrix = []

print("Enter each row of the matrix, with elements separated by spaces:")

for i in range(size):

 row = list(map(float, input().split()))

 matrix.append(row)

trans=np.transpose(matrix)

print(trans)
