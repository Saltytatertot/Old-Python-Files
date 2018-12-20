#Excersise 10, Turtle clock
#Tatum Gray
#2/18/2016


import turtle
wn = turtle.Screen()
fred = turtle.Turtle()

for i in range(12):
	fred.penup()
	fred.forward(50)
	fred.pendown()
	fred.forward(10)
	fred.penup()
	fred.forward(10)
	fred.shape('turtle')
	fred.stamp()
	fred.penup()
	fred.forward(-70)
	fred.right(30)
wn.exitonclick()
