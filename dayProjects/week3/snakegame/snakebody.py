from turtle import Turtle

class Snake:
    def __init__(self):
        self.snake_body = []
        self.snake_dir = 0
    
    def new_body(self, pos):
        new_part = Turtle()
        new_part.penup()
        new_part.shape("square")
        if (len(self.snake_body) + 1) % 5 == 0:
            new_part.color("cyan")
        elif len(self.snake_body) % 2 == 0:
            new_part.color("lime")
        else:
            new_part.color("green")
        new_part.speed("fastest")
        new_part.goto(pos)
        self.snake_body.append(new_part)

    def up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)

    def down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)

    def left(self):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)

    def right(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)

    def move_forward(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[i].goto(self.snake_body[i - 1].pos())
        self.snake_body[0].forward(20)
