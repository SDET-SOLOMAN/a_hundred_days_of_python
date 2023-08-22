import time
from day_18.food_class import Food
from day_18.snake_class import Snake
from day_18.score_class import Score
from turtle import Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Famous Nokia 3310 Snake Game")

food = Food()
snake = Snake()
scoring = Score()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while True:

    screen.update()
    snake.move()
    time.sleep(.1)

    if snake.head.distance(food) < 12:
        food.create_food()
        scoring.score_up()
        snake.extra_snake()

    if snake.head.xcor() > 280 or  snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoring.game_over()
        break

    if snake.is_tale():
        scoring.game_over()
        break

screen.exitonclick()
