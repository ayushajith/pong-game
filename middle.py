from turtle import Turtle


class Middle(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.left(90)
        self.color("white")
        self.penup()
        self.goto(x=0, y=420)
        self.right(180)
        for _ in range(25):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(15)
