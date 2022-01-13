from turtle import Turtle, Screen
import random
import turtle

dots = Turtle()
turtle.colormode(255)
screen = Screen()
screen.title("Dots Painting")

colours = [(220, 225, 210), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46),
           (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121),
           (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232),
           (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]

y_position = -200
x_position = -200
dots.penup()
dots.hideturtle()

for a in range(10):
    dots.setposition(y_position, x_position)
    x_position += 50
    for i in range(10):
        dots.dot(20, random.choice(colours))
        dots.forward(50)

screen.exitonclick()

