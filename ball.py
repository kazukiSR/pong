from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.ballWall = 10
        self.ballPaddle = 10
        self.move_speed = 0.1


    def move(self):
        new_x = self.xcor() + self.ballPaddle
        new_y = self.ycor() + self.ballWall
        self.goto(new_x, new_y)

    def bounceWall(self):
        self.ballWall *= -1
        self.move_speed *= 0.9

    def bouncePaddle(self):
        self.ballPaddle *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.bouncePaddle()
        self.bounceWall()
        self.goto(0, 0)
        self.move_speed = 0.1
