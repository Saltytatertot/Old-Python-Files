
#User will enter in a number
print("HeLlO HuMaN. I aM yOur cAlCulAtoR! PlEaSe fOllow iNstrUctiOns")
num1 = float(input("Enter First Number: "))

op = (input("Enter Operator for numbers: "))

num2 = float(input("Enter Second Number: "))
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Sorry Human I have anticipated that! No more Calculations!")
