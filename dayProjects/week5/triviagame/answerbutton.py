from tkinter import Button

class AnswerButton(Button):
    def __init__(self, parent, text, command = None):
        super().__init__(parent)
        self.config(text=text, width=30, height=2, font=("Arial", 14), bg="white", fg="black", wraplength=270)
        if command != None:
            self["command"] = command