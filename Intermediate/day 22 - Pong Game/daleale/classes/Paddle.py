from turtle import Turtle
from .ScoreBoard import ScoreBoard


class Paddle(Turtle):

    def __init__(self, paddle_pos, score_pos):
        self.__y_speed = 0
        self.__scoreboard = ScoreBoard(score_pos)
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.pensize(20)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(paddle_pos)

    def move_up(self):
        if self.ycor() < 230:
            self.__y_speed = 8
        else:
            self.__y_speed = 0

    def move_down(self):
        if self.ycor() > -230:
            self.__y_speed = -8
        else:
            self.__y_speed = 0

    def stop_move_up(self):
        self.__y_speed = 0

    def stop_move_down(self):
        self.__y_speed = 0

    def collision(self, ball):
        if self.distance(ball) < 50 and (ball.xcor() < -430 or ball.xcor() > 430):
            ball.change_direction()
            ball.bounce_player()
            if ball.xcor() < -430:
                ball.setx(-430)
            else:
                ball.setx(430)

    def update_position(self):
        if -230 <= self.ycor() <= 230:
            self.goto(x=self.xcor(), y=(self.ycor() + self.__y_speed))
        else:
            if self.ycor() < -230:
                self.goto(x=self.xcor(), y=-230)
            elif self.ycor() > 230:
                self.goto(x=self.xcor(), y=230)

    def increment_score(self, ball):
        self.__scoreboard.increment()
        if self.__scoreboard.is_ten():
            ball.finish_game(self.__scoreboard)