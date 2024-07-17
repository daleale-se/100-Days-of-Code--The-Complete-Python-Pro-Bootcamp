from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        self.__level = 1
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(x=-200, y=250)
        self.__show_level()

    def __show_level(self):
        self.write(arg=f"level: {self.__level}", move=False, align="center", font=FONT)

    def increase_level(self):
        self.__level += 1

    def update_level(self):
        self.clear()
        self.__show_level()

    def restart_level(self):
        self.__level = 1
        self.update_level()
