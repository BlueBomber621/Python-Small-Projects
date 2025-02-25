import tkinter

view = tkinter.Tk()
view.title("Miles/Kilometer Converter")
view.minsize(width=150, height=180)
view.config(padx=5, pady=15)

label = tkinter.Label
button = tkinter.Button

# Functions
def set_convert():
    if mkvalue.get() == "Miles":
        input_label["text"] = "Miles"
        output_label["text"] = "Kilometers"
    else:
        input_label["text"] = "Kilometers"
        output_label["text"] = "Miles"
    if number_entry.get() != "":
        do_conversion()

def do_conversion():
    value = float(number_entry.get())
    if mkvalue.get() == "Miles":
        output_amt_label["text"] = str(round((value * 1.609), 4))
    else:
        output_amt_label["text"] = str(round((value / 1.609), 4))

# Labels
input_label = label(text="Miles", font=("Sans Serif", 16))
input_label.grid(column=2, row=1)
output_label = label(text="Kilometers", font=("Sans Serif", 16))
output_label.grid(column=2, row=2)
output_amt_label = label(text="0", font=("Sans Serif", 10, "bold"))
output_amt_label.grid(column=1, row=2)
label1 = label(text="is equal to", font=("Sans Serif", 16))
label1.grid(column=0, row=2)

# Buttons
calculate_button = button(text="Calculate", bg="lime", font=("Sans Serif", 16), command=do_conversion)
calculate_button.grid(column=1, row=3)

# Input
number_entry = tkinter.Entry(width=8, font=("Sans Serif", 14))
number_entry.grid(column=1, row=1)

# Radial
mkvalue = tkinter.StringVar(value="Miles")
miles_radial = tkinter.Radiobutton(text="Miles", variable=mkvalue, value="Miles", font=("Sans Serif", 14), command=set_convert)
miles_radial.grid(column=0, row=0)
kilo_radial = tkinter.Radiobutton(text="Kilometers", variable=mkvalue, value="Kilometers", font=("Sans Serif", 14), command=set_convert)
kilo_radial.grid(column=2, row=0)


tkinter.mainloop()