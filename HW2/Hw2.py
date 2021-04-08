import math

1
weight = int(input("Введіть вагу в грамах: "))
tonne = weight / 1000 ** 2
print (tonne, "t")
kilogram = weight / 1000
print (kilogram, "kg")

2
byte = float(input("Введіть кількість байтів: "))
kiloByte = byte / 1024
print (kiloByte, "kB")
megaByte = byte / 1024 ** 2
print (megaByte, "MB")

3
number1 = input("Введіть перше число: ")
number2 = input("Введіть друге число: ")
if '.' in number1:
    number1 = float(number1)
else:
    number1 = int(number1)
if '.' in number2:
    number2 = float(number2)
else:
    number2 = int(number2)
number1, number2 = number2, number1
print ("number1 =", number1)
print ("number2 =", number2)
    # назад:
buffer = number1
number1 = number2
number2 = buffer
print ("number1 =", number1)
print ("number2 =", number2)

4
length = float(input("Введіть довжину прямокутника: "))
width = float(input("Введіть ширину прямокутника: "))
area = length * width
print ("Area =", area)
perimeter =  (length + width) * 2
print ("Perimeter =", perimeter)

5
radius = float(input("Введіть радіус кола: "))
area = math.pi * radius ** 2
print ("Area = %.2f" %(area))
circumference = 2 * math.pi * radius
print ("Circumference = %.2f" %(circumference))

6
length1 = float(input("Введіть довжину 1го катета: "))
length2 = float(input("Введіть довжину 2го катета: "))
hypotenuse = math.sqrt(length1 ** 2 + length2 ** 2)
print ("Hypotenuse = %.3f" %(hypotenuse))
