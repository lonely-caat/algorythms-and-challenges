from turtle import Turtle, Screen
from random import randint, choice

turtle = Turtle()
turtle.shape('turtle')
colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'white']
direction = ['left', 'right']


def draw_form(sides):
    angle = 360/sides
    color = colors[randint(0, len(colors))]
    for _ in range(sides):
        turtle.pencolor(color)
        turtle.forward(300)
        turtle.right(angle)


for element in range(4, 10):
    draw_form(element)


def draw_random_form():
    turtle.width(10)
    turtle.speed(3)
    dir = choice(direction)


