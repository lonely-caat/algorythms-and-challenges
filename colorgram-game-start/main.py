import colorgram
from turtle import Turtle, Screen
from random import choice


colorz = colorgram.extract('Monet-Bridge_cat-det-400x300.jpeg', 10)
colors = ['red', 'pink', 'yellow', 'beige', 'orange']

def return_color_tuples(colors_list):
    colors_tuples = []
    for element in colors_list:
        colors_tuples.append((element.rgb.r, element.rgb.g, element.rgb.b))
    return colors_tuples

turtle = Turtle()
turtle.shape('circle')
turtle.width(10)
turtle.penup()

for _ in range(5):
    for _ in range(5):
        color = choice(colors)
        turtle.color(color)
        turtle.dot()
        turtle.forward(50)
        # turtle.pendown()
    current_position = turtle.pos()
    turtle.goto(0, current_position[1]+50)







