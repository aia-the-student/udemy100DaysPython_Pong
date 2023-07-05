from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.screensize(canvwidth=800, canvheight=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle()
left_paddle.set_side('left')

right_paddle = Paddle()
right_paddle.set_side('right')

screen.listen()

game_is_on = True
screen.update()


screen.exitonclick()