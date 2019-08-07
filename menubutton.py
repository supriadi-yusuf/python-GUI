from tkinter import (
    Tk, Menubutton, RAISED, Menu, IntVar
)

layar = Tk()
layar.title("Menu Button")
layar.geometry("300x100")

mb = Menubutton( master=layar, text="condiment", relief=RAISED)
mb.grid()
mb.menu = Menu( master=mb, tearoff=0)

mb["menu"] = mb.menu

mayoVar = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton(label="mayo", variable=mayoVar)
mb.menu.add_checkbutton(label="ketch", variable=ketchVar)

mb.pack()

layar.mainloop()
