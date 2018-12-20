#Functions Section 3 Excersise 10
#Tatum Gray
#2/29/2016

import turtle

wn = turtle.Screen()
fred = turtle.Turtle()

def drawstar(t, num):
    for i in range(num):
        t.forward(100)
        t.left(216)
        t.penup()
        t.forward(350)
        t.right(144)
        t.pendown()
num = 5
wn.bgcolor("green")
fred.color('blue')
fred.pensize(10)
def star_star(num):
    for i in range(num):
        drawstar(fred,num)
star_star(num)
wn.exitonclick()
#If the pen was not put up the turtle would make starception, by having 5 stars
#look like they conjoin together to make one big star
