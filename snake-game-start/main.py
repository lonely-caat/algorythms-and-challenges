from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

snek = Snake()
food = Food()
score = Score()

screen = Screen()
screen.setup(width=600, height=600)
screen.title('snek goes meeeeeeeeeow')
screen.bgcolor('grey')
screen.tracer(0)
screen.listen()
screen.onkey(fun=snek.up, key='w')
screen.onkey(fun=snek.left, key='a')
screen.onkey(fun=snek.right, key='d')
screen.onkey(fun=snek.down, key='s')


snake_is_alive = True
while snake_is_alive:
    screen.update()
    time.sleep(0.1)
    snek.move()

    # omnom
    if snek.sneke_head.distance(food) < 15:
        food.refresh()
        score.add_score()
        snek.extend()

    # wall collisions
    if snek.sneke_head.xcor() > 280 or snek.sneke_head.xcor() < -280 or snek.sneke_head.ycor() > 280 or snek.sneke_head.ycor() < -280:
        # snake_is_alive = False
        score.reset()
        snek.reset()

    # self collisions
    for segment in snek.sausage[1:]:
        if snek.sneke_head.distance(segment) < 10:
            # snake_is_alive = False
            score.reset()
            snek.reset()


    # screen.onkey(fun=snek.screen.bye, key='c')




screen.exitonclick()
