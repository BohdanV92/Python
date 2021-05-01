from random import randint

matrix = [[0 for j in range(4)] for i in range(5)]

for i in range (5):
    for j in range (3):
        matrix[i][j] = randint(0, 100)
        print("%4d" % (matrix[i][j]), end="")
    print()
    matrix[i][3] = sum(matrix[i][0:3])

for i in range (5):
    for j in range (4):
        print("%5d"%(matrix[i][j]),end="")
    print()

