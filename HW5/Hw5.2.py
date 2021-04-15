# 2
counter = 0
for i in range (10):
    number = int(input("Enter natural number >2: "))
    while number <= 2:
        print ("Incorrect")
        number = int(input("Enter natural number >2: "))
    if number % 5 == 0:
        counter += 1
print (counter)
