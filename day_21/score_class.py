from turtle import Turtle


class Score(Turtle):


    def __init__(self):
        super().__init__()
        self.score = -1
        with open("data.txt", mode='r') as file:
            self.high_score = int(file.read())
        self.goto(0, 265)
        self.color('white')
        self.hideturtle()

    def reset_game(self):
        with open("data.txt", mode='w') as file:
            if self.score > self.high_score:
                file.write(str(self.score))
        self.score = 0
        self.clear()
        self.write(arg=f"Current Score: {self.score}; Highest Score {self.high_score}", align='center', font=('Arial', 22, "normal"))


    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"Game Over! Your Score: {self.score}", align='center', font=('Arial', 22, "normal"))

    def score_up(self):
        with open('data.txt') as file:
            high_score = file.read()
            self.clear()
            self.score += 1
            self.write(arg=f"Current Score: {self.score}; Highest Score {high_score}", align='center', font=('Arial', 22, "normal"))
