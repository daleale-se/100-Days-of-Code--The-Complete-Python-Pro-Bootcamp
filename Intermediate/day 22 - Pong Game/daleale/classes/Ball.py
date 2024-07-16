from turtle import Turtle
import random
import time


class Ball(Turtle):

    def __init__(self):
        self.__direction = "right"
        self.__in_game = True
        self.__speed = 5
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("circle")
        self.color("white")
        self.pensize(20)
        self.set_angle()
        self.setheading(random.randint(0, 90) - 45)

    def move(self):
        time.sleep(.01)
        if self.__in_game:
            self.forward(self.__speed)

    def finish_game(self, scoreboard):
        self.__in_game = False
        self.change_direction()
        scoreboard.show_result(self.__direction)


    def bounce(self):
        if self.ycor() > 280:
            if self.__direction == "right":
                self.setheading(-45 + random.randint(0, 45))
            else:
                self.setheading(-180 + 22.5 + random.randint(0, 45))
        elif self.ycor() < -280:
            if self.__direction == "right":
                self.setheading(22.5 + random.randint(0, 45))
            else:
                self.setheading(90 + 22.5 + random.randint(0, 45))

    def change_direction(self):
        if self.__direction == "right":
            self.__direction = "left"
        else:
            self.__direction = "right"

    def bounce_player(self):
        if self.__direction == "right":
            self.setheading(random.randint(0, 90) - 45)
        else:
            self.setheading(random.randint(0, 90) + 90 + 45)
        self.__speed += 1

    def out_of_field(self, paddle_l, paddle_r):
        if self.xcor() < -500 or 500 < self.xcor():
            if self.__direction == "right":
                paddle_l.increment_score(self)
            elif self.__direction == "left":
                paddle_r.increment_score(self)
            self.change_direction()
            self.set_angle()
            self.goto(0, 0)
            self.__speed = 5

    def set_angle(self):
        if self.__direction == "right":
            self.setheading(random.randint(0, 90) - 45)
        else:
            self.setheading(random.randint(0, 90) + 90 + 45)

