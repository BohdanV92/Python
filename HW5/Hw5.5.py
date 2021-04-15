# 5
P = int(input("Enter first number: "))
H = int(input("Enter second number (more than the first number): "))
while P >= H:
    print("Error")
    P = int(input("Enter first number: "))
    H = int(input("Enter second number (more than the first number): "))
n = int(input("Enter your number: "))
summ = 0
mult = 1
counter = 0
while n != P or n != H:
    if n < P:
        summ += n
    elif n > H:
        mult *= n 
    elif P < n < H:
        counter += 1
    else:
        break
    n = int(input("Enter your number: "))
print ("Sum = %d, Multiplication = %d, Counter = %d" % (summ, mult, counter))
