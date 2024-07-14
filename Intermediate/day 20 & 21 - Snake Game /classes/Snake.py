from turtle import Turtle

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
        if self.__head.heading() != DOWN:
            self.__head.setheading(UP)

    def turn_left(self):
        if self.__head.heading() != RIGHT:
            self.__head.setheading(LEFT)

    def turn_down(self):
        if self.__head.heading() != UP:
            self.__head.setheading(DOWN)

    def turn_right(self):
        if self.__head.heading() != LEFT:
            self.__head.setheading(RIGHT)
