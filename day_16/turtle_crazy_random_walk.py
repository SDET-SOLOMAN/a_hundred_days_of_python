from turtle import Turtle, Screen
from random import choice, randint

sdet_soloman = Turtle('turtle')
sdet_soloman.pensize(10)
screen = Screen()
screen.colormode(255)

angles = [360, 270, 180, 90, 0]

def my_colors():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b

# different shapes
# for num in range(3, 11):
#     sdet_soloman.color(choice(colours))
#     angle = 360 / num
#     for num2 in range(1, num + 1):
#         sdet_soloman.forward(100)
#         sdet_soloman.right(angle)


# random walk

def walk(num):
    for n in range(num + 1):
        sdet_soloman.color(my_colors())
        sdet_soloman.setheading(choice(angles))
        sdet_soloman.forward(20)


walk(90)
screen.exitonclick()