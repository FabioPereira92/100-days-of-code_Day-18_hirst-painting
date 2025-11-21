import turtle
from turtle import Turtle, Screen
import random

colors = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (227, 159, 49), (29, 40, 154), (212, 76, 15), (241, 36, 161), (223, 21, 120), (68, 10, 31), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (79, 74, 212)]

screen = Screen()
turtle.colormode(255)
tim = Turtle()
tim.penup()
tim.hideturtle()
tim.setposition(-250, -250)

for i in range(10):
    for _ in range(10):
        tim.dot(20,random.choice(colors) )
        tim.forward(50)
    tim.setposition(-250, -250 + 50 * (i + 1))

screen.exitonclick()