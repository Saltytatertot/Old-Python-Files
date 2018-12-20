#Exponent Simply provided by the python shell
#print(2**3)

#example of using for loops to create something the code is already capable of doing.

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
#'int' should be used for converting input whole numbers into useable code
#'float'can be used for non integar values; just so long as they go before the input is called.


base_User = float(input("Enter a number you want for the base of the exponent: "))
pow_User = float(input("Enter the exponent variable: "))
print(raise_to_power(base_User,pow_User))
