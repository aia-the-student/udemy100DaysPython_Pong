from turtle import Screen
from paddle import Paddle
from time import sleep
from ball import Ball

screen = Screen()
screen.screensize(canvwidth=800, canvheight=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle(side='left')
right_paddle = Paddle(side='right')

ball = Ball()

screen.listen()
screen.onkey(key='Up', fun=right_paddle.up)
screen.onkey(key='Down', fun=right_paddle.down)
screen.onkey(key='w', fun=left_paddle.up)
screen.onkey(key='s', fun=left_paddle.down)

game_is_on = True
screen.update()

i = 0
while game_is_on:
    sleep(0.5)
    i += 1
    ball.move()

    if ball.ycor() > 300:
        ball.bounce('upper')
    if ball.ycor() < -300:
        ball.bounce('lower')

    screen.update()
    if i > 20:
        game_is_on = False

screen.exitonclick()
