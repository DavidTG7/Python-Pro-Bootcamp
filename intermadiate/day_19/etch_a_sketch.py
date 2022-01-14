from turtle import Turtle, Screen

my_line = Turtle()
screen = Screen()


def forward():
    my_line.forward(10)


def backward():
    my_line.backward(10)


def counter_clockwise():
    new_heading = my_line.heading() + 10
    my_line.setheading(new_heading)


def clockwise():
    new_heading = my_line.heading() - 10
    my_line.setheading(new_heading)


def clear_screen():
    my_line.clear()
    my_line.penup()
    my_line.home()
    my_line.pendown()

  
screen.listen()
screen.onkey(key="a", fun=backward)
screen.onkey(key="d", fun=forward)
screen.onkey(key="w", fun=counter_clockwise)
screen.onkey(key="s", fun=clockwise)
screen.onkey(key="space", fun=clear_screen)

screen.exitonclick()
