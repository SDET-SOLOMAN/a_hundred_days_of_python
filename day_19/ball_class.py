from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.shapesize(stretch_wid=1.2, stretch_len=1.2)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.moving_speed = .1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.moving_speed *= .9

    def reset(self):
        if self.xcor() > 0:
            self.goto(0, 0)
            self.move()
        else:
            self.goto(0, 0)
            self.bounce()
