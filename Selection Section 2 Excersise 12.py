#Selection Section 2 Excersise 12
#Tatum Gray
#3/18/2016

year = int(input("Please enter a Year. "))
if year % 4 != 0:
    print(year, "is not a leap year.")
elif year % 100 != 0:
    print(year, "is a leap year.")
elif year % 400 != 0:
    print(year, "is not a leap year.")
else:
    print(year, "is a leap year.")
