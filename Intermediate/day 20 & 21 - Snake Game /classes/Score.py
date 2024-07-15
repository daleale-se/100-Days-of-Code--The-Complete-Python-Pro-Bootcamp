from turtle import Turtle


ALIGNMENT = "center"
FONT = ('Sans', 20, 'normal')


class Score(Turtle):

    def __init__(self):
        self.__score = 0
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.__update_score()
        self.hideturtle()

    def __update_score(self):
        self.write(f"score = {self.__score}", False, ALIGNMENT, FONT)

    def increase(self):
        self.__score += 1
        self.clear()
        self.__update_score()

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", False, ALIGNMENT, FONT)
