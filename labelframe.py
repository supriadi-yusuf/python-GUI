from tkinter import (
    Tk, LabelFrame, BOTH, YES, Label
)

layar = Tk()
layar.title("LabelFrame")

lbfr = LabelFrame(master=layar, text="This is a label frame")
lbfr.pack(fill=BOTH, expand=YES)

lb = Label(master=lbfr, text="Inside the Labelframe")
lb.pack()

layar.mainloop()
