from turtle import Turtle, Screen
import random

shapes = Turtle()
shapes.color("#FF6347")
angle_shape = 3
colours = ["royal blue", "gold", "lime", "orange red", "medium violet red", "dark blue", "blue violet", "saddle brown"]

for i in range(8):
    shapes.color(random.choice(colours))
    for a in range(angle_shape):
        shapes.forward(150)
        shapes.right(360 / angle_shape)
    angle_shape += 1

screen = Screen()
screen.exitonclick()
