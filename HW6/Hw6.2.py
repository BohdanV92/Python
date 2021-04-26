list1 = []
for item in range (10):
    numb = float(input("Enter real number: "))
    list1.append(numb)
summ = sum(list1)
mult = 1
for item in list1:
    mult *= item
print ("List1: ", list1)
print ("Sum: %.2f; Multiplication: %.2f" % (summ, mult))

