import turtle

def square(aTurtle, upperX, upperY, width):
    aTurtle.up()
    aTurtle.goto(upperX, upperY)
    aTurtle.down()
    for side in range(4):
         aTurtle.forward(width)
         aTurtle.right(90)
    aTurtle.up()
    aTurtle.goto(-upperX, upperY)
    aTurtle.down()
    for side in range(4):
        aTurtle.fd(-width)
        aTurtle.right(-90)

def recursive_squares(aTurtle, upperX, upperY, width, level):
    if (level > 0):
         square(aTurtle, upperX, upperY, width)
         recursive_squares(aTurtle, upperX, upperY, width / 3, level - 1)
         
squares = turtle.Turtle()
squares.color("blue")
recursive_squares(squares, -200, 200, 400, 3)
squares.hideturtle()
wn = turtle.Screen()
wn.exitonclick()
