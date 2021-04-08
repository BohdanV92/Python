number = int(input("Введіть ціле число: "))
length = str(number)

if number == 0:
    print ("Нуль")
elif number > 0:
    sign = "Додатнє"
else:
    sign = "Від'ємне"

if "-" in length:
    length = len(length) - 1
else:
    length = len(length)

print (sign, length, "-значне число")
