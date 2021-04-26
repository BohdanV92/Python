import random
list1 = []
for item in range (30):
    list1.append(random.randint(1, 10))

count = list1.count(list1[0])
count_item = list1[0]

for item in list1:
    if list1.count(item) > count:
        count = list1.count(item)
        count_item = item
        
print ("List: ", list1)
print ("Max count of: %d; Quantity: %d" % (count_item, count))


