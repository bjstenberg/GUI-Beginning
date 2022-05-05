from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)


miles_input = Entry(width=10)
miles_input.grid(column=2, row=0)


miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=3, row=0)


equal_label = Label(text="is equal to", font=("Arial", 12))
equal_label.grid(column=1, row=1)


result_label = Label(text="0", font=("Arial", 12))
result_label.grid(column=2, row=1)


label_km = Label(text="Km", font=("Arial", 12))
label_km.grid(column=3, row=1)


button = Button(text="Calculate", command=miles_to_km)
button.grid(column=2, row=2)


window.mainloop()