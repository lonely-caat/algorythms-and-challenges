from turtle import Turtle, Screen
turtle = Turtle()
screen = Screen()


def move_forward(distance=20):
    turtle.forward(distance)


def turn_left(angle=10):
    turtle.left(angle)


def turn_right(angle=10):
    turtle.right(angle)


def turn_back(distance=20):
    turtle.back(distance)


screen.listen()
screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=turn_left, key='a')
screen.onkey(fun=turn_right, key='d')
screen.onkey(fun=turn_back, key='s')
screen.onkey(fun=screen.bye, key='c')

screen.exitonclick()
