from tkinter import (
    PanedWindow, mainloop, BOTH, Entry, VERTICAL, Scale, Button, HORIZONTAL
)

pw1 = PanedWindow()
pw1.pack(fill=BOTH, expand=1)

ent1 = Entry(master=pw1, bd=5)
pw1.add(ent1)

pw2 = PanedWindow(master=pw1, orient=VERTICAL)
pw1.add(pw2)

sc1 = Scale(master=pw2, orient=HORIZONTAL)
pw2.add(sc1)

bt1 = Button(master=pw2, text="OK")
pw2.add(bt1)

mainloop()
