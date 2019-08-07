import tkinter
# state normal, withdrawn

lyr = tkinter.Tk()
lyr2 = tkinter.Toplevel(master=lyr)

lyr.geometry("400x400")
lyr2.geometry("400x400")

lyr.title("main")
lyr2.title('child')

bt = tkinter.Button(master=lyr, text="hide", command=lambda : lyr.state("withdrawn"))
bt2 = tkinter.Button(master=lyr2, text="show", command=lambda : lyr.state("normal"))

bt.pack()
bt2.pack()

lyr.mainloop()
