#Python Turtle Graphics Section 3 Square Spiral
#Tatum Gray
#2/17/2016

import turtle
wn = turtle.Screen()
fred = turtle.Turtle()
wn.bgcolor('black')
fred.color('white')

for i in range(0,500,10):
    fred.left(90)
    fred.forward(i)
    
wn.exitonclick()
