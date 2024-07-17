import time
from turtle import Screen
from classes.Player import Player
from classes.CarManager import CarManager


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    player = Player()
    car_manager = CarManager()

    screen.listen()
    screen.onkeypress(key="Up", fun=player.go_up)
    screen.onkeyrelease(key="Up", fun=player.stop)

    game_is_on = True
    while game_is_on:
        time.sleep(0.01)
        player.update_frame()
        car_manager.move()
        car_manager.refresh()
        if player.ycor() > 270:
            player.go_start_position()
            car_manager.increase_speed()
        if car_manager.collision(player):
            player.go_start_position()

        screen.update()


main()
