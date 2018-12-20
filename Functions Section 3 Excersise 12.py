#Functions Section 3 Excersise 12
#Tatum Gray
#3/1/2016

import turtle
wn = turtle.Screen()
fred = turtle.Turtle()

def drawSprite(t,legnum,leglength):
    angle = 360/legnum
    t.shape('arrow')
    for i in range(legnum):
        t.right(angle)
        t.forward(leglength)
        t.stamp()
        t.backward(leglength)

drawSprite(fred,15,120)

wn.exitonclick()
