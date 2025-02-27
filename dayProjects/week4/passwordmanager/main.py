import tkinter
import random
import tkinter.messagebox
import pyperclip
import json

# Constants
LPINK = "#f0c5c9"
RPINK = "#fa9090"
RED = "#aa3e39"
GREY = "#444444"
CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01236789!@#$%^&*-_+?"
DATA_PATH = "dayProjects/week4/passwordmanager/userinfo.json"

# Functions
def add_info():
        if web_input.get() != "" and name_input.get() != "" and pass_input.get() != "":
            new_data = {web_input.get():{"name": name_input.get(),"pass": pass_input.get()}}
            try:
                with open(file=DATA_PATH, mode="r") as datafile:
                    cur_data = json.load(datafile)
                    cur_data.update(new_data)
                with open(file=DATA_PATH, mode="w") as datafile:
                    json.dump(cur_data, datafile, indent=4)
                    web_input.delete(0, len(web_input.get()) + 1)
                    pass_input.delete(0, len(pass_input.get()) + 1)
            except FileNotFoundError:
                with open(file=DATA_PATH, mode="w") as datafile:
                    json.dump(new_data, datafile, indent=4)
            except json.JSONDecodeError:
                with open(file=DATA_PATH, mode="w") as datafile:
                    json.dump(new_data, datafile, indent=4)
        else:
            tkinter.messagebox.showwarning("Missing fields", "You have missing fields.\nPlease fill out all fields.")
            after_ex = None
            def revert_button():
                pass_add_button["text"] = "Add Info"
                after_ex = False
            revert_button()
            if after_ex == True:
                view.after_cancel(reversion)
            pass_add_button["text"] = "Fields Required"
            after_ex = True
            reversion = view.after(500, revert_button)

def generate_pass():
    new_pass = ""
    for _ in range(random.randint(12, 15)):
        new_pass += CHARS[random.randint(0, len(CHARS) - 1)]
    pass_input.delete(0, len(pass_input.get()) + 1)
    pass_input.insert(0, new_pass)
    pyperclip.copy(pass_input.get())

def search_data():
    try:
        userdata = open(file=DATA_PATH)
        file_get = json.load(userdata)
    except FileNotFoundError:
        tkinter.messagebox.showerror("No File", "We could not find the data file.")
    else:
        web = web_input.get()
        if web != "":
            if web in file_get:
                user_name = file_get[web]["name"]
                user_pass = file_get[web]["pass"]
                tkinter.messagebox.showinfo(f"User Info: {web}", f"The data for {web}:\nUsername/Email: {user_name}\nPassword: {user_pass}")
            else:
                tkinter.messagebox.showerror("Data Missing", "We could not find the data required for the request: " + web_input.get() + "\nDetails may not exist for " + web_input.get())
        else:
            tkinter.messagebox.showerror("Required Parameter", "Please input a site.")
        userdata.close()

# Window
view = tkinter.Tk()
view.title("Password Manager")
view.config(padx=40, pady=60, background=LPINK)

# Labels
label = tkinter.Label
web_label = label(text="Website:", font=("Sans Serif", 14, "bold"), fg=GREY, bg=LPINK)
web_label.grid(row=1, column=0)
name_label = label(text="Username/Email:", font=("Sans Serif", 14, "bold"), fg=GREY, bg=LPINK)
name_label.grid(row=2, column=0)
pass_label = label(text="Password:", font=("Sans Serif", 14, "bold"), fg=GREY, bg=LPINK)
pass_label.grid(row=3, column=0)

# Buttons
pass_gen_button = tkinter.Button(bg=RED, fg=LPINK, activebackground=GREY, activeforeground=RPINK, width=7, text="Generate", font=("Sans Serif", 8, "bold"), command=generate_pass)
pass_gen_button.grid(row=3, column=2)
pass_gen_button = tkinter.Button(bg=RED, fg=LPINK, activebackground=GREY, activeforeground=RPINK, width=7, text="Search", font=("Sans Serif", 8, "bold"), command=search_data)
pass_gen_button.grid(row=1, column=2)
pass_add_button = tkinter.Button(bg=RED, fg=LPINK, activebackground=GREY, activeforeground=RPINK, width=39, text="Add Info", font=("Sans Serif", 8, "bold"), command=add_info)
pass_add_button.grid(row=4, column=1, columnspan=2)

# Inputs
input = tkinter.Entry
web_input = input(bg=RPINK, font=("Sans Serif", 14, "bold"))
web_input.grid(row=1, column=1)
name_input = input(bg=RPINK, font=("Sans Serif", 14, "bold"), width=26)
name_input.grid(row=2, column=1, columnspan=2)
pass_input = input(bg=RPINK, font=("Sans Serif", 14, "bold"))
pass_input.grid(row=3, column=1)

# Canvas
logo = tkinter.Canvas(width=200, height=200, bg=LPINK, highlightthickness=0)
logo_image = tkinter.PhotoImage(file="dayProjects\week4\passwordmanager\logo.png")
logo.create_image(100, 100, anchor=tkinter.CENTER, image=logo_image)
logo.grid(row=0, column=1)

tkinter.mainloop()