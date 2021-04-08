import math
figure = int(input("Make a choise: '1'-circule, '2'-rectangle, '3'-triangle: "))
if figure < 1 or figure > 3:
    print ("Incorrectly")
elif figure == 1:
    radius = float(input("Enter the radius: "))
    if radius <= 0:
        print ("Incorrectly")
    else:
        area = math.pi * radius ** 2
elif figure == 2:
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    if length <= 0 or width <= 0:
        print ("Incorrectly")
    else:
        area = length * width
else:
    a = float(input("Enter the leg1: "))
    b = float(input("Enter the leg2: "))
    c = float (input("Enter the hypotenuse: "))
    if a <= 0 or b <= 0 or c <= 0 or a + b <= c:
        print ("Incorrectly")
    else:
        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
print ("Area = %.2f " % (area))
