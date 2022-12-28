import turtle
import pandas as pd
from guesses import Guess
from score import Score

score = Score()

IMAGE_PATH = 'blank_states_img.gif'

data = pd.read_csv('50_states.csv')
states_list = data['state']

screen = turtle.Screen()
screen.title = 'guess the state!'
screen.addshape(IMAGE_PATH)

turtle = turtle.Turtle()
turtle.shape(IMAGE_PATH)

RUNNING = True


def guess_a_state():
    answer_state = screen.textinput(title='guess the state', prompt='give me a name')
    answer_state = answer_state.title()

    if answer_state in data['state'].values:

        guesses = Guess(int(data['x'][data['state']==answer_state]), int(data['y'][data['state']==answer_state]))
        score.add_state(answer_state)
        guesses.fill_in_state(answer_state)

    if answer_state == 'Exit':
        global RUNNING

        RUNNING = False


while RUNNING:
    score.display_score()

    screen.update()
    # import time;time.sleep(0.1)
    guess_a_state()

