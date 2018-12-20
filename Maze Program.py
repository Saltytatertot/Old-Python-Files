#Fianl Program Maze
#Tatum Gray
#5/14/2016

#This is a maze that you have to navigate using simple commands and turtles.

import turtle
userTurtle = turtle.Turtle()
draw = turtle.Turtle()
scr = turtle.Screen()

def drawMaze():
    draw.pencolor("gold")
    draw.pensize(3)
    draw.penup()
    draw.goto(0,-180)
    draw.pendown()
    draw.speed(10)
    draw.setheading(180)
    draw.fd(180)
    draw.setheading(90)
    draw.fd(60)
    draw.setheading(0)
    draw.fd(120)
    draw.backward(120)
    draw.setheading(90)
    draw.fd(300)
    draw.setheading(0)
    draw.fd(120)
    draw.setheading(-90)
    draw.fd(120)
    draw.setheading(180)
    draw.fd(60)
    draw.setheading(90)
    draw.fd(60)
    draw.setheading(-90)
    draw.fd(120)
    draw.setheading(90)
    draw.fd(60)
    draw.setheading(0)
    draw.fd(120)
    draw.setheading(-90)
    draw.fd(60)
    draw.setheading(0)
    draw.fd(60)
    draw.setheading(-90)
    draw.fd(60)
    draw.backward(60)
    draw.setheading(0)
    draw.fd(60)
    draw.setheading(90)
    draw.fd(60)
    draw.penup()
    draw.setheading(180)
    draw.fd(60)
    draw.pendown()
    draw.setheading(90)
    draw.fd(60)
    draw.setheading(180)
    draw.fd(60)
    draw.setheading(90)
    draw.fd(60)
    draw.setheading(0)
    draw.fd(120)
    draw.setheading(-90)
    draw.fd(60)
    draw.backward(60)
    draw.setheading(0)
    draw.fd(60)
    draw.setheading(-90)
    draw.fd(240)
    draw.setheading(180)
    draw.fd(60)
    draw.setheading(-90)
    draw.fd(60)
    draw.setheading(180)
    draw.fd(120)
    draw.setheading(90)
    draw.fd(60)
    draw.setheading(180)
    draw.fd(60)
    draw.setheading(90)
    draw.fd(60)
    draw.backward(60)
    draw.setheading(180)
    draw.fd(60)
    draw.penup()
    draw.setheading(0)
    draw.fd(300)
    draw.pendown()
    draw.setheading(-90)
    draw.fd(120)
    draw.setheading(180)
    draw.fd(120)
    draw.ht()
    
    userTurtle.penup()
    userTurtle.goto(-30,180)
    userTurtle.setheading(-90)
    
def mazeGame():
    scr.bgcolor("#0070ff")

def m1():
    userTurtle.setheading(90)
    userTurtle.fd(30)
    userTurtle.pos()
    print(userTurtle.pos())

def m2():
    userTurtle.setheading(180)
    userTurtle.fd(30)
    userTurtle.pos()
    print(userTurtle.pos())

def m3():
    userTurtle.setheading(360)
    userTurtle.fd(30)
    userTurtle.pos()
    print(userTurtle.pos())

def m4():
    userTurtle.setheading(-90)
    userTurtle.fd(30)
    userTurtle.pos()
    print(userTurtle.pos())

scr.onkeypress(m1, "Up")
scr.onkeypress(m2, "Left")
scr.onkeypress(m3, "Right")
scr.onkeypress(m4, "Down")
    
scr.listen()
        
drawMaze()