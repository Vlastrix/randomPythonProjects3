from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.color("turquoise1")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        self.equis = 300

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(arg=self.r_score, align="center", font=("Courier", 60, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
