from turtle import Turtle, Screen
import random

walker = Turtle()
walker.pensize(10)
screen = Screen()
screen.bgcolor("black")

colours = ["royal blue", "gold", "lime", "orange red", "medium violet red", "dark blue", "blue violet", "saddle brown",
           "pale goldenrod", "olive", "spring green", "light salmon", "medium purple", "dark violet", "cyan", "gray"]
angle_walk = [0, 90, 180, 270]

for i in range(300):
    walker.color(random.choice(colours))
    walker.right(random.choice(angle_walk))
    walker.forward(30)

screen.exitonclick()

