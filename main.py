from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from gameover import GameOver
import time

screen = Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food = Food()
scoreboard = Scoreboard()
gameover = GameOver()

screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")
scoreboard.show_score()

game_is_on= True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    # Detect collision with wall.
    if snake.head.xcor()>280 or snake.head.xcor() < -300 or snake.head.ycor()>300 or snake.head.ycor()<-280:
        gameover.game_over_display()
        game_is_on = False

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            gameover.game_over_display()
            game_is_on = False

screen.exitonclick()