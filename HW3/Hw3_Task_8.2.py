number = int(input("Enter a natural number: "))
if number <= 0:
    print ("It's not a natural number")
elif number % 5 == 0:
    print ("Kratne 5")
elif number % 2 != 0:
    print ("Neparne")
else:
    print ("Parne")

