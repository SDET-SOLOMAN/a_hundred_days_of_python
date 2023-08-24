from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('black')
        self.hideturtle()

    def score_up(self):
        self.clear()
        self.score += 1

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write(f"Game Over, Your Final Score is: {self.score}", align='center', font=('Courier', 22, 'normal'))
    def display_score(self):
        self.penup()
        self.goto(-240, 280)
        self.write(f"The Score is: {self.score}", align='center', font=('Courier', 22, 'normal'))
