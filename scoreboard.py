from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()

        self.right_score = 0
        self.left_score = 0

        self.update_scoreboard()

    def l_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.right_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.setpos(-100, 200)
        self.write(self.left_score, align='center', font=("Courier", 80, "normal"))
        self.setpos(100, 200)
        self.write(self.right_score, align='center', font=("Courier", 80, "normal"))
