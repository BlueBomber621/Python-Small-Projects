from turtle import Screen
from turtleplayer import TPlayer
from text import Text
from car import Car
import time
from levels import car_levels

view = Screen()
view.setup(width=560, height=600)
view.tracer(0)

game_running = False
level = 1

player = TPlayer()
level_text = Text("Level: 1", (-220, 260), "black", 18)
game_over_text = Text("", (0, 0), "red", 50)

cars = []
def add_car(speed, color, pos, time):
    global cars
    new_car = Car(speed, color, time)
    new_car.sety(pos)
    cars.append(new_car)

def level_setup():
    global cars
    global level
    global car_levels
    for car in cars:
        car.hideturtle()
    cars = []
    if level <= len(car_levels):
        for car_data in car_levels[level - 1]:
            add_car(car_data[0], car_data[1], car_data[2], car_data[3])
    else:
        for car_data in car_levels[(level - 1) % len(car_levels)]:
            add_car(car_data[0], car_data[1], car_data[2], car_data[3])
        for car in cars:
            for i in range(10):
                car.move()
        for car_data in car_levels[(level + 6) % len(car_levels)]:
            add_car(car_data[0], car_data[1], car_data[2], car_data[3])

game_running = True

view.listen()
view.onkey(key="w", fun=player.move)
view.onkey(key="Up", fun=player.move)
level_setup()

while game_running:
    view.update()
    player_hit = False
    for car in cars:
        car.move()
        if (player_hit == False) and car.check_col(player):
            player_hit = True
    if player_hit:
        player.color("red")
        game_over_text.rewrite("Game Over")
        game_running = False
        view.update()
    elif player.ycor() > 270:
        player.sety(-280)
        level += 1
        level_text.rewrite(f"Level: {level}")
        level_setup()

    time.sleep(0.05)

view.exitonclick()