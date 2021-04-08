number = int(input("Enter a natural number: "))
if number <= 0:
    print ("It's not a natural number")
elif number % 4 == 0:
    print ("Kratne 4")
elif number % 2 == 0:
    print ("Parne")
else:
    print ("Neparne")
