money = int(input("Enter sum of money: "))
if money % 200 == 0:
    print ("You can exchange for 200, 100, 10 and 1 UAH")
elif money % 200 != 0 and money % 100 == 0:
    print ("You can exchange for 100, 10 and 1 UAH")
elif money % 100 != 0 and money % 10 == 0:
    print ("You can exchange for 10 and 1 UAH")
else:
    print ("You can exchange only for 1 UAH")
