from turtle import Turtle, Screen
import random

CIRCLE_ANGLE = 360


def square(timmy: Turtle):
    timmy.color("#DA70D6")
    timmy.left(90)

    for _ in range(8):
        timmy.forward(100)
        timmy.right(45)


def dash_line(timmy):
    for _ in range(25):
        timmy.forward(5)
        timmy.penup()
        timmy.forward(5)
        timmy.pendown()


def draw_figures(timmy: Turtle):
    colors = ["#ADFF2F", "#66CDAA", "#40E0D0", "#00BFFF", "#BDB76B", "#A52A2A", "#EE82EE"]
    timmy.penup()
    timmy.setpos(50, 75)
    timmy.pendown()

    for side in range(3, 11):
        current_angle = CIRCLE_ANGLE / side
        timmy.color(random.choice(colors))
        for _ in range(side):
            timmy.right(current_angle)
            timmy.forward(100)


def random_walk(timmy: Turtle):
    timmy.pensize(10)
    colors = ["#ADFF2F", "#66CDAA", "#40E0D0", "#00BFFF", "#BDB76B", "#A52A2A", "#EE82EE", "#9400D3", "#FFDAB9", "#000080", "#A9A9A9"]
    angles = [0, 90, 180, 270]
    while True:
        timmy.color(random.choice(colors))
        timmy.right(random.choice(angles))
        timmy.forward(30)


def main():
    timmy = Turtle()

    # square(timmy)
    # dash_line(timmy)
    # draw_figures(timmy)
    random_walk(timmy)

    screen = Screen()
    screen.exitonclick()
    screen.bgcolor("#000000")

    return 0


main()
