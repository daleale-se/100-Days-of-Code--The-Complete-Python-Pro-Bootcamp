from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.speed("fastest")
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.refresh()

    def was_eaten(self, head: Turtle):
        return head.distance(x=self.xcor(), y=self.ycor()) < 15

    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))