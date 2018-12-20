import turtle
wn = turtle.Screen()
moe = turtle.Turtle()
curly = turtle.Turtle()
larry = turtle.Turtle()

moe.speed(50)
curly.speed(50)
larry.speed(50)

moe.right(90)
curly.left(90)
larry.up(100)

for i in range(360):
    moe.forward(i)
    curly.forward(i)
    larry.forward(i)
    moe.left(1/2*i)
    curly.right(1/2*i)
    larry.right(1/2*i)
wn.exitonclick()
