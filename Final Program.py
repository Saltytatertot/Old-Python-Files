#Final Program
#Tatum Gray
#5/14/2016

#This Program follows the style of a Choose Your Own Adventure Book.

ent = "(Press Enter)"
print("Welcome to -Title-, a Choose Your Own Adventure Story.")
print()
name = input("To get started, what is your name? >> ")
print()
print(name, "is a perfect name to start your story.")
print()
writ = input("""To get yourself familiar with what you'll will have to do,
here is a sample choice; Do you like apples or oranges better?""" + ent)
choiceX = int(input("""
1:Apples \t\t 2:Oranges
"""))

def choose(choice,resp1,resp2,extra):   #Resp is a response the program will give.
    if choice == 1:
        print(resp1)
    elif choice == 2:
        print(resp2)
    else:
        print(extra)
choose(choiceX,"I like apples better too.","I prefer the juice to the fruit myself.","Come on get with the program.")
print()
Alright = input("Alright I think you have the hang of it now." + ent)
