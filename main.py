from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) <= 15:
        snake.extend()
        food.refresh()
        scoreboard.scoring()

    if (
        snake.head.xcor() >= 290
        or snake.head.xcor() <= -290
        or snake.head.ycor() >= 290
        or snake.head.ycor() <= -290
    ):
        snake.reset()
        scoreboard.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            scoreboard.reset()


screen.exitonclick()
