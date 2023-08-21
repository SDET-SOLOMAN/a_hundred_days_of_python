from random import choice
from turtle import Turtle, Screen

sdet_soloman = Turtle('turtle')
sdet_soloman.speed(10)
screen = Screen()

def forward():
    sdet_soloman.forward(20)

def back():
    sdet_soloman.backward(20)


def anti_clock():
    sdet_soloman.left(20)

def clock():
    sdet_soloman.right(20)


screen.listen()
screen.onkey(key='w', fun=forward)
screen.onkey(key='s', fun=back)
screen.onkey(key='a', fun=anti_clock)
screen.onkey(key='d', fun=clock)





screen.exitonclick()