from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.get_highscore_from_file()
        self.penup()
        self.speed('fastest')
        self.pensize(10)

        self.setposition(-20,280)
        self.update_score()
        self.hideturtle()

    @staticmethod
    def get_highscore_from_file():
        with open('data.txt', 'r') as data_file:
            data = int(data_file.read())
        return data

    @staticmethod
    def write_highscore_to_file(data):
        with open('data.txt', 'w') as data_file:
            data_file.write(str(data))

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.highscore}", font=('Arial', 14, 'normal'))

    def add_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score >= self.highscore:
            self.highscore = self.score
            self.write_highscore_to_file(self.highscore)
        self.score = 0
        self.update_score()

    def game_over(self):
        self.setposition(-30, 0)
        self.write(f"Game Over! \nYour score: {self.score}", font=('Arial', 16, 'normal'))



