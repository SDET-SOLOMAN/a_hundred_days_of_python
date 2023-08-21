from random import choice, randint
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=700, height=600)
user_input = screen.textinput("Turtle race bet", 'Which turtle will win this race, make your bet: ')


def create_turtles(height, num_turtle):
    race_turtles = []
    number = - (height // num_turtle)
    colors = ['blue', 'red', 'pink', 'yellow', 'orange', 'black']
    for num in range(num_turtle):
        temp = Turtle('turtle')
        temp.color(colors[num])
        temp.penup()
        temp.setposition(-340, number)
        number += 50
        race_turtles.append(temp)
    return race_turtles


turtles = create_turtles(700, 6)

winner = ""
game = True
while game:
    for race_turtle in turtles:
        distance = randint(0, 20)
        race_turtle.forward(distance)
        if race_turtle.xcor() > 300:
            game = False
            winner = race_turtle.color()[0]
            break
print(f"The winner is {winner}")
if user_input.lower() == winner:
    print("You are winner!!!")
screen.exitonclick()
