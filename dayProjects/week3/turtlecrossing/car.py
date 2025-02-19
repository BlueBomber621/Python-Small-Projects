from turtle import Turtle

class Car(Turtle):
    def __init__(self, speed, color, wait):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setx(-270)
        self.speedamt = speed
        self.waitamt = 0
        self.waitmax = wait
        self.color(color)
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)

    def move(self):
        if self.xcor() < -260 and self.waitamt <= 0:
            self.setx(260)
            self.waitamt = self.waitmax
            self.showturtle()
        elif self.xcor() < -260 and self.waitamt > 0 and self.isvisible():
            self.hideturtle()
        elif self.xcor() < -260 and self.waitamt > 0:
            self.waitamt -= 1
        else:
            self.goto(self.xcor() - self.speedamt, self.ycor())

    def check_col(self, player):
        my_hit = (self.xcor() + 20, self.xcor() - 20, self.ycor() + 10, self.ycor() - 10)
        p_hit = (player.xcor() + 10, player.xcor() - 10, player.ycor() + 10, player.ycor() - 10)

        return my_hit[0] >= p_hit[1] and p_hit[0] >= my_hit[1] and my_hit[2] >= p_hit[3] and p_hit[2] >= my_hit[3]