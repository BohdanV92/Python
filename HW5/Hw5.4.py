# 4
a = input("Enter first symbol: ")
b = input("Enter second symbol: ")
for n in range (1,11):
    if n == 1 or n == 10:
        print ("%s" % (a*7))
    else:
        print ("%s%s%s" % (a, b*5, a))
