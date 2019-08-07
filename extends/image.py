from tkinter import *

root = Tk()

photo = PhotoImage(file="supri.gif")

lb = Label( master=root, image=photo)
lb.pack()

root.mainloop()
