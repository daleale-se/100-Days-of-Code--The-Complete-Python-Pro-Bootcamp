from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 2
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        self.__speed = 0
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        self.__speed = MOVE_DISTANCE

    def stop(self):
        self.__speed = 0

    def update_frame(self):
        self.goto(x=self.xcor(), y=(self.ycor() + self.__speed))

    def go_start_position(self):
        self.goto(STARTING_POSITION)
