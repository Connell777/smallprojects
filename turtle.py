#turtle graphics

from turtle import *
color('green')
bgcolor('black')
speed(199)
hideturtle()
b = 0
while b < 500:
    right(b)
    forward(b * 3)
    b = b + 1
