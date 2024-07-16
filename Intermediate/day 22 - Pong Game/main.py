from classes.Paddle import Paddle
from classes.Ball import Ball
from classes.Window import Window


def main():
    window = Window()
    window.create_dash_line()
    screen = window.get_screen()

    screen.listen()

    paddle_a = Paddle((450, 0))
    screen.onkey(key="Up", fun=paddle_a.move_up)
    screen.onkey(key="Down", fun=paddle_a.move_down)

    paddle_b = Paddle((-450, 0))
    screen.onkey(key="w", fun=paddle_b.move_up)
    screen.onkey(key="s", fun=paddle_b.move_down)

    ball = Ball()
    while True:
        screen.update()
        ball.move()
        ball.bounce()
        paddle_a.collision(ball)
        paddle_b.collision(ball)

    screen.exitonclick()


main()
