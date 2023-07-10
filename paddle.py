from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, side):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)

        x = 0
        if str(side).lower() in ['left', 'right']:
            self.side = str(side).lower()
            x = 350
            if self.side == 'left':
                x = -350

        self.setpos(x=x, y=0)

    def up(self):
        y = self.pos()[1]
        self.sety(y=y+20)

    def down(self):
        y = self.pos()[1]
        self.sety(y=y-20)
