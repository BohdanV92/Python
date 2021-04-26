import random
list1 = []
index_even_numbers = []

for item in range (100):
   list1.append(random.randint(1, 100))  

n = -1
for item in list1:
    n += 1
    if item % 2 == 0:
        index_even_numbers.append(n)
            
print ("List1: ", list1)
print ("Index_even_numbers: ", index_even_numbers)


