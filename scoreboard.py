from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 60, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(arg=self.r_score, align=ALIGNMENT, font=FONT)

    def l_score_is(self):
        self.l_score += 1
        self.update_score()

    def r_score_is(self):
        self.r_score += 1
        self.update_score()
