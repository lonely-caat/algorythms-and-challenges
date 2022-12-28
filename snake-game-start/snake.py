from turtle import Turtle
SPAWN_X = 150
SPAWN_Y = 150
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.sausage = []
        self.create_snake()
        self.sneke_head = self.sausage[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segemnt(position)

    def add_segemnt(self, position):
        sneke_segment = Turtle('square')
        sneke_segment.penup()
        sneke_segment.goto(position)
        self.sausage.append(sneke_segment)

    def extend(self):
        self.add_segemnt(self.sausage[-1].position())

    def reset(self):
        for segment in self.sausage:
            segment.goto(10000, 10000)
        self.sausage.clear()
        self.create_snake()
        self.sneke_head = self.sausage[0]




    def move(self):
        for segment in range(len(self.sausage) - 1, 0, -1):
            segment_coordinate_x = self.sausage[segment - 1].xcor()
            segment_coordinate_y = self.sausage[segment - 1].ycor()
            # print(segment_coordinate_x, segment_coordinate_y)
            self.sausage[segment].goto(segment_coordinate_x, segment_coordinate_y)

        self.sneke_head.forward(20)
        print(self.sausage[0].position())

    def up(self):
        if self.sneke_head.heading() != DOWN:
            self.sneke_head.setheading(UP)

    def down(self):
        if self.sneke_head.heading() != UP:
            self.sneke_head.setheading(DOWN)

    def left(self):
        if self.sneke_head.heading() != RIGHT:
            self.sneke_head.setheading(LEFT)

    def right(self):
        if self.sneke_head.heading() != LEFT:
            self.sneke_head.setheading(RIGHT)
