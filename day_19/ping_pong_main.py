from day_19.paddle_class import Paddle
from day_19.ball_class import Ball
from day_19.score_class import Score
from turtle import Screen
from time import sleep

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("SDET SOLOMAN PING PONG GAME")

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

while True:
    sleep(ball.moving_speed)
    score.display_score()
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()

    if ball.distance(r_paddle) < 62 and ball.xcor() > 320 or ball.distance(l_paddle) < 62 and ball.xcor() < -320:
        ball.paddle_bounce()

    if ball.xcor() > 340:
        score.left_score_up()
        ball.moving_speed += .05
        ball.reset()

    elif ball.xcor() < -340:
        score.right_score_up()
        ball.moving_speed += .05
        ball.reset()



    screen.update()

screen.exitonclick()
