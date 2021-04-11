#1
text = "Beautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.\nReadability counts.\n"
#a
text_upper = text.upper()
#b
text_lower = text.lower()
print ("Python's philosophy:\n%s\n.upper:\n%s\n.lower:\n%s" %(text, text_upper, text_lower))


#2
number = int(input("Enter the natural 4-digits number: "))
if number < 1000 or number > 9999:
    print ("Incorrect number")
else:
    number_str = str(number)
#a
    multiplication = int(number_str[0]) * int(number_str[1]) * int(number_str[2]) * int(number_str[3])
#b
    reverse = number_str[3] + number_str[2] + number_str[1] + number_str[0]
    print ("Multiplication of digits of number: %d\nReverse of number: %s" %(multiplication, reverse))
