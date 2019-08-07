# https://www.youtube.com/watch?v=RTM9tiV_HoY&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d&index=2
from tkinter import *

root = Tk()

topFrame = Frame(root)
bottomFrame = Frame(root)

topFrame.pack()
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="Button 4", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack()

root.mainloop()
