from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

WIDTH = 800
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH,height=HEIGHT)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
delay = 0.1
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    if ball.xcor() >= 330 and ball.distance(r_paddle) < 58 or ball.xcor() <= -330 and ball.distance(l_paddle) < 58:
        ball.bounce_paddle()

    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.score()
        scoreboard.update_score()

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.score()
        scoreboard.update_score()
    if scoreboard.l_score > 10 or scoreboard.r_score > 10:
        scoreboard.winner()
        game_is_on = False
screen.exitonclick()