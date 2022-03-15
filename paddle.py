from turtle import Turtle

PADDLE_WIDTH = 5
PADDLE_LENGTH = 1
UP = 90
DOWN = 270
MOVE_DISTANCE = 20

class Paddle:

    def __init__(self, position):
        self.paddle = Turtle(shape="square")
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LENGTH)
        self.paddle.goto(position)

    def goUp(self):
        new_y = self.paddle.ycor() + MOVE_DISTANCE
        self.paddle.goto(self.paddle.xcor(), new_y)

    def goDown(self):
        new_y = self.paddle.ycor() - MOVE_DISTANCE
        self.paddle.goto(self.paddle.xcor(), new_y)

    def pos(self):
        return self.paddle.pos()


