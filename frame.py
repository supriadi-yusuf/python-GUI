import tkinter

layar=tkinter.Tk()
layar.title("frame")

frame = tkinter.Frame(master=layar)
frame.pack()

bottomframe = tkinter.Frame(master=layar)
bottomframe.pack(side=tkinter.BOTTOM)

redbutton = tkinter.Button( master=frame, text="Red", fg="red")
redbutton.pack(side=tkinter.LEFT)

greenbutton = tkinter.Button( master=frame, text="Green", fg="green")
greenbutton.pack(side=tkinter.LEFT)

bluebutton = tkinter.Button( master=frame, text="Blue", fg="blue")
bluebutton.pack(side=tkinter.LEFT)

blackbutton = tkinter.Button( master=bottomframe, text="Black", fg="black")
blackbutton.pack(side=tkinter.BOTTOM)

layar.mainloop()
