from turtle import Screen
from classes.Snake import Snake
from classes.Food import Food
from classes.Score import Score
import time


def main():

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Py")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Score()

    screen.listen()
    screen.onkeypress(key="Up", fun=snake.turn_up)
    screen.onkeypress(key="Left", fun=snake.turn_left)
    screen.onkeypress(key="Down", fun=snake.turn_down)
    screen.onkeypress(key="Right", fun=snake.turn_right)

    in_game = True
    while in_game:
        time.sleep(.1)
        screen.update()
        snake.move()
        if snake.eat(food):
            snake.grow()
            scoreboard.increase()
            food.refresh()
        if snake.collision_wall() or snake.collision_himself():
            scoreboard.reset_score()
            snake.reset()

    screen.exitonclick()


main()
