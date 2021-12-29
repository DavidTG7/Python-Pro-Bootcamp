from turtle import *
color('red', 'yellow')
begin_fill()

bgcolor("black")
while True:
    forward(200)
    left(220)
    if abs(pos()) < 1:
        break
# end_fill()
done()