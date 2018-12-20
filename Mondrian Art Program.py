#Mondrian Art Program
#Tatum Gray
#4/3/2016

import random
import turtle
fred = turtle.Turtle()
wn = turtle.Screen()
wn.colormode(255)

wn.bgcolor('black')
fred.speed(100)
fred.hideturtle()

rectamount = int(input('How many rectangle should be drawn? '))
width = int(input('What should the maximum WIDTH be? '))
heigth = int(input('What should the maximum HEIGHT be? '))
width = max(10,width)
heigth = max(10,heigth)
def rectangle(w,h,t):
    for i in range(2):
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
def mondrian (rectamount,t,width,heigth):
    for i in range(rectamount):
        t.pu()
        width = random.randint(10,width)
        heigth = random.randint(10,heigth)
        t.setx(random.randrange(-300,300))
        t.sety(random.randrange(-200,200))
        red =(random.randint(0,255))
        green =(random.randint(0,255))
        blue =(random.randint(0,255))
        newColor = (red,green,blue)
        t.fillcolor(newColor)
        t.color(newColor)
        t.begin_fill()
        t.pd()
        rectangle(width,heigth,fred)
        t.end_fill()  
mondrian(rectamount,fred,width,heigth)
wn.exitonclick()

