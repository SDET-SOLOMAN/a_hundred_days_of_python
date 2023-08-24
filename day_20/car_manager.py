from turtle import Turtle
from random import choice, randint, random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
Y_COR_UPPER = 280
Y_COR_LOWER = -280
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = STARTING_MOVE_DISTANCE
        self.my_cars = []

    def create_car(self):
        for char in range(0, 12):
            if char == randint(0, 33):
                char = Turtle()
                char.shape('square')
                char.shapesize(stretch_wid=1, stretch_len=randint(1, 3) * .9)
                char.color(choice(COLORS))
                char.penup()
                char.goto(320, randint(Y_COR_LOWER, Y_COR_UPPER))
                self.my_cars.append(char)

    def move(self):
        for car in self.my_cars:
            car.backward(self.level)

    def speed_up(self):
        self.level += MOVE_INCREMENT
