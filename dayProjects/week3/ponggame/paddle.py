from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.goto(pos)
        self.shapesize(stretch_len=1, stretch_wid=5)

    def up(self):
        if self.ycor() < 225:
            self.goto((self.xcor(), self.ycor() + 25))

    def down(self):
        if self.ycor() > -225:
            self.goto((self.xcor(), self.ycor() - 25))