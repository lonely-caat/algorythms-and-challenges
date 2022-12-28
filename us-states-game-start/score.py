from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.setposition(0, 0)
        self.guessed_states_list = []
        self.penup()
        self.speed('fastest')
        self.pensize(100)
        self.hideturtle()
        self.display_score()


    def display_score(self):
        self.clear()
        self.write(f"your score is {len(self.guessed_states_list)}/50", font=('Arial', 16, 'normal'))

    def add_state(self, state):
        if state not in self.guessed_states_list:
            self.guessed_states_list.append(state)








