import time
from turtle import Screen
from snake import *
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("SNAKE GAMEEEEEE!!!!")
screen.tracer(0)

snake = Snake()
food = Food()
score_b = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_b.score += 1
        score_b.display_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score_b.game_over()

    for body in snake.segments:
        if body == snake.head:
            pass
        else:
            if snake.head.pos() == body.pos():
                game_is_on = False
                score_b.game_over()




screen.exitonclick()
