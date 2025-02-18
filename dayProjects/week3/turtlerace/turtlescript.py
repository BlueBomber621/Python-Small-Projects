from turtle import Turtle, Screen
import random

race_on = False
winner_turtle = "None"

view = Screen()
view.bgcolor(0.1, 0.38, 0.1)

turtles = [Turtle(), Turtle(), Turtle(), Turtle(), Turtle(), Turtle()]
def init_turtle(turtle, ylv, colored):
    turtle.shape("turtle")
    turtle.penup()
    turtle.setpos(-300, ylv)
    turtle.color(colored)

def move_turtle(turtle):
    turtle.forward(random.randint(1, 10))
    
for i in range(6):
    color_index = ["red", "orange", "yellow", "green", "blue", "purple"]
    init_turtle(turtles[i], -50 + (i * 20), color_index[i])

user_bet = view.textinput("Bet", "Pick a color to bet on:").lower()

if user_bet:
    race_on = True

while race_on:
    for turtle in turtles:
        move_turtle(turtle)
        if turtle.pos()[0] > 299:
            race_on = False
            winner_turtle = turtle.color()[0]

if user_bet == winner_turtle:
    print(f"You won! {winner_turtle.capitalize()} turtle was the winning color!")
else:
    print(f"You lose! {winner_turtle.capitalize()} turtle was the winning color!")

view.exitonclick()