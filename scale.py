from tkinter import (
    Tk, DoubleVar, Scale, CENTER, Label, Button, HORIZONTAL
)

layar = Tk()
layar.title("Scale")

def show_value():
    selection = "Value = " + str(scaleVar.get())
    label.config(text=selection)


scaleVar = DoubleVar()

scale = Scale( master=layar,
               #showvalue=0, #hide selected value
               #sliderlength=50,
               #orient=HORIZONTAL,
               #length=200,
               #label="prioritas",
               #from_=0,
               #to=1,
               #resolution=0.2,
               #tickinterval=0.2,
               variable=scaleVar)
               
#scale.pack()
scale.pack(anchor=CENTER)

button = Button( master=layar, text="Get Scale Value", command=show_value)
button.pack(anchor=CENTER)

label=Label(master=layar)
label.pack()

layar.mainloop()
