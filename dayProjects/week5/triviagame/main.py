from triviafunction import TriviaFunction
from answerbutton import AnswerButton
from questionframe import QuestionFrame
from questionlist import get_questions
from tkinter import Tk, Label, mainloop

# Variables
question_answer_buttons = []

current_round = 1

# Display
view = Tk()
view.config(padx=50, pady=50, bg="gray")

# Button Reaction
def trigger_answer(input):
    print(input)

# Continue Function
def continue_question():
    global current_round, question_answer_buttons
    if trivia.question_number < len(trivia.questions):
        trivia.question_number += 1
        setup_questions(trivia.questions[trivia.question_number - 1])
    elif current_round < 3:
        current_round += 1
        setup_round(current_round)
        setup_questions(trivia.questions[0])
    else:
        for button in question_answer_buttons:
            button.grid_remove()
        question_answer_buttons.clear()
        category_label.grid_remove()
        displayed_question.itemconfig(displayed_question.label, fill="black")
        trivia.question_typer(f"Congratulations, you completed the trivia with a score of:\n{trivia.score}/{trivia.maxscore}", displayed_question)
        

# Setup round
def setup_round(round = int):
    rounds = ["easy", "medium", "hard"]
    trivia.questions = get_questions(rounds[round - 1])
    trivia.question_number = 1

def setup_questions(question):
    global question_answer_buttons
    for button in question_answer_buttons:
        button.grid_remove()
    question_answer_buttons.clear()
    question_answer_buttons = trivia.question_setup(AnswerButton)
    for button in question_answer_buttons:
        button.grid(row=round(question_answer_buttons.index(button) / 2 + 1.99), column=(question_answer_buttons.index(button) % 2))
    

# Question Display
category_label = Label(text="Category:", font=("Arial", 28, "bold"), fg="#eee", bg="gray")
category_label.grid(row=0, column=0, columnspan=2)

displayed_question = QuestionFrame(view)
displayed_question.grid(row=1, column=0, columnspan=2)

trivia = TriviaFunction(displayed_question, view, category_label, continue_question)

# Initialize functionality
setup_round(current_round)
setup_questions(trivia.questions[0])

mainloop()