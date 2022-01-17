from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE")

x_position = [0, -10, -20]
for _ in range(0, 3):
    snake = Turtle(shape="square")
    snake.shapesize(0.5)
    snake.penup()
    snake.color("white")
    snake.goto(x=x_position[_], y=0)




screen.exitonclick()