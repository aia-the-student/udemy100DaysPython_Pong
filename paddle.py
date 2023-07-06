from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.side = None

    def set_side(self, side):
        x = 0
        if str(side).lower() in ['left', 'right']:
            self.side = str(side).lower()
            x = 350
            if self.side == 'left':
                x = -350

        self.setpos(x=x, y=0)

    def move(self, direction):
        y = self.pos()[1]
        delta = 0
        if direction == 'up':
            delta = 20
        if direction == 'down':
            delta = -20
        self.sety(y=y+delta)
