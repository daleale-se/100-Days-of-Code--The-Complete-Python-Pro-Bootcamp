import random
import turtle
# from colorgram import extract, Color
from turtle import Turtle, Screen


# def create_color(color: Color):
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     return r, g, b


# def extract_color():
#     colors = extract('image.jpg', 10)
#     selected_colors = []
#     for color in colors:
#         selected_colors.append(create_color(color))
#     print(selected_colors)

def main():
    turtle.colormode(255)
    turtle.bgcolor("black")

    pencil = Turtle()
    pencil.shape("circle")
    pencil.penup()
    pencil.speed(0)
    pencil.hideturtle()

    # extract_color()
    colors = [(55, 254, 156), (65, 1, 214), (252, 246, 72), (254, 146, 228), (194, 254, 250), (2, 213, 55),
              (252, 143, 37), (110, 181, 254), (253, 34, 254)]

    for i in range(10):
        pencil.sety(-225 + 50 * i)
        pencil.setx(-225)
        for _ in range(10):
            pencil.dot(20, random.choice(colors))
            pencil.forward(50)

    screen = Screen()
    screen.exitonclick()


main()
