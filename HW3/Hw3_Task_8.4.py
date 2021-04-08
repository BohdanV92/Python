number = int(input("Enter a number of place: "))
if number < 1 or number > 54:
    print ("Incorrectly")
elif number < 37:
    if number % 2 == 0:
        print ("Верхнє, купе")
    else:
        print ("Нижнє, купе")
else:
    if number % 2 == 0:
        print ("Верхнє, бічне")
    else:
        print ("Нижнє, бічне")
