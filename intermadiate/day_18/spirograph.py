from turtle import Turtle, Screen
import random
import turtle

circle = Turtle()
circle.pensize(1)
turtle.colormode(255)
screen = Screen()
screen.bgcolor("black")
circle.speed(11)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)
    return new_color


angle = 4

for i in range(90):
    circle.color(random_color())
    circle.circle(200)
    circle.right(angle)


screen.exitonclick()

