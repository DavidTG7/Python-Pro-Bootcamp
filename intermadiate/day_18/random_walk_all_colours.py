from turtle import Turtle, Screen
import turtle
import random

walker = Turtle()
walker.pensize(10)
turtle.colormode(255)
screen = Screen()
screen.bgcolor("black")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)
    return new_color


angle_walk = [0, 90, 180, 270]

for i in range(300):
    walker.color(random_color())
    walker.right(random.choice(angle_walk))
    walker.forward(30)

screen.exitonclick()

