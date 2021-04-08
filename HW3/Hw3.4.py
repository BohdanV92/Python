import math
area = float(input("Enter area of hall: "))
radius = float(input("Enter radius of scene: "))
width = float(input("Enter width of passage: "))
if (math.sqrt(area) / 2 - radius) >= width:
    print ("You can do it")
else:
    print ("You can't do it")
