from tkinter import (
    Tk, Label, Entry, Button, StringVar
)

from tkinter.messagebox import showerror

def tambah():
    #ent3TextVar.set("hasil")
    try:
        val1 = int(ent1.get())
        val2 = int(ent2.get())
        vl3 = val1 + val2
        ent3TextVar.set(vl3)
    except Exception:
        showerror("error", "input error!")
    #else:
    #    pass

layar = Tk()

lbl1 = Label(master=layar, text="Physics")
lbl1.place( x=10, y=10)

ent1 = Entry(master=layar, bd=5)
ent1.place( x=60, y=10)

lbl2 = Label(master=layar, text="Math")
lbl2.place( x=10, y=50)

ent2 = Entry(master=layar, bd=5)
ent2.place( x=60, y=50)

lbl3 = Label(master=layar, text="Total")
lbl3.place(x=10, y=150)

ent3TextVar = StringVar()

ent3 = Entry(master=layar, bd=5, textvariable=ent3TextVar)
ent3.place(x=60, y=150)

bt1 = Button(master=layar, text="Add", command=tambah)
bt1.place(x=100, y=100)

#width x height + x-offset + y-offset
layar.geometry("250x250+10+10")

layar.mainloop()
