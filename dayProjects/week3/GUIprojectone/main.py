import tkinter

view = tkinter.Tk()
view.title("First GUI Project")
view.minsize(width=500, height=300)

# Label
# label1 = tkinter.Label(text="Label 1", font=("Arial", 28, "bold"))
# label1.pack(expand=False) # Puts label on screen, and centers (centers vertically wit hdefault side being top) | expand True makes it center both ways if this part of the items is alone
# label2 = tkinter.Label(text="Label 2", font=("Serif", 28))
# label2.pack(expand=False, side="left") # If also expanding and elements are on the same side, they will center in areas shrunk vertically(top/bottom) or horizontally(right/left)
# The labels are default prioritized growing horzontal/vertical based on the order made,
# even if both expand and the first is top to expand vertically and the second is left to
# expand horizontally, the first will expand vertically all the way, and there won't be
# equal vertical space. If a third label is made, after the first label made expanding
# vertically, to be expanding on the bottom and on left side, the bottom will not be
# expanded vertically but will share the bottom of the screen horizontally and equally.

# Items without expanding will only take as much space as they minimally need, but expanding
# will not expand over the space that other labels would minimally need.

# label3 = tkinter.Label(text="I am red", fg="red", font=("Arial", 16)) # fg changes text color, bg changes text background color, 
# # bg color doesn't expand with expand=True alone
# label3.pack()

# Using labelobject["kwarg"] = ... with kwarg being the kew word argument name, configures that single atribute.
# label3["font"] = ("Arial", 20, "italic")

# Using labelobject.config(kwarg=..., kwarg=...), kwarg being the key word argument name, helps configure many attributes at once.
# label3.config(text="I am blue text with red background", bg="red", fg="blue")

# [ BUTTONS ]

# # Function for the button, reference 1
# def button1_clicked():
#     label4["text"] = "Button was clicked!"

# Buttons are made with tkinter.Button(), however it saves time to declare an easy-to-use keyword 
# for the object if you will use more than one
button = tkinter.Button
label = tkinter.Label
# label4 = label(text="Hello!", font=("Arial", 16))
# label4.pack()
# button1 = button(text="Click me!", command=button1_clicked) # buttons do have the standard text, fg, bg, font, 
# # and they also can use command with a function name in order to activate a function when clicked.
# button1.pack()

# # Getting the button to work may take a function (see reference 1) to operate.

# [ INPUTS ]

# # Function for button, reference 2
# def button2_clicked():
#     label4.config(text=name_input.get(), fg="gray")

# Inputs comes from tkinter.Entry(), and the same shorcut applies if needed
input = tkinter.Entry
# name_input = input(width=12) # there are kwargs such as width to set the desired width of the entry
# name_input.pack()
# label4 = label(text="No name", font=("Arial", 16))
# label4.pack()
# button2 = button(text="Set Name", bg="gray", fg="white", font=("Arial", 16), command=button2_clicked)
# button2.pack()

# The button sets the label to the name_input's value using name_input.get(), which that line in this
# case is set to a string value for the input.

# [ TEXT ]

# Text is a multi-line input, obtained by tkinter.Text()
text = tkinter.Text
# text1 = text(width=4, height=32)
# text1.pack()

# [ SPINBOX ]

# def print_spinbox1_value():
#     print(spinbox1.get())
# spinbox = tkinter.Spinbox
# spinbox1 = spinbox(width=6, from_=0, to=10, command=print_spinbox1_value)
# spinbox1.pack()

# [ SCALE ]

# def print_scale1_value(num):
#     print(num)
# scale = tkinter.Scale
# scale1 = scale(from_=0, to=20, command=print_scale1_value) # This appears to throw in a value to the function, being the value.
# scale1.pack()

# [ CHECKBOX/CHECKBUTTON ]

# # Checkbuttons need a bit more, as they must put their value in a IntVar, which is a tkinter class used as well
# # IntVar still needs to use intvarclass.get() to get the value, checkboxes make it 0 or 1
# def print_checkbox1_state():
#     print(check_state1.get())
# check_state1 = tkinter.IntVar()
# checkbox = tkinter.Checkbutton
# checkbox1 = checkbox(text="On/Off", variable=check_state1, command=print_checkbox1_state)
# checkbox1.pack()

# [ RADIO INPUTS ]

# # Radio inputs are a lot like checkboxes but groups of them are for certain values, which only one can be true.
# def print_radio_state():
#     print(radio_state.get())
# radio_state = tkinter.IntVar()
# radio = tkinter.Radiobutton
# radio1 = radio(text="Option 1", variable=radio_state, value=1, command=print_radio_state)
# radio2 = radio(text="Option 2", variable=radio_state, value=2, command=print_radio_state)
# radio3 = radio(text="Option 3", variable=radio_state, value=3, command=print_radio_state)
# radio1.pack()
# radio2.pack()
# radio3.pack()

# [ LISTBOX ]

# # Listboxes store a list of items
# def print_listbox_value(item):
#     print(listbox1.get(listbox1.curselection())) # Gets the currently selected item
# listbox = tkinter.Listbox
# listbox1 = listbox(height=3) # 'command' kwarg does not work here
# veggies = ["Carrots", "Broccoli", "Radish"]
# for item in veggies:
#     listbox1.insert(0, item)
# listbox1.bind("<<ListboxSelect>>", print_listbox_value) # This is how you use the function by selecting a listbox item, 
# # does send an argument, but it's not the value of what was selected
# listbox1.pack()

view.mainloop()