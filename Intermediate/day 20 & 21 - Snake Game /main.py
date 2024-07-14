from turtle import Screen
from classes.Snake import Snake
import time

# def snake_movement(snake: list[Turtle]):
#     x_pos = snake[0].xcor()
#     y_pos = snake[0].ycor()
#     for i in range(1, len(snake)):
#         x_aux = snake[i].xcor()
#         y_aux = snake[i].ycor()
#         snake[i].goto(x=x_pos, y=y_pos)
#         x_pos = x_aux
#         y_pos = y_aux


def main():

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Py")
    screen.tracer(0)
    screen.delay(0)

    snake = Snake()

    screen.listen()
    screen.onkey(key="Up", fun=snake.turn_up)
    screen.onkey(key="Left", fun=snake.turn_left)
    screen.onkey(key="Down", fun=snake.turn_down)
    screen.onkey(key="Right", fun=snake.turn_right)

    in_game = True
    while in_game:

        screen.update()
        time.sleep(.1)
        snake.move()

    screen.exitonclick()


main()
