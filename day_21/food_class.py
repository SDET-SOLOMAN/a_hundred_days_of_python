from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()

    def create_food(self):
        self.penup()
        self.shape('circle')
        self.shapesize(.5)
        self.color("red")
        self.speed('fastest')
        self.location_of_food()

    def location_of_food(self):
        new_x = randint(-200, 200)
        new_y = randint(-200, 200)
        self.goto(new_x, new_y)
