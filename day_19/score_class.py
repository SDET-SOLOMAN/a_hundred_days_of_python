from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.goto(0, 265)
        self.color('white')
        self.hideturtle()

    def left_score_up(self):
        self.clear()
        self.l_score += 1
        self.display_score()

    def right_score_up(self):
        self.clear()
        self.r_score += 1
        self.display_score()

    def display_score(self):
        self.penup()
        self.goto(0, 230)
        self.write(f"{self.l_score} : {self.r_score}", align='center', font=('Courier', 55, 'normal'))
