from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.goto(0, 265)
        self.color('white')
        self.hideturtle()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"Game Over! Your Score: {self.score}", align='center', font=('Arial', 22, "normal"))


    def score_up(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Current score is {self.score}", align='center', font=('Arial', 22, "normal"))
