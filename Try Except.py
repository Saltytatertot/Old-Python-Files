#catching errors in python.

#prevents python from returing an error.
#he gets too broad exception clause in his
#tries to divide by 0



#don't try to except everything. or else nothing will be returned and you want to be
#a good programmer now don't you.
try: 
    Value = 10/0
    #apparently the division error only appears when implemented before number variable
    #if 34/0 is input, then a Value error was printed.
    
    number = int(input("NUMBER: "))
    print(number)
except ZeroDivisionError as err: #as err prints the error instead of returning an error.
    print(err)
except ValueError:
    print("Invalid Input.")

    
