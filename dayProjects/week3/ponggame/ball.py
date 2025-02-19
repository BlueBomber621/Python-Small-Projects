from turtle import Turtle

class Ball(Turtle):
    def __init__(self, xv, yv):
        super().__init__()
        self.xv = xv
        self.yv = yv
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto((0, 0))
    
    def move_ball(self):
        if abs(self.ycor()) > 270:
            self.yv *= -1
        self.goto((self.xcor() + self.xv, self.ycor() + self.yv))