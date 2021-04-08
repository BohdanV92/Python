year = int(input("Enter a year: "))
if year % 100 == 0:
    print (year // 100, "century")
else:
    print (year // 100 + 1, "century")
if year % 4 == 0:
    print ("A leap year")
else:
    print ("Not a leap year")
