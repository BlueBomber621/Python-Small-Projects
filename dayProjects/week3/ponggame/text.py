from turtle import Turtle

class Text(Turtle):
    def __init__(self, init_text, pos, color, size):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.color(color)
        self.hideturtle()
        self.goto(pos)
        self.size = size
        self.write(init_text, False, "center", ("Arial", self.size, "normal"))
    
    def rewrite(self, new_text):
        self.clear()
        self.write(new_text, False, "center", ("Arial", self.size, "normal"))