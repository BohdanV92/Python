from random import randint

matrix = [[0 for j in range(10)] for i in range(10)]
matrix_change  = [[0 for j in range(10)] for i in range(10)]

print("Matrix")
for i in range (10):
    for j in range (10):
        matrix[i][j] = randint(0, 100)
        print("%5d"%(matrix[i][j]),end="")
    print()

for i in range (10):
    temp = matrix[i][i]
    matrix[i][i] = matrix[i][9-i]
    matrix[i][9-i] = temp

print("Change diagonals matrix")
for i in range (10):
    for j in range (10):
        print("%5d"%(matrix[i][j]),end="")
    print()
