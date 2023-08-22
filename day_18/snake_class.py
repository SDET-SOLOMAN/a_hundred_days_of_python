from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.snakes = []
        self.create_snakes()
        self.head = self.snakes[0]

    def create_snakes(self):
        for num in POSITIONS:
            self.add_snake(num)

    def add_snake(self, n):
        temp = Turtle('square')
        temp.color('white')
        temp.shapesize(1)
        temp.penup()
        temp.goto(n)
        self.snakes.append(temp)

    def extra_snake(self):
        self.add_snake(self.snakes[-1].position())

    def move(self):
        for num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[num - 1].xcor()
            new_y = self.snakes[num - 1].ycor()
            self.snakes[num].goto(new_x, new_y)
        self.snakes[0].forward(10)

    def is_tale(self):
        for snake in self.snakes[1:]:
            if self.head.distance(snake) < 10:
                return True
        return False

    def up(self):
        if self.snakes[0].heading() != 270:
            self.snakes[0].setheading(90)

    def down(self):
        if self.snakes[0].heading() != 90:
            self.snakes[0].setheading(270)

    def left(self):
        if self.snakes[0].heading() != 0:
            self.snakes[0].setheading(180)

    def right(self):
        if self.snakes[0].heading() != 180:
            self.snakes[0].setheading(0)
