from turtle import Turtle, Screen
import random
import time


class Ball(Turtle):

    def __init__(self):
        self.__direction = "right"
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("circle")
        self.color("white")
        self.pensize(20)
        self.setheading(random.randint(0, 90) - 45)

    def move(self):
        time.sleep(.01)
        self.forward(4)

    def bounce(self):
        if self.ycor() > 280:
            if self.__direction == "right":
                self.setheading(270 + 22.5 + random.randint(0, 45))
            else:
                self.setheading(180 + 22.5 + random.randint(0, 45))
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
