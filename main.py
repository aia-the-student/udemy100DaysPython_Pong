from turtle import Screen
from paddle import Paddle
from time import sleep

screen = Screen()
screen.screensize(canvwidth=800, canvheight=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle()
left_paddle.set_side('left')

right_paddle = Paddle()
right_paddle.set_side('right')

def right_paddle_up():
    right_paddle.move("up")


def right_paddle_down():
    right_paddle.move("down")


def left_paddle_up():
    left_paddle.move('up')


def left_paddle_down():
    left_paddle.move('down')


screen.listen()
screen.onkey(key='Up', fun=right_paddle_up)
screen.onkey(key='Down', fun=right_paddle_down)
screen.onkey(key='w', fun=left_paddle_up)
screen.onkey(key='s', fun=left_paddle_down)

game_is_on = True
screen.update()

i = 0
while game_is_on:
    sleep(0.5)
    i += 1
    screen.update()
    if i > 20:
        game_is_on = False



screen.exitonclick()