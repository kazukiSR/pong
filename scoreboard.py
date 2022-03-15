from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write(f"{self.score1}:{self.score2}", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.score1}:{self.score2}", align=ALIGNMENT, font=FONT)

    def p1_point(self):
        self.score1 += 1
        self.update_scoreboard()

    def p2_point(self):
        self.score2 += 1
        self.update_scoreboard()