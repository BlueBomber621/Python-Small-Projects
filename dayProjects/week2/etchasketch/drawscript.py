from turtle import Turtle, Screen

pen = Turtle("circle")
pen.color("cyan")
pen.pencolor("black")
pen.shapesize(0.2, 0.2)

view = Screen()
view.bgcolor(0.95, 0.97, 0.87)

def move_right():
    pen.setx(pen.pos()[0] + 5)

def move_left():
    pen.setx(pen.pos()[0] - 5)

def move_up():
    pen.sety(pen.pos()[1] + 5)

def move_down():
    pen.sety(pen.pos()[1] - 5)

def clear_art():
    pen.clear()

# Use WASD to move pen, press C to clear your drawings
view.listen()
view.onkey(key="d", fun=move_right)
view.onkey(key="a", fun=move_left)
view.onkey(key="w", fun=move_up)
view.onkey(key="s", fun=move_down)
view.onkey(key="c", fun=clear_art)
view.exitonclick()