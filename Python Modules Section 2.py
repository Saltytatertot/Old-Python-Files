#Python Modules Section 2
#Tatum Gray
#3/10/2016
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')

fred = turtle.Turtle()
wn.setworldcoordinates(0,-1.25,360,1.25)

fred.penup()
for angle in range(360):
    y = math.cos(math.radians(angle))
    fred.goto(angle, y)
    fred.pendown()
    #print(y)

wn.exitonclick()
