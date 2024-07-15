import time
from turtle import Turtle
from .Food import Food


MOVE_FORWARD = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self):
        self.__segments: list[Turtle] = []
        self.__create_snake()
        self.__head = self.__segments[0]

    def __create_snake(self):
        x_pos = 0
        for _ in range(3):
            t = Turtle("square")
            t.penup()
            t.speed(0)
            t.pensize(20)
            t.color("white")
            t.goto(x=x_pos, y=0)
            self.__segments.append(t)
            x_pos -= MOVE_FORWARD

    def move(self):
        for i in range(len(self.__segments) - 1, 0, -1):
            x_pos = self.__segments[i - 1].xcor()
            y_pos = self.__segments[i - 1].ycor()
            self.__segments[i].goto(x=x_pos, y=y_pos)
        self.__head.forward(MOVE_FORWARD)

    def turn_up(self):
        if self.__head.heading() != DOWN and self.__head.heading() != UP:
            self.__head.setheading(UP)
            print("up")

    def turn_left(self):
        if self.__head.heading() != RIGHT and self.__head.heading() != LEFT:
            self.__head.setheading(LEFT)
            print("left")

    def turn_down(self):
        if self.__head.heading() != UP and self.__head.heading() != DOWN:
            self.__head.setheading(DOWN)
            print("down")

    def turn_right(self):
        if self.__head.heading() != LEFT and self.__head.heading() != RIGHT:
            self.__head.setheading(RIGHT)
            print("right")

    def eat(self, food: Food):
        return food.was_eaten(self.__head)

    def collides_wall(self):
        return (self.__head.xcor() > 280) or (-280 > self.__head.ycor() > 280)

