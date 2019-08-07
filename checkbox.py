import tkinter

layar = tkinter.Tk()
layar.title("checkbox")

CheckVar1 = tkinter.IntVar()
CheckVar2 = tkinter.IntVar()

cb1 = tkinter.Checkbutton( master=layar, text="Music", variable=CheckVar1,
                        onvalue=1, offvalue=0, height=5, width=20)
cb2 = tkinter.Checkbutton( master=layar, text="Music", variable=CheckVar2,
                        onvalue=1, offvalue=0, height=5, width=20)

cb1.pack()
cb2.pack()

#cb2.select() # or
CheckVar2.set(1) # to get value : CheckVar2.get()

layar.mainloop()
