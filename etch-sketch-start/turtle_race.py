from turtle import Turtle, Screen
from random import randint
colors = ['red', 'pink', 'yellow', 'beige', 'orange', 'magenta']
starting_position_y = -100
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='enter your bet', prompt=f'which turtle will win')
flock_of_turtles = []

for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    starting_position_y += 30
    new_turtle.goto(x=-200, y=starting_position_y)
    flock_of_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for t in flock_of_turtles:
        t.forward(randint(0, 10))
        # print(t.position()[1])
        # print(t.position()[0])
        if t.position()[0] > 230:
            if t.color()[0] == user_bet:
                print('you won')
            else:
                print(f'you lost:( {t.color()[1]} won')
            is_race_on = False

screen.exitonclick()
