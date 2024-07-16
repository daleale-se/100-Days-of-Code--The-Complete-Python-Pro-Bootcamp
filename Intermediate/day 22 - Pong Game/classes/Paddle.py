from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.pensize(20)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(pos)

    def move_up(self):
        self.sety(self.ycor() + 20)

    def move_down(self):
        self.sety(self.ycor() - 20)

    def collision(self, ball):
        if self.distance(ball) < 50 and (ball.xcor() < -430 or ball.xcor() > 430):
            ball.change_direction()
            ball.bounce_player()
            if ball.xcor() < -430:
                ball.setx(-430)
            else:
                ball.setx(430)
        