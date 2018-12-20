#Excersice 6, User Shape Program
#Tatum Gray
#2/11/2016

import turtle
wn = turtle.Screen()
fred = turtle.Turtle()

side_number = input("Enter in a side number:")
side_length = input("Enter in a side length:")
pen_color = input("Enter in a side color:")
fill = input("Enter in a shape color:")

user_side_number = int(side_number)
user_side_length = int(side_length)

fred.begin_fill()

for shape in range(user_side_number):
	fred.color(pen_color)
	fred.forward(user_side_length)
	fred.left(360/user_side_number)
fred.color(fill)
fred.end_fill()

wn.exitonclick()
