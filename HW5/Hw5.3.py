# 3 (Multiplication to 9)
print("%4s%4s%4s%4s%4s%4s%4s%4s%4s%4s" % ('n','1','2','3','4','5','6','7','8','9'))
for n in range (1, 10):
    print("%4d%4d%4d%4d%4d%4d%4d%4d%4d%4d" % (n,n,2*n,3*n,4*n,5*n,6*n,7*n,8*n,9*n))

"""
???? як, щоб вийшло рядки...?
for n in range (1, 10):
    for a in range (1, 10): 
        print("%4d" % (n*a))
"""
