from tkinter import *

window = Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)

# Label
label = Label(text="New Text ", font=("Arial", 24, "bold"))
label.grid(column=0, row=0)
# label["text"] = "hello"
# label.config(text="hello")

# Button
def button_clicked():
    print("I got clicked")
    label["text"] = my_entry.get()
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

# Button number 2
button2 = Button(text="Don't click me")
button2.grid(column=3, row=0)


# Entry
my_entry = Entry(width=10)
my_entry.grid(column=4, row=4)



window.mainloop()
