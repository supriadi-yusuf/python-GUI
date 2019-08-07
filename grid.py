from tkinter import (
    Tk, Button
)

layar = Tk()
layar.title("Grid")

b=0
for r in range(6):
    for c in range(6):
        b += 1
        if b < 10 :
            Button(master=layar,
                        #bd=1,
                        borderwidth=1,
                        text=str(b)
                        ).grid( row=r, column=c, ipadx=4)
        else :
            Button(master=layar,
                        #bd=1,
                        borderwidth=1,
                        text=str(b)
                        ).grid( row=r, column=c)

layar.mainloop()
