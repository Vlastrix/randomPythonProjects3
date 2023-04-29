from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-290, 260)
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.home()
        self.write(arg="Game Over", align="center", font=FONT)
