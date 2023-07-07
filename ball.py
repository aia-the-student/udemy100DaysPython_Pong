from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.7)
        self.penup()

        self.velocity = 20

        self.x_delta = self.velocity # velocity in delta x/y per second
        self.y_delta = self.velocity

    def move(self):
        current_pos = self.pos()
        self.setpos(x=current_pos[0]+self.x_delta
                    , y=current_pos[1]+self.y_delta)

    def bounce(self, wall):
        if wall == 'upper':
            self.y_delta = -self.velocity
        if wall == 'lower':
            self.y_delta = self.velocity
