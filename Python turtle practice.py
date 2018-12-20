import turtle
wn = turtle.Screen()
fred = turtle.Turtle()

for i in range(4):
    fred.forward(100)
    fred.right(90)
for n in range(1):
    fred.right(90)
    fred.forward(100)
fred.goto(6.25,0)
for n in range(1):
    fred.right(90)
    fred.forward(100)
wn.exitonclick()
