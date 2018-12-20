#Recursion Section 2
#Tatum Gray
#5/3/2016

import turtle

def drawPoly(t,num_sides,side_length,red,green,blue):
    t.begin_fill()
    t.fillcolor(red,green,blue)
    for i in range(num_sides):
        t.forward(side_length)
        t.left(360/num_sides)
    t.end_fill()
    if num_sides > 2:
        drawPoly(t,num_sides-1,side_length,red+10,green+25,blue+35)
def main():
    wn = turtle.Screen()
    wn.bgcolor("magenta")
    wn.colormode(255)
    fred = turtle.Turtle()
    fred.back(25)
    drawPoly(fred,8,100,0,0,0)
    fred.hideturtle()
    wn.exitonclick()
main()

