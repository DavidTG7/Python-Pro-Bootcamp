from turtle import Turtle, Screen

dashed_line = Turtle()
dashed_line.pensize(5)
dashed_line.color("#FF6347")

for _ in range(20):
    dashed_line.pendown()
    dashed_line.forward(10)
    dashed_line.penup()
    dashed_line.forward(10)

screen = Screen()
screen.exitonclick()
