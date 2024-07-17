from turtle import Screen
from classes.Player import Player
from classes.CarManager import CarManager
from classes.Scoreboard import Scoreboard


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    player = Player()
    scoreboard = Scoreboard()
    car_manager = CarManager()

    screen.listen()
    screen.onkeypress(key="Up", fun=player.go_up)
    screen.onkeyrelease(key="Up", fun=player.stop)
    screen.onkeypress(key="Down", fun=player.go_down)
    screen.onkeyrelease(key="Down", fun=player.stop)

    game_is_on = True
    while game_is_on:
        player.update_frame()
        car_manager.move()
        car_manager.refresh()
        if player.ycor() > 270:
            player.go_start_position()
            car_manager.increase_speed()
            scoreboard.increase_level()
            scoreboard.update_level()
        if car_manager.collision(player):
            car_manager.restart_speed()
            game_is_on = False
        if player.ycor() < -280:
            player.stop_going_down()
        screen.update()

    scoreboard.game_over()
    screen.exitonclick()


main()
