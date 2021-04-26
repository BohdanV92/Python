import random
list1 = []
list2 = []
list3 = []
index2 = 0
for item in range (10):
    list1.append(random.randint(1, 10))
for item in range (10):
    numb2 = int(input("Enter number: "))
    list2.append(numb2)
for item in list1:
    numb3 = item + list2[index2]
    index2 += 1
    list3.append(numb3)

#Або так, і тоді не потрібно "index2":
"""
for item in range (10):
    numb3 = list1[item] + list2[item]
    list3.append(numb3)   
"""
    
print ("List1: ", list1)
print ("List2: ", list2)
print ("List3: ", list3)
