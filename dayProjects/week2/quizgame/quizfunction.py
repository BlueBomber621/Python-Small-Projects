import random

class QuizFunction:
    def __init__(self, question_list):
        self.current_question = 0
        self.questions = question_list

    def pull_question(self):
        self.current_question += 1
        new_question = self.questions[random.randint(0, len(self.questions) - 1)]
        self.questions.remove(new_question)
        pchoice = input(str(self.current_question) + ". " + new_question.question + " (True/False): ").lower()
        if pchoice == new_question.answer.lower():
            print("Correct!")
            return True
        else:
            print("Incorrect!")
            return False
        