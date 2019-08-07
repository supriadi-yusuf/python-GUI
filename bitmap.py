from tkinter import (
    Tk, Button, RAISED
)

layar = Tk()
layar.title("Bitmap")

Button(master=layar, text="error", relief=RAISED, bitmap="error").pack()
Button(master=layar, text="hourglass", relief=RAISED, bitmap="hourglass").pack()
Button(master=layar, text="info", relief=RAISED, bitmap="info").pack()
Button(master=layar, text="question", relief=RAISED, bitmap="question").pack()
Button(master=layar, text="warning", relief=RAISED, bitmap="warning").pack()

layar.mainloop()
