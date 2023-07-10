from turtle import Turtle
# from numpy import sign

# VELOCITY_INCREASE = 2
INITIAL_MOVE_SPEED = 0.2

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.7)
        self.penup()

        self.velocity = 10
        self.x_delta = self.velocity
        self.y_delta = self.velocity
        self.move_speed = INITIAL_MOVE_SPEED

    def move(self):
        current_pos = self.pos()
        self.setpos(x=current_pos[0]+self.x_delta, y=current_pos[1]+self.y_delta)

    def bounce_y(self):
        self.y_delta *= -1

    def bounce_x(self):
        self.x_delta *= -1

    def restart(self):
        self.setpos(0, 0)
        self.x_delta *= -1
        self.move_speed = INITIAL_MOVE_SPEED

    def increase_speed(self):
        self.move_speed *= 0.9
        # self.x_delta += sign(self.x_delta)*VELOCITY_INCREASE
        # self.y_delta += sign(self.y_delta)*VELOCITY_INCREASE
