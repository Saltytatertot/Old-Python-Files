#Selection Section 1 Excersise 6
#Tatum Gray
#3/17/2016
import math

def findHypot(a,b):
    a = a ** 2
    
    b = b ** 2
    c = a + b
    c = math.sqrt(c)
    return c

a = int (input("Enter a side length: "))
b = int (input("Enter another side length: "))
if a < 0 or b < 0:
    print("A poitive value is required, please try again.")
else:
    print(findHypot(a,b))
