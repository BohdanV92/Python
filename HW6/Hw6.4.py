import random

list1 = []
list_positive = []
list_negative = []

for item in range (20):
    list1.append(random.randint(-5, 5))

for item in list1:
    if item > 0:
        list_positive.append(item)
    elif item < 0:
        list_negative.append(item)
    else:
        continue        

print ("List1: ", list1)
print ("List_positive: ", list_positive)
print ("List_negative: ", list_negative)
