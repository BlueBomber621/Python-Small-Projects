from turtle import Turtle, Screen
import random
import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('dayProjects/week2/turtlehinterpainting/image.jpg', 30)

color_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_list.append((round((r/255), 4), round((g/255), 4), round((b/255), 4)))
turtle1 = Turtle()
turtle1.shape("arrow")
turtle1.color("black")
turtle1.pensize(10)
turtle1.penup()
turtle1.speed(0)
turtle1.setposition(x=-160, y=-160)

def dot_press(turtle):
    turtle.pendown()
    turtle.forward(0.01)
    turtle.backward(0.01)
    turtle.penup()

for _ in range(256):
    turtle1.pencolor(random.choice(color_list))
    dot_press(turtle1)
    turtle1.forward(20)
    if turtle1.position()[0] >= 160:
        turtle1.setx(-160)
        turtle1.sety(turtle1.pos()[1] + 20)

view = Screen()
view.bgcolor("white")

view.delay(500)
view.exitonclick()