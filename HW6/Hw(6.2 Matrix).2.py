from random import randint

m = int(input("m - ? "))
n = int(input("n - ? "))

matrix = [[0 for j in range(n)] for i in range(m)]

quantity = 0
for i in range (m):
    for j in range (n):
        matrix[i][j] = randint(0, 1000)
        print("%4d" % (matrix[i][j]), end="")
        if len(str(matrix[i][j])) == 2:
            quantity += 1
    print()

print("Quantity two-digit numbers: ", quantity)
