from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, *args):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=6, stretch_len=1.5)
        self.penup()
        self.goto(*args)

    def up(self):
        a = self.ycor() + 20
        self.goto(self.xcor(), a)

    def down(self):
        a = self.ycor() - 20
        self.goto(self.xcor(), a)

