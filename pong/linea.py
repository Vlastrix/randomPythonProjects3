from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.center_line()
        self.hideturtle()

    def center_line(self):
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 295)
        self.pensize(2)
        self.setheading(270)
        for _ in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
