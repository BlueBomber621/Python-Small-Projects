from turtle import Turtle

class TPlayer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.speed("fastest")
        self.goto((0, -280))
        self.setheading(90)

    def move(self):
        self.sety(self.ycor() + 10)