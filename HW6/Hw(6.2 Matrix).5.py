from random import randint

m = int(input("m - ? "))
n = int(input("n - ? "))

matrix_1 = [[0 for j in range(n)] for i in range(m)]
matrix_2 = [[0 for j in range(n)] for i in range(m)]
matrix_max = [[0 for j in range(n)] for i in range(m)]

print("Matrix_1")
for i in range (m):
    for j in range (n):
        matrix_1[i][j] = randint(0, 100)
        print("%5d"%(matrix_1[i][j]),end="")
    print()

print("Matrix_2")
for i in range (m):
    for j in range (n):
        matrix_2[i][j] = randint(0, 100)
        print("%5d"%(matrix_2[i][j]),end="")
    print()

print("Matrix_max")
for i in range (m):
    for j in range (n):
        if matrix_1[i][j] > matrix_2[i][j]:
            print("%5d"%(matrix_1[i][j]),end="")
        else:
            print("%5d"%(matrix_2[i][j]),end="")
    print()
