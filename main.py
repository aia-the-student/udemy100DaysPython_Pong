from turtle import Screen
from paddle import Paddle
from time import sleep
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.screensize(canvwidth=800, canvheight=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle(side='left')
right_paddle = Paddle(side='right')

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='Up', fun=right_paddle.up)
screen.onkey(key='Down', fun=right_paddle.down)
screen.onkey(key='w', fun=left_paddle.up)
screen.onkey(key='s', fun=left_paddle.down)

game_is_on = True
screen.update()

while game_is_on:
    sleep(ball.move_speed)
    ball.move()

    if abs(ball.ycor()) > 280:
        ball.bounce_y()

    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or \
            (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.increase_speed()
        ball.bounce_x()

    if ball.xcor() > 360:
        ball.restart()
        scoreboard.l_point()

    if ball.xcor() < -360:
        ball.restart()
        scoreboard.r_point()

    screen.update()

screen.exitonclick()
