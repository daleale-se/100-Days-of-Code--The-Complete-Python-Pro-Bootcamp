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
        self.__head = None
        self.__create_snake()

    def __create_snake(self):
        x_pos = 0
        for i in range(3):
            self.__add_segment((x_pos, 0))
            x_pos -= MOVE_FORWARD
        self.__head = self.__segments[0]

    def __add_segment(self, pos):
        t = Turtle("square")
        t.penup()
        t.speed("slow")
        t.resizemode("user")
        t.color("white")
        t.goto(pos)
        self.__segments.append(t)
    
    def move(self):
        x_pos, y_pos = self.__head.pos()
        self.__head.forward(20)
        for segment in self.__segments[1:]:
            x_aux = segment.xcor()
            y_aux = segment.ycor()
            segment.goto(x=x_pos, y=y_pos)
            x_pos = x_aux
            y_pos = y_aux

    def turn_up(self):
        if self.__head.heading() != DOWN and self.__head.heading() != UP:
            self.__head.setheading(UP)

    def turn_left(self):
        if self.__head.heading() != RIGHT and self.__head.heading() != LEFT:
            self.__head.setheading(LEFT)

    def turn_down(self):
        if self.__head.heading() != UP and self.__head.heading() != DOWN:
            self.__head.setheading(DOWN)

    def turn_right(self):
        if self.__head.heading() != LEFT and self.__head.heading() != RIGHT:
            self.__head.setheading(RIGHT)

    def eat(self, food: Food):
        return food.was_eaten(self.__head)

    def collision_wall(self):
        return ((280 < self.__head.xcor()) or (self.__head.xcor() < -280) or (280 < self.__head.ycor()) or
                (self.__head.ycor() < -280))

    def collision_himself(self):
        for segment in self.__segments[1:]:
            if self.__head.distance(segment) < 10:
                return True
        return False

    def grow(self):
        self.__add_segment(self.__segments[-1].position())

    def reset(self):
        for segment in self.__segments:
            segment.goto(1000, 1000)
        self.__segments.clear()
        self.__create_snake()
