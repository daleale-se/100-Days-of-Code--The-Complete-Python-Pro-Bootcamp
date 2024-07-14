import turtle
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
    colors = ["#ADFF2F", "#40E0D0", "#BDB76B", "#A52A2A", "#EE82EE"]
    timmy.penup()
    timmy.setpos(50, 75)
    timmy.pendown()

    for side in range(3, 11):
        current_angle = CIRCLE_ANGLE / side
        timmy.color(random.choice(colors))
        for _ in range(side):
            timmy.right(current_angle)
            timmy.forward(100)


# def random_color():
#    hexadecimal = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
#    color = "#"
#    for _ in range(6):
#        color += random.choice(hexadecimal)
#    return color


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def random_walk(timmy: Turtle):
    timmy.pensize(3)
    timmy.speed(0)
    angles = [0, 90, 180, 270]
    while True:
        timmy.color(random_color())
        timmy.right(random.choice(angles))
        timmy.forward(15)


def spirograph(timmy):
    timmy.speed(0)

    for _ in range(int(CIRCLE_ANGLE / 6)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.left(6)


def main():
    timmy = Turtle()
    turtle.colormode(255)

    # square(timmy)
    # dash_line(timmy)
    # draw_figures(timmy)
    # random_walk(timmy)

    spirograph(timmy)

    screen = Screen()
    screen.exitonclick()

    return 0


main()
