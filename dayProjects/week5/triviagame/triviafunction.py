import random

class TriviaFunction():
    def __init__(self, canvas, view, category, cont_func):
        self.score = 0
        self.maxscore = 0
        self.question_number = 1
        self.questions = []
        self.ready_answer = False
        self.cont_func = cont_func
        self.aft_typer = None
        self.canvas = canvas
        self.view = view
        self.category_label = category

    # Handles the typing of the canvas text character at a time
    def question_typer(self, lasttext, canvas, currenttext = ""):
        if len(currenttext) < len(lasttext):
            currenttext += lasttext[len(currenttext)]
            canvas.itemconfig(canvas.label, text=currenttext)
            self.aft_typer = self.view.after(50, self.question_typer, lasttext, canvas, currenttext)

    # Handles making the answer buttons for the current question
    def question_setup(self, button_temp):
        self.ready_answer = True
        self.canvas.itemconfig(self.canvas.label, fill="black")
        if self.aft_typer != None:
            self.view.after_cancel(self.aft_typer)
            self.aft_typer = None
        self.category_label["text"] = self.questions[self.question_number - 1]["category"]
        return_buttons = [button_temp(self.view, entry, self.trigger_false) for entry in self.questions[self.question_number - 1]["incorrect_answers"]]
        return_buttons.insert(0, button_temp(self.view, self.questions[self.question_number - 1]["correct_answer"], self.trigger_true))
        random.shuffle(return_buttons)
        self.aft_typer = self.view.after(50, self.question_typer, self.questions[self.question_number - 1]["question"], self.canvas)
        return return_buttons
    
    # Functions to connect to buttons to trigger an answer check accordingly
    def trigger_false(self):
        if self.ready_answer:
            self.answer_check(0)

    def trigger_true(self):
        if self.ready_answer:
            self.answer_check(1)

    # Checks if the answer was right or wrong and handles logic accordingly
    def answer_check(self, answer):
        if self.aft_typer != None:
            self.view.after_cancel(self.aft_typer)
            self.aft_typer = None
        self.ready_answer = False
        self.maxscore += 1
        if answer == 1:
            self.canvas.itemconfig(self.canvas.label, fill="green")
            self.score += 1
            self.view.after(50, self.question_typer, f"Correct!\nScore: {self.score}/{self.maxscore}", self.canvas)
        else:
            self.canvas.itemconfig(self.canvas.label, fill="maroon")
            self.view.after(50, self.question_typer, f"Incorrect!\nScore: {self.score}/{self.maxscore}", self.canvas)
        # After 4.4 seconds, continue to the next function through the main functionality
        self.view.after(4400, self.cont_func)