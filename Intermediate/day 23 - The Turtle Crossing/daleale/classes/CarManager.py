from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.__car_speed = 1
        self.__car_quantity = 30
        self.__cars: list[Turtle] = []
        self.__spawn_cars()

    def __create_car(self):
        car = Turtle("square")
        car.penup()
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.setheading(180)
        car.color(random.choice(COLORS))
        car.goto(x=random.randint(340, 1000), y=self.__random_y_pos())
        self.__cars.append(car)

    @staticmethod
    def __random_y_pos():
        y_value = random.randint(-250, 250)
        while y_value % 25 != 0:
            y_value = random.randint(-250, 250)
        return y_value

    def __spawn_cars(self):
        for _ in range(self.__car_quantity):
            self.__create_car()

    def move(self):
        for car in self.__cars:
            car.forward(self.__car_speed)

    def refresh(self):
        for car in self.__cars:
            if car.xcor() < -320:
                car.goto(x=340, y=self.__random_y_pos())

    def increase_speed(self):
        self.__car_speed += 1

    def collision(self, player: Turtle):
        for car in self.__cars:
            if car.distance(player) < 25 and (car.ycor() - 30) < player.ycor() < (car.ycor() + 30):
                return True
        return False
