from turtle import Turtle


ALIGNMENT = "center"
FONT = ('Sans', 80, 'normal')
FONT_WINNER = ('Sans', 50, 'bold')


class ScoreBoard(Turtle):

    def __init__(self, pos):
        self.__score = 0
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(pos)
        self.__update_score()
        self.hideturtle()

    def __update_score(self):
        self.write(f"{self.__score}", False, ALIGNMENT, FONT)

    def increment(self):
        self.__score += 1
        self.clear()
        self.__update_score()

    @staticmethod
    def show_result(direction: str):
        t = Turtle()
        t.penup()
        t.color("green")
        t.hideturtle()
        t.goto(x=0, y=0)
        t.write(f"{direction.upper()} PADDLE WIN", False, ALIGNMENT, FONT_WINNER)

    def is_ten(self):
        return self.__score == 10
