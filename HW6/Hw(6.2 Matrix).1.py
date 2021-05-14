from random import randint

m = int(input("m - ? "))
n = int(input("n - ? "))

matrix = [[0 for j in range(n+1)] for i in range(m+1)]

print("Old matrix")
for i in range (m):
    for j in range (n):
        matrix[i][j] = randint(0, 100)
        print("%5d"%(matrix[i][j]),end="")
    matrix[i][n] = sum(matrix[i][0:n])
    print()

for j in range(n+1):
    sum_n = 0
    for i in range(m):
        sum_n = sum_n + matrix[i][j]
    matrix[m][j] = sum_n

print("New matrix")
for i in range (m+1):
    for j in range (n+1):
        print("%5d"%(matrix[i][j]),end="")
    print()
