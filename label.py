import tkinter

layar = tkinter.Tk()
layar.title('Label')
layar.geometry("200x200")

var = tkinter.StringVar()

label = tkinter.Label( master=layar, textvariable=var, relief=tkinter.RAISED)

var.set("Hi, how are you?")

label.pack()

layar.mainloop()
