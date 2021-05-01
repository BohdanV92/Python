from random import randint

m = int(input("m - ? "))
n = int(input("n - ? "))

matrix = [[0 for j in range(n)] for i in range(m)]

print("Matrix:")
for i in range (m):
    for j in range (n):
        matrix[i][j] = randint(0, 100)
        print("%4d"%(matrix[i][j]),end="")
    print()

row_0_sort = sorted(matrix[0][0:n]) ## Сортуєм 0й рядок
print("Row_0_sort: ", row_0_sort, sep = "\n")

for j in range(n):   ## Без цього "for" на великих кількостях стовпців, де часто повторяються числа в 0-му рядку - НЕ всі переставляє ...
    for j in range(n):
        if matrix[0][j] == row_0_sort[j]: 
            continue
        else:
            j_next = (matrix[0][0:n]).index(row_0_sort[j])  ## Індекс елемента в 0-му рядку матриці, який потрібно переставити на "j-те" місце
            for i in range(m):
                buf = matrix[i][j]
                matrix[i][j] = matrix[i][j_next]
                matrix[i][j_next] = buf
                
##            for i in range (m):
##                for j in range (n):
##                    print("%4d"%(matrix[i][j]),end="")
##                print()
##            print()
            
print("Change colomns matrix:")
for i in range (m):
    for j in range (n):
        print("%4d"%(matrix[i][j]),end="")
    print()


    
