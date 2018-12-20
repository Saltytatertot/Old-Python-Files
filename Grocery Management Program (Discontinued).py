#Final Program
#Tatum Gray
#5/12/2016

#This Program follows the style of a Choose Your Own Adventure Book.

print("Welcome to -Title-.")

name = input("To get started, what is your name? >> ")
print()
print(name,  "is a perfect name to start your story.")
print()
ent = "(Press Enter)"
writ = input("""To get yourself familiar with what you'll will have to do,
here is a sample choice; Do you like apples or oranges better?""" + ent)
def choice():
    writ
    choiceX = int(input("""
1: Apple\t\t 2: Orange
"""))
    if choiceX == 1:
        print("I like apples better too.")
    elif choiceX == 2:
        print("I prefer the juice to the fruit myself.")
    else:
        print("Come on get with the program.")
        choice()
choice()
