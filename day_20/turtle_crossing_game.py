import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)

car = CarManager()
player = Player()
score = Scoreboard()

screen.setup(width=600, height=600)
screen.listen()
screen.onkey(player.up, 'Up')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    car.create_car()
    car.move()
    score.display_score()

    for cars in car.my_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            score.game_over()
    if player.is_restart():
        score.score_up()
        player.restart()
        car.speed_up()

screen.exitonclick()