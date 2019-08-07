from tkinter import (
    Tk, Button, RAISED
)

layar = Tk()
layar.title("Cursor")

Button(master=layar, text="circle", relief=RAISED, cursor="circle").pack()
Button(master=layar, text="plus", relief=RAISED, cursor="plus").pack()

#layar.config(cursor="watch")

layar.mainloop()
