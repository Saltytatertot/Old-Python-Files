#Minecraft Tile Program
#Tatum Gray
#2/19/16

import turtle
wn = turtle.Screen()
steve = turtle.Turtle()

steve.fillcolor('brown')
steve.begin_fill()

for i in range(4):
    steve.forward(100)
    steve.right(90)
steve.end_fill()
steve.fillcolor('green')
steve.begin_fill()
steve.right(90)
steve.forward(10)
steve.left(90)
steve.forward(10)
steve.right(90)
steve.forward(20)
steve.left(90)
steve.forward(20)
steve.left(90)
steve.forward(10)
steve.right(90)
steve.forward(30)
steve.right(90)
steve.forward(20)
steve.left(90)
steve.forward(20)
steve.left(90)
steve.forward(30)
steve.right(90)
steve.forward(20)
steve.left(90)
steve.forward(10)
steve.end_fill()
wn.exitonclick()


