from tkinter import Canvas

class QuestionFrame(Canvas):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(bg="white", width=300, height=300)
        self.label = self.create_text(150, 150, fill="black", font=("Arial", 16), justify='center', width=250)