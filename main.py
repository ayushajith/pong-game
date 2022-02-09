from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from middle import Middle
import time

X = 800
Y = 600

screen = Screen()
paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()
middle = Middle()


screen.setup(width=X, height=Y)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

screen.listen()
screen.onkey(fun=paddle_r.move_paddle_up, key="Up")
screen.onkey(fun=paddle_r.move_paddle_down, key="Down")
screen.onkey(fun=paddle_l.move_paddle_up, key="w")
screen.onkey(fun=paddle_l.move_paddle_down, key="s")

is_game_on = True
while is_game_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()

    # Detect collision with upper and lower wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # Detect collision with left paddle
    if ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # If the left paddle misses
    if ball.xcor() < -400:
        ball.ball_reset()
        scoreboard.r_score_is()

    # If the right paddle misses
    if ball.xcor() > 400:
        ball.ball_reset()
        scoreboard.l_score_is()

screen.exitonclick()
