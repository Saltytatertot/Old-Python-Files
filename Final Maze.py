#Final Program Invisible maze
#Tatum Gray
#5/14/2016

import turtle
fred = turtle.Turtle()
wn = turtle.Screen()

difficulty = int(input("""Before you get started, pick a difficulty.
1 for Easy.
2 for Hard.
"""))

if difficulty == 2:
    fred.penup()
else:
    print("Easy it is.")
fred.fd(60)


wn.exitonclick
