import turtle
import pandas

data = pandas.read_csv("./dayProjects/week3/USstatesgame/50_states.csv")
state_names = data["state"].tolist()
state_guess = []

game_running = False

view = turtle.Screen()
view.title("US States Game")
image = "./dayProjects/week3/USstatesgame/blank_states_img.gif"
view.addshape(image)
view.tracer(0)

background = turtle.Turtle()
background.shape(image)
background.penup()
background.speed("fastest")
view.update()

game_running = True

while game_running:
    guess = view.textinput(f"{len(state_guess)}/50 States Guessed", "Guess one of the 50 states.")
    if guess == "" or not guess:
        guess = "exit"
    if guess.lower() == "exit":
        missed_states = [state for state in state_names if not state_guess.__contains__(state)]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("./dayProjects/week3/USstatesgame/states_to_learn.csv")
        game_running = False
    elif guess != "" and type(guess) == str:
        guess = guess.lower().title()
        if state_names.__contains__(guess) and (not state_guess.__contains__(guess)):
            state_guess.append(guess)
            guessed_state = data[data.state == guess]
            background.goto(guessed_state.x.item(), guessed_state.y.item())
            background.write(guess, False, "center", ("Arial", 8, "normal"))
            background.goto(0, 0)
        else:
            if state_names.__contains__(guess) and state_guess.__contains__(guess):
                background.goto(0, -290)
                background.write("Already guessed that! You lose!", ("Arial", 16, "normal"))
                background.goto(0, 0)
                game_running = False
            else:
                background.goto(0, -290)
                background.write("Not one of the states! You lose!", ("Arial", 16, "normal"))
                background.goto(0, 0)
                game_running = False
        if len(state_names) <= len(state_guess):
            background.goto(0, -290)
            background.write("You got all the states! You win!", ("Arial", 16, "normal"))
            background.goto(0, 0)
            game_running = False

        if not game_running:
            missed_states = [state for state in state_names if not state_guess.__contains__(state)]
            new_data = pandas.DataFrame(missed_states)
            new_data.to_csv("./dayProjects/week3/USstatesgame/states_to_learn.csv")
            game_running = False
            choice = view.textinput("Retry", "Want to try again? Y/N")
            if choice != "":
                choice = choice.lower()
            if choice == "y":
                state_guess = []
                background.clear()
                game_running = True

    view.update()

view.bye()