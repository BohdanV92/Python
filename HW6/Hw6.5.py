import random

list1 = []
list_buf = []

for item in range (50):
    list1.append(random.randint(-100, 100))
print ("List1: ", list1)

for item in list1:
    if item >= 0:
        list_buf.append(item)

list1 = list_buf
print ("List_changed: ", list1)
#------------------------------------

import random
list1 = []

for item in range (50):
    list1.append(random.randint(-100, 100))
print ("List1: ", list1)

for item in list1:
    for item in list1:
        if item < 0:
            list1.remove(item)

print ("List_changed: ", list1)
