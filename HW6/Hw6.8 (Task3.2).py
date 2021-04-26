import random
list1 = []
for item in range (10):
    list1.append(random.randint(1, 10000))
print ("List: ", list1)
print ("Max_index: ", list1.index(max(list1)))
print ("Min_index: ", list1.index(min(list1)))

maxx = max(list1)
index_maxx = list1.index(maxx)
index_minn = list1.index(min(list1))
list1[index_maxx] = min(list1)
list1[index_minn] = maxx

print ("Changed List: ", list1)
print ("Max_index: ", list1.index(max(list1)))
print ("Min_index: ", list1.index(min(list1)))
#--------------------------------------------------------------------

import random
list1 = []
for item in range (10):
    list1.append(random.randint(1, 10000))
print ("List: ", list1)
print ("Max_index: ", list1.index(max(list1)))
print ("Min_index: ", list1.index(min(list1)))

maxx = max(list1)
minn = min(list1)
index_maxx = list1.index(maxx)
index_minn = list1.index(minn)
list1.pop(index_maxx)
list1.insert(index_maxx, minn)
list1.pop(index_minn)
list1.insert(index_minn, maxx)

print ("Changed List: ", list1)
print ("Max_index: ", list1.index(max(list1)))
print ("Min_index: ", list1.index(min(list1)))
