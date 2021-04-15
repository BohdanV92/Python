# 1
import random
print("Guess the number in [0:100]. You have 10 attempts!")
a = random.randint(0, 101)
for i in range (10):
    choise = int(input("Enter number: "))
    if choise > a:
        print("Too big")
    elif choise < a:
        print("Too small")
    else:
        print ("You guessed!")
        break
if choise != a:
    print("Number = %d\nTry again!"%(a))
