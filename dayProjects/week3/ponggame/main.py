from turtle import Screen
from paddle import Paddle
from ball import Ball
from text import Text
import time

view = Screen()
view.setup(width=720, height=560)
view.bgcolor("black")
view.title("Pong")
view.tracer(0)

game_running = False
p1_score = 0
p2_score = 0
required_score = round(view.numinput("Points to Win", "How many points will be needed to win this match?", 3))
if required_score < 1 or required_score > 100:
    required_score = 3

p1_scoreboard = Text("0", (-100, 220), "white", 36)
p2_scoreboard = Text("0", (100, 220), "white", 36)
winner_text = Text("", (0, 0), "white", 50)

p1_paddle = Paddle((-320, 0))
p2_paddle = Paddle((320, 0))
ball = Ball(5, 5)

view.listen()
view.onkey(key="w", fun=p1_paddle.up)
view.onkey(key="s", fun=p1_paddle.down)
view.onkey(key="Up", fun=p2_paddle.up)
view.onkey(key="Down", fun=p2_paddle.down)

game_running = True
winner_text.rewrite(str(round(required_score)) + " point match.")
view.update()
time.sleep(1)
winner_text.rewrite("Begin")
view.update()
time.sleep(1)
winner_text.rewrite("")

while game_running:
    view.update()
    ball.move_ball()
    if abs(ball.xcor()) > 340:
        if ball.xcor() > 0:
            p1_score += 1
            p1_scoreboard.rewrite(str(p1_score))
        else:
            p2_score += 1
            p2_scoreboard.rewrite(str(p2_score))
        ball.goto((0,0))
        ball.xv /= (ball.xv / -5)
        ball.yv /= (abs(ball.yv) / 5)
    if ((ball.distance(p2_paddle) < 20 or (ball.xcor() > 300 and ball.distance(p2_paddle) < 60)) and ball.xv > 0) or ((ball.distance(p1_paddle) < 20 or (ball.xcor() < -300 and ball.distance(p1_paddle) < 60)) and ball.xv < 0):
        ball.xv = round(ball.xv * -1.25)
        ball.yv = round(ball.yv * 1.5)
    time.sleep(0.05)
    if p1_score > required_score - 1:
        p1_paddle.hideturtle()
        p2_paddle.hideturtle()
        ball.hideturtle()
        winner_text.rewrite("Player 1")
        view.update()
        time.sleep(0.5)
        winner_text.rewrite("Player 1 Wins")
        view.update()
        game_running = False
    if p2_score > required_score - 1:
        p1_paddle.hideturtle()
        p2_paddle.hideturtle()
        ball.hideturtle()
        winner_text.rewrite("Player 2")
        view.update()
        time.sleep(0.5)
        winner_text.rewrite("Player 2 Wins")
        view.update()
        game_running = False

view.exitonclick()