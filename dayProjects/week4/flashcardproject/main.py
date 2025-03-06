import tkinter
import tkinter.messagebox
import pandas
import random

# Pallet
LTEAL = "#8feab0"
TEAL = "#24aaaa"
DTEAL = "#148888"
DMAGENTA = "#681170"
DSILVER = "#33363a"

# Functions
df = {}
try:
    df = pandas.read_csv("dayProjects/week4/flashcardproject/words_to_learn.csv").to_dict()
    if len(df["spanish"]) < 1:
        df = pandas.read_csv("dayProjects/week4/flashcardproject/words.csv").to_dict()
except FileNotFoundError:
    df = pandas.read_csv("dayProjects/week4/flashcardproject/words.csv").to_dict()
current_list = df
current_list["spanish"] = [df["spanish"][key] for key in df["spanish"]]
current_list["english"] = [df["english"][key] for key in df["english"]]
learn_words = {
    "spanish": [],
    "english": []
}
word_index = 0

def flip_card():
    global current_list, word_index
    view.flashcard_flip = None
    if len(current_list["english"]) > 0:
        word_select = current_list["english"][word_index]
        flashcard.itemconfig(flashcard_title, text="English")
        flashcard.itemconfig(flashcard_answer, text=word_select)

def new_card():
    global current_list, word_index, learn_words
    if len(current_list["spanish"]) > 0:
        if view.flashcard_flip is not None:
            view.after_cancel(view.flashcard_flip)
        word_index = random.randint(0, min(len(current_list["spanish"]), len(current_list["english"])) - 1)
        word_select = current_list["spanish"][word_index]
        flashcard.itemconfig(flashcard_title, text="Spanish")
        flashcard.itemconfig(flashcard_answer, text=word_select)
        view.flashcard_flip = view.after(3000, flip_card)
    else:
        flashcard.itemconfig(flashcard_title, text="Congratulations")
        flashcard.itemconfig(flashcard_answer, text="Cards finished!")
        if not view.complete:
            view.complete = True
            dataframe = pandas.DataFrame(learn_words)
            dataframe.to_csv(path_or_buf="dayProjects/week4/flashcardproject/words_to_learn.csv", index=False, encoding="utf-8")
            tkinter.messagebox.showinfo("Complete", "Run again to practice cards you missed!")

def correct_card():
    global current_list, word_index
    if len(current_list["spanish"]) > 0:
        del current_list["spanish"][word_index]
        del current_list["english"][word_index]
    new_card()

def false_card():
    global current_list, word_index, learn_words
    if len(current_list["spanish"]) > 0:
        if not learn_words["spanish"].__contains__(current_list["spanish"][word_index]):
            learn_words["spanish"].append(current_list["spanish"][word_index])
            learn_words["english"].append(current_list["english"][word_index])
    new_card()


# Window
view = tkinter.Tk()
view.config(background=TEAL, padx=50, pady=50)
view.flashcard_flip = None
view.complete = False

# Canvas
flashcard = tkinter.Canvas(background=TEAL, width=800, height=526, highlightthickness=0)
flashcard_image = tkinter.PhotoImage(file="dayProjects/week4/flashcardproject/CardFront.png")
flashcard.create_image(400, 260, image=flashcard_image)
flashcard_title = flashcard.create_text(400, 150, text="Card Title", font=("Arial", 40, "italic"))
flashcard_answer = flashcard.create_text(400, 260, text="Card Answer", font=("Arial", 60, "bold"))
flashcard.grid(column=0, row=0, columnspan=2)

# Buttons
no_image = tkinter.PhotoImage(file="dayProjects/week4/flashcardproject/NoButton.png")
yes_image = tkinter.PhotoImage(file="dayProjects/week4/flashcardproject/YesButton.png")
no_button = tkinter.Button(image=no_image, highlightthickness=0, bg=TEAL, activebackground=DTEAL, padx=5, pady=5, command=false_card)
no_button.grid(column=0, row=1)
yes_button = tkinter.Button(image=yes_image, highlightthickness=0, bg=TEAL, activebackground=DTEAL, padx=5, pady=5, command=correct_card)
yes_button.grid(column=1, row=1)

new_card()

tkinter.mainloop()