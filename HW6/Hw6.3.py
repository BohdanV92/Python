import random

list1 = []
zero = 0
positive = 0
negative = 0

for item in range (20):
    list1.append(random.randint(-5, 4))

for item in list1:
    if item > 0:
        positive += 1
    elif item < 0:
        negative += 1
    else:
        zero += 1   

print ("List1: ", list1)
print ("Positive: %d; Negative: %d; Zero: %d" % (positive, negative, zero))
