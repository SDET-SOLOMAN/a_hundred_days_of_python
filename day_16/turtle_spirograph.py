from turtle import Turtle, Screen
from random import choice, randint

sdet_soloman = Turtle('turtle')
sdet_soloman.speed(10)
screen = Screen()
screen.colormode(255)


def my_colors():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def spiro(numiko):
    for n in range(360 // numiko):
        sdet_soloman.color(my_colors())
        sdet_soloman.circle(100)
        sdet_soloman.setheading(sdet_soloman.heading() - numiko)

spiro(30)
screen.exitonclick()
