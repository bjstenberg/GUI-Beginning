from tkinter import *


def button_clicked():
    print("Got me!")
    new_text = input.get()
    my_label.config(text=new_text)


# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)
# Add padding - this can be used on all widgets - this adds space between the walls, or other widgets
window.config(padx=20, pady=20)


# Labels
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="This is new text")
#my_label.pack(side="left")
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click Me", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)

button2 = Button(text="No, me!", command=button_clicked)
button2.grid(column=2, row=0)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)
# Dont mix GRID and PACK, either or!
#input.pack()




# Alltid i slutet
window.mainloop()