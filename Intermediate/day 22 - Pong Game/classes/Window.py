from turtle import Screen, Turtle


class Window:

    def __init__(self):
        Screen().setup(width=1000, height=600)
        Screen().bgcolor("black")
        Screen().title("Pong Py")
        Screen().tracer(0)

    @staticmethod
    def create_dash_line():
        dash_line = Turtle("square")
        dash_line.color("white")
        dash_line.pensize(10)
        dash_line.hideturtle()
        dash_line.penup()
        dash_line.goto(0, -300)
        dash_line.setheading(90)
        while dash_line.ycor() < 300:
            dash_line.pendown()
            dash_line.forward(15)
            dash_line.penup()
            dash_line.forward(20)

    @staticmethod
    def get_screen():
        return Screen()
