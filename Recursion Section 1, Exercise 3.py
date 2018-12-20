#Recursion Section 1, Exercise 3
#Tatum Gray
#5/1/2016

import turtle
import random

def tree(branchLen,t,width):
    if branchLen <= 15:
        t.color('green')    #Changes branch color to green if the length is short enough
    if branchLen > 5:
        t.pensize(width)
        t.forward(branchLen)
        t.right(20)
        t.pensize(width)
        tree(branchLen-15,t,width-2)    #Changes the width of the branch
        t.left(40)
        t.pensize(width)
        tree(branchLen-15,t,width-2)    #Changes the width of the branch
        t.right(20)
        t.pensize(width)
        t.backward(branchLen)
        t.color('brown')

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.speed(100)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('brown')
    tree(75,t,10)
    myWin.exitonclick()

main()


