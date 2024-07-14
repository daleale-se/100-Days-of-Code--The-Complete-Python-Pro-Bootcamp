from turtle import Turtle, Screen


def turtle_events(titi, screen):

    def move_forward():
        titi.forward(10)

    def turn_east():
        titi.setheading(0)

    def turn_north():
        titi.setheading(90)

    def turn_west():
        titi.setheading(180)

    def turn_south():
        titi.setheading(270)

    screen.listen()

    screen.onkey(key="space", fun=move_forward)
    screen.onkey(key="Right", fun=turn_east)
    screen.onkey(key="Up", fun=turn_north)
    screen.onkey(key="Left", fun=turn_west)
    screen.onkey(key="Down", fun=turn_south)


def etch_a_sketch(titi, screen):

    titi.speed(9)

    def move_forward():
        titi.forward(10)

    def move_backward():
        titi.backward(10)

    def turn_left():
        titi.setheading(titi.heading() + 10)

    def turn_right():
        titi.right(10)

    def clear():
        titi.setpos(0,0)
        titi.clear()

    screen.listen()

    screen.onkey(key="w", fun=move_forward)
    screen.onkey(key="s", fun=move_backward)
    screen.onkey(key="d", fun=turn_right)
    screen.onkey(key="a", fun=turn_left)
    screen.onkey(key="c", fun=clear)


def main():

    titi = Turtle()
    screen = Screen()

    # turtle_events(titi, screen)

    etch_a_sketch(titi, screen)

    screen.exitonclick()


main()
