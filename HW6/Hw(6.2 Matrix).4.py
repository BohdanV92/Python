from random import randint

matrix = [[0 for j in range(5)] for i in range(5)]

for i in range (5):
    for j in range (5):
        matrix[i][j] = randint(0, 100)
        print("%5d"%(matrix[i][j]),end="")
    print()

list_min = []

for j in range(5):
    min_n = matrix[0][j]
    for i in range(5):
        if matrix[i][j] < min_n:
            min_n = matrix[i][j]
    list_min.append(min_n)

print("Row of min numbers in colomns: ", list_min)

max_of_min = max(list_min)

print("Max element in Row-min: %d" % (max_of_min))
