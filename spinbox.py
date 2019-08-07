from tkinter import (
    Tk, Spinbox, StringVar
)

from tkinter.messagebox import showinfo

layar = Tk()
layar.title("Spinbox")

sp1var = StringVar()
sp1 = Spinbox( master=layar,
               from_=1,
               to=12,
               increment=2,
               textvariable=sp1var)
sp1.pack()
sp1var.set(4)

listwarna = ["merah", "kuning", "hijau", "biru", "orange"]
sp2var = StringVar()
sp2 = Spinbox(  master=layar,
                value=listwarna,
                textvariable=sp2var)
sp2.pack()
sp2var.set(listwarna[2])

showinfo("spinbox1", sp1.get())

layar.mainloop()
