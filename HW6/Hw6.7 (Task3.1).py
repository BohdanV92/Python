import random
list1 = []
list_unique = []

for item in range (10):
    list1.append(random.randint(1, 10))

for item in list1:
    if list1.count(item) == 1:
        list_unique.append(item)

print ("List: ", list1)
print ("Unique elements: ", list_unique)
