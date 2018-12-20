import turtle
wn = turtle.Screen()
fred = turtle.Turtle()

fred.speed(100)

for i in range(350):
    fred.forward(i)
    fred.left(70)
    fred.forward(-i)
    fred.left(90)
wn.exitonclick()
