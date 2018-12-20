#Excercise 9 Star Turtle
#Tatum Gray
#2/10/2016

import turtle
wn = turtle.Screen()
fred = turtle.Turtle()
new_color = input("Please enter a color for the turtle:")
new_bgcolor = input("Please enter a color for the background:")
pen_size = input("Now enter in a pen size:")

fred.color(new_color)
wn.bgcolor(new_bgcolor)
fred.pensize(pen_size)

for star in range (5):
    fred.right(144)
    fred.forward(100)
wn.exitonclick()
