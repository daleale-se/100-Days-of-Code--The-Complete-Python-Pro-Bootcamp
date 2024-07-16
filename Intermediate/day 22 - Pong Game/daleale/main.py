from classes.Paddle import Paddle
from classes.Ball import Ball
from classes.Window import Window


def main():
    window = Window()
    window.create_dash_line()
    screen = window.get_screen()

    screen.listen()

    paddle_r = Paddle((450, 0), (80, 170))
    screen.onkeypress(key="Up", fun=paddle_r.move_up)
    screen.onkeypress(key="Down", fun=paddle_r.move_down)
    screen.onkeyrelease(key="Up", fun=paddle_r.stop_move_up)
    screen.onkeyrelease(key="Down", fun=paddle_r.stop_move_down)

    paddle_l = Paddle((-450, 0), (-80, 170))
    screen.onkeypress(key="w", fun=paddle_l.move_up)
    screen.onkeypress(key="s", fun=paddle_l.move_down)
    screen.onkeyrelease(key="w", fun=paddle_l.stop_move_up)
    screen.onkeyrelease(key="s", fun=paddle_l.stop_move_down)

    ball = Ball()
    while True:
        screen.update()
        paddle_l.update_position()
        paddle_r.update_position()
        ball.move()
        ball.bounce()
        ball.out_of_field(paddle_l, paddle_r)
        paddle_l.collision(ball)
        paddle_r.collision(ball)


    screen.exitonclick()


main()
