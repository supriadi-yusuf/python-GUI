from tkinter import *

root = Tk()
root.title("fitting")
root.geometry("400x300")

one = Label( root, text="one", bg="red", fg="white")
two = Label( root, text="two", bg="green", fg="black")
three = Label( root, text="three", bg="blue", fg="white")

one.pack()
two.pack(fill=X) # full fill horizontally
three.pack( side=LEFT, fill=Y) # fullfill vertically

root.mainloop()
