from turtle import Turtle
from random import random


def main():
    t = Turtle("square")
    t.screen.tracer(0)

    def go_up():
        t.setheading(90)

    def go_left():
        t.setheading(180)

    def go_down():
        t.setheading(270)

    def go_right():
        t.setheading(0)

    def update_frame():
        t.forward(10)
        t.screen.update()

        t.screen.ontimer(update_frame, 50)

    t.screen.listen()
    t.screen.onkey(key="y", fun=go_up)
    t.screen.onkey(key="g", fun=go_left)
    t.screen.onkey(key="h", fun=go_down)
    t.screen.onkey(key="j", fun=go_right)

    t.screen.ontimer(update_frame, 50)

    t.screen.mainloop()


main()
