from tkinter import *

window = Tk()
window.title("Miles to km Converter")
window.minsize(300, 100)
window.config(padx=90, pady=20)


def calc():
    user_miles = miles_input.get()
    km = round(int(user_miles) * 1.609, 3)
    result_label["text"] = km


miles_input = Entry(width=10)
miles_input.grid(column=1, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=1)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=2)

result_label = Label(text="0")
result_label.grid(column=1, row=2)

km_label = Label(text="Km")
km_label.grid(column=2, row=2)

calc_button = Button(text="Calculate", command=calc)
calc_button.grid(column=1, row=3)

window.mainloop()