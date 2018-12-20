#Recursion Section 1 Exercise 2
#Tatum Gray
#5/1/2016

def reverse(text):
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]
print(reverse('hello world'))

UserInput = input("Enter a PHRASE to REVERSE: " )

print("." + reverse(UserInput))
