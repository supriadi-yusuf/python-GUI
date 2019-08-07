from tkinter import (
    Tk, Button, FLAT, RAISED, SUNKEN, GROOVE, RIDGE
)

layar = Tk()
layar.title("relief")

Button(master=layar, text="FLAT", relief=FLAT).pack()
Button(master=layar, text="RAISED", relief=RAISED).pack()
Button(master=layar, text="GROOVE", relief=GROOVE).pack()
Button(master=layar, text="SUNKEN", relief=SUNKEN).pack()
Button(master=layar, text="RIDGE", relief=RIDGE).pack()

layar.mainloop()
