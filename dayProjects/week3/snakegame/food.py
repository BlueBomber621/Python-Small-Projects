from turtle import Turtle

class Food(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("red")
        self.speed("fastest")
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.goto(pos)