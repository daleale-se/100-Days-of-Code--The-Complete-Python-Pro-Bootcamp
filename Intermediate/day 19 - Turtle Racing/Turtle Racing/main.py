import random
from turtle import Turtle, Screen


def main():

    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ("
                                                              "red/orange/yellow/green/blue/purple)")
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    turtles = []

    y_pos = -100
    for color in colors:
        turtle = Turtle(shape="turtle")
        turtle.penup()
        turtle.color(color)
        turtle.goto(x=-220, y=y_pos)
        y_pos += 40
        turtles.append(turtle)

    turtle_reach_finish = False

    if user_bet in colors:
        while not turtle_reach_finish:
            for turtle in turtles:
                turtle.forward(random.randint(0, 10))
                if turtle.xcor() > 230:
                    turtle_reach_finish = True
                    winner_color: str = turtle.pencolor()
                    if winner_color == user_bet:
                        print(f"YOU WIN. {winner_color.upper()} turtle is the winner.")
                    else:
                        print(f"YOU LOSE. {winner_color.upper()} turtle is the winner.")

    screen.exitonclick()


main()
