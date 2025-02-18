from questions import Question
from data import *
from quizfunction import QuizFunction

answer_results = {"correct": 0, "incorrect": 0}
cont_game = True

def question_bank_setup(dataset):
    bank_return = []
    for question in dataset:
        question_q = question["question"]
        question_a = question["answer"]
        question_obj = Question(question_q, question_a)
        bank_return.append(question_obj)
    return bank_return

def continue_check(dataset, category):
    global answer_results
    global cont_game
    answer_perc = round(float(answer_results["correct"] / (answer_results["correct"] + answer_results["incorrect"])), 4)
    if answer_perc > 0.75:
        print(f"Your have {answer_perc * 100}% of the answers correct, continuing:")
        print("Category: " + category)
        question_bank = question_bank_setup(dataset)
        quiz_section = QuizFunction(question_bank)
        for i in range(1, len(question_bank) + 1):
            result = quiz_section.pull_question()
            if result:
                answer_results["correct"] += 1
            else:
                answer_results["incorrect"] += 1
    else:
        print(f"Game Over! You answered {answer_results['correct']} correct of {answer_results['correct'] + answer_results['incorrect']} questions, with an accuracy of {answer_perc * 100}%")
        cont_game = False

question_bank = question_bank_setup(question_data_animals)

print("Welcome to the quiz! Get above 75%" + " correct to pass each section!")
print("Category: Animals")

quiz_section1 = QuizFunction(question_bank)
for i in range(1, len(question_bank) + 1):
    result = quiz_section1.pull_question()
    if result:
        answer_results["correct"] += 1
    else:
        answer_results["incorrect"] += 1

if cont_game:
    continue_check(question_data_history, "History")
if cont_game:
    continue_check(question_data_geology, "Geology")
if cont_game:
    continue_check(question_data_science_math, "Science & Math")
if cont_game:
    continue_check(question_data_final_hard, "Final")

if cont_game:
    answer_perc = round(float(answer_results["correct"] / (answer_results["correct"] + answer_results["incorrect"])), 4)
    if answer_perc > 0.75:
        print(f"Congradulations! You completed the quiz with {answer_perc * 100}% correct!")
        ranking = ""
        if answer_perc > 0.97:
            ranking = "S"
        elif answer_perc > 0.91:
            ranking = "A"
        elif answer_perc > 0.85:
            ranking = "B"
        elif answer_perc > 0.782:
            ranking = "C"
        else:
            ranking = "D"
        print("Your rank: " + ranking)
        if ranking == "S":
            print("You're very smart! Good Job!")
        else:
            print("Do you think you can do better?")
    else:
        print(f"Game Over! You answered {answer_results['correct']} correct of {answer_results['correct'] + answer_results['incorrect']} questions, with an accuracy of {answer_perc * 100}%")