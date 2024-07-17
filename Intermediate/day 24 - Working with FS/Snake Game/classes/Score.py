from turtle import Turtle


ALIGNMENT = "center"
FONT = ('Sans', 20, 'normal')


class Score(Turtle):

    def __init__(self):
        self.__score = 0
        self.__highscore = 0
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.__update_score()
        self.hideturtle()
        self.__read_highscore()

    def __update_score(self):
        self.clear()
        self.write(f"Score: {self.__score}  HighScore: {self.__highscore}", False, ALIGNMENT, FONT)

    def reset_score(self):
        if self.__score > self.__highscore:
            self.__highscore = self.__score
            self.__save_highscore()
        self.__score = 0
        self.__update_score()

    def increase(self):
        self.__score += 1
        self.__update_score()

    def __read_highscore(self):
        with open("data.txt", mode="r") as file:
            self.__highscore = int(file.read())
        self.__update_score()

    def __save_highscore(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.__highscore))
