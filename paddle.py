from turtle import Turtle

UP = 90
DOWN = 270


class Paddle:

    def __init__(self):
        self.paddle = []
        self.side = None

    def set_side(self, side):
        if str(side).lower() in ['left', 'right']:
            self.side = str(side).lower()
            x = 350
            if self.side == 'left':
                x = -350

            for i in range(5):
                trt = Turtle()
                trt.penup()
                trt.shape('square')
                trt.color('white')
                trt.setpos(x=x, y=-40+i*20)
                self.paddle.append(trt)

    def move(self, direction):
        heading = 0
        if str(direction).lower() == 'up':
            heading = UP
        if str(direction).lower() == 'down':
            heading = DOWN

        if heading in (UP, DOWN):
            for trt in self.paddle:
                trt.setheading(heading)
                trt.forward(20)
