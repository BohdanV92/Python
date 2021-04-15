# 6
number = float(input("Enter your number: "))
counter = 0
positive = 0
negative = 0 
while number != 0:
    counter += 1
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        break
    number = float(input("Enter your number: "))
positive = positive / counter * 100
negative = negative / counter * 100
print ("Positive numbers = %.1f%%, Negative numbers = %.1f%%" % (positive, negative))

