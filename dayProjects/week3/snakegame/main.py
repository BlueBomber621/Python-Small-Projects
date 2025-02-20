from turtle import Screen
from snakebody import Snake
from food import Food
from text import Text
import time
import random


view = Screen()
view.setup(width=600, height=600)
view.bgcolor("black")
view.title("My Snake Game")
view.tracer(0)

player_snake = Snake()
for i in range(3):
    player_snake.new_body((0 - i * 20, 0))

highscore = 0
try:
    with open("./dayProjects/week3/snakegame/highscore.txt", mode="r") as file:
        highscore = int(file.read())
except:
    highscore = 0

game_running = True
time_space = 0.25
snake_score = 0

def turn(turn):
    if turn == "up":
        player_snake.up()
    elif turn == "down":
        player_snake.down()
    elif turn == "left":
        player_snake.left()
    elif turn == "right":
        player_snake.right()
    view.update()

view.listen()
view.onkeypress(key="Up", fun=player_snake.up)
view.onkeypress(key="Down", fun=player_snake.down)
view.onkeypress(key="Left", fun=player_snake.left)
view.onkeypress(key="Right", fun=player_snake.right)

new_food = Food((random.randint(-14, 14) * 20, random.randint(-14, 14) * 20))
scoreboard = Text("Score: 0", (-120, 260), "white")
highscoreboard = Text("Highscore: " + str(highscore), (120, 260), "white")
game_over_text = Text("", (0, 0), "red")

while game_running:
    view.update()
    if len(player_snake.snake_body) > 25:
        time_space = 0.075
    elif len(player_snake.snake_body) > 15:
        time_space = 0.1
    elif len(player_snake.snake_body) > 5:
        time_space = 0.2
    else:
        time_space = 0.25
    player_snake.move_forward()
    if abs(player_snake.snake_body[0].xcor()) > 295 or abs(player_snake.snake_body[0].ycor()) > 295:
        game_over_text.rewrite("Game Over")
        game_running = False
    for body in player_snake.snake_body[1:len(player_snake.snake_body)]:
        if player_snake.snake_body[0].distance(body) < 10:
            game_over_text.rewrite("Game Over")
            game_running = False
    if player_snake.snake_body[0].distance(new_food) < 15 and game_running:
        snake_score += 1
        scoreboard.rewrite("Score: " + str(snake_score))
        player_snake.new_body(player_snake.snake_body[-1].pos())
        new_food.goto((random.randint(-14, 14) * 20, random.randint(-14, 14) * 20))
    time.sleep(time_space)
    if snake_score > highscore:
        with open("./dayProjects/week3/snakegame/highscore.txt", mode="w") as file:
            file.write(str(snake_score))
            highscore = snake_score
            highscoreboard.rewrite("Highscore: " + str(highscore))


view.exitonclick()