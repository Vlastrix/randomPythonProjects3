from turtle import Turtle
MOVEMENT = 20


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(coordinates)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        new_y = self.ycor() + MOVEMENT
        self.sety(new_y)

    def move_down(self):
        new_y = self.ycor() - MOVEMENT
        self.sety(new_y)
