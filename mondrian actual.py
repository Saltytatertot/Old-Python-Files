import random
import turtle
wn = turtle.Screen()
fred = turtle.Turtle()

w = 200
h = 200
print(w)
print(h)

w = random.randint(10,w)
h = random.randint(10,h)
for i in range(4):
    for i in range(2):
        fred.fd(w)
        fred.rt(90)
        fred.fd(h)
        fred.rt(90)
    print(w)
    print(h)
