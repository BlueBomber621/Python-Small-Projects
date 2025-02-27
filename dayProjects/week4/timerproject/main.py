import tkinter
import math

# CONSTANTS
YELLOW = "#d3d399"
YELORANGE = "#b9a06a"
VIOLET = "#6e336f"
SILVER = "#4a5555"
FONT_NAME = "Georgia"
CHECKMARK_TIME = 15

# Functions
timer = 0
timer_action = None
timer_cont = False
def timer_format(timer):
    if timer < 3600:
        return f"{math.floor(timer / 60)}:{math.floor((timer % 60) / 10)}{timer % 10}"
    else:
        return f"{math.floor(timer / 3600)}:{math.floor((timer % 3600) / 600)}{math.floor(((timer % 3600) / 60) % 10)}:{math.floor((timer % 60) / 10)}{timer % 10}"

def start_timer():
    global timer
    if time_input.get() != "":
        timer = int(time_input.get()) + 1
    else:
        timer = CHECKMARK_TIME * 60 + 1
    if not timer_cont:
        tick()
def reset_timer():
    global timer, timer_cont
    timer = 0
    lime.itemconfig(lime_text, text=timer_format(0))
    checks["text"] = ""
    view.after_cancel(timer_action)
    timer_cont = False
def tick():
    global timer, timer_cont
    timer_cont = True
    if timer > 0:
        timer -= 1
        lime.itemconfig(lime_text, text=timer_format(timer))
        if timer == 0:
            checks["text"] += "✅"
        global timer_action
        timer_action = view.after(990, tick)
    else:
        timer_cont = False


# Window
view = tkinter.Tk()
view.title("Timer")
view.config(padx=100, pady=70, bg=YELORANGE)

# Title
title_label = tkinter.Label(text="Timer", fg=SILVER, bg=YELORANGE, font=(FONT_NAME, 30, "bold"))
title_label.grid(row=0, column=1)
checks = tkinter.Label(text="", fg="lime", bg=YELORANGE, font=(FONT_NAME, 12, "bold"))
checks.grid(row=3, column=1)

# Buttons
start_button = tkinter.Button(text="Start", bg=VIOLET, fg="white", width=10, height=2, command=start_timer)
start_button.grid(row=2, column=0)
reset_button = tkinter.Button(text="Reset", bg=VIOLET, fg="white", width=10, height=2, command=reset_timer)
reset_button.grid(row=2, column=2)

# Input
time_input = tkinter.Entry(width=12, bg=SILVER, fg="white")
time_input.grid(row=2, column=1)

# Canvas
lime = tkinter.Canvas(width=198, height=206, bg=YELORANGE, highlightthickness=0)
lime_image = tkinter.PhotoImage(file="dayProjects/week4/timerproject/lime.png")
lime.create_image(100, 103, anchor=tkinter.CENTER, image=lime_image)
lime_text = lime.create_text(99, 103, text="00:00", fill=YELLOW, anchor=tkinter.CENTER, font=(FONT_NAME, 32, "bold"), )
lime.grid(row=1, column=1)

tkinter.mainloop()