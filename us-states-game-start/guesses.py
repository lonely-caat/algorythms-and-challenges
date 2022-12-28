from turtle import Turtle


class Guess(Turtle):
    def __init__(self, x,y):
        super().__init__()

        self.penup()
        self.speed('fastest')
        self.pensize(100)
        self.setposition(x, y)
        self.hideturtle()

    def fill_in_state(self, state):
        self.write(f"{state}", font=('Arial', 16, 'normal'))







