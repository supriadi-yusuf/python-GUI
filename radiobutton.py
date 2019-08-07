from tkinter import (
    Tk, IntVar, Label, Radiobutton, W
)

def sel():
    selection = "You select the Option " + str(selectVar.get())
    label.config(text=selection)

layar=Tk()
layar.title("Radio Button")

selectVar = IntVar()

R1 = Radiobutton(master=layar, text="Option 1", variable=selectVar, value=1, command=sel)
R1.pack(anchor=W)

R2 = Radiobutton(master=layar, text="Option 2", variable=selectVar, value=2, command=sel)
R2.pack(anchor=W)

R3 = Radiobutton(master=layar, text="Option 3", variable=selectVar, value=3, command=sel)
R3.pack(anchor=W)

label = Label(master=layar)
label.pack()

R1.select()

layar.mainloop()
