import turtle
from turtle import left, right, forward
size = 10
def hilbert(level, angle):
    if level == 0:
        return
    turtle.color("Blue")
    turtle.speed("Fastest")
    right(angle)
    hilbert(level - 1, -angle)
    forward(size)
    left(angle)
    hilbert(level - 1, angle)
    forward(size)
    hilbert(level - 1, angle)
    left(angle)
    forward(size)
    hilbert(level - 1, -angle)
    right(angle)
hilbert(5, 90)
