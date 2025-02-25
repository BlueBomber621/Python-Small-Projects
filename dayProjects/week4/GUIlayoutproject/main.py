import tkinter

view = tkinter.Tk()
view.title("Layout Project")
view.minsize(width=600, height=480)
view.config(pady=180, padx=120)

label = tkinter.Label
button = tkinter.Button
input = tkinter.Entry

# Functions
def set_labels():
    name_label["text"] = color_input.get().title()
    if color_input.get().lower() == "black":
        color_label.config(fg="black", bg="white")
    else:
        color_label.config(fg=color_input.get().lower(), bg="black")

# Labels
title_label = label(text="Color Viewer", font=("Times New Roman", 24))
title_label.grid(column=2, row=0)
title_label.config(pady=15, padx=15)
name_label = label(text="White", font=("Times New Roman", 16))
name_label.grid(column=1, row=1)
color_label = label(text="Your Color", fg="white", bg="black", font=("Times New Roman", 16))
color_label.grid(column=3, row=1)

# Buttons
set_button = button(width=12, height=2, text="Set Color", command=set_labels)
set_button.grid(column=2, row=2)

# Inputs
color_input = input(width=12, bg="gray")
color_input.grid(column=2, row=4)

tkinter.mainloop()