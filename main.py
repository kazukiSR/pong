from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()
paddle1 = Paddle((-350, 0))
paddle2 = Paddle((350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(paddle2.goUp, "Up")
screen.onkeypress(paddle2.goDown, "Down")
screen.onkeypress(paddle1.goUp, "w")
screen.onkeypress(paddle1.goDown, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceWall()

    # Paddle collision
    if ball.distance(paddle2.pos()) < 50 and ball.xcor() > 320 or ball.distance(paddle1.pos()) < 50 and ball.xcor() < -320:
        ball.bouncePaddle()

    # P1 Miss
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.p2_point()

    # P2 miss
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.p1_point()


screen.exitonclick()
