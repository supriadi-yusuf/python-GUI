"""
this tutorial is based on https://tkdocs.com/tutorial/windows.html
"""

import tkinter

def doWindow():
    global myWindow

    if myWindow is None:
        myWindow = tkinter.Toplevel(layar)
        myWindow.title("My Window")
        myInfo.set("Destroy Window")
    else:
        myWindow.destroy() # every element ( Button, Label, etc) also has this method
        myWindow = None
        myInfo.set("Create Window")

layar = tkinter.Tk()
layar.title("Window")
layar.geometry("200x200")

myInfo = tkinter.StringVar()
button = tkinter.Button( layar, textvariable=myInfo, command=doWindow)
button.place(x=50,y=50)

myInfo.set("Create Window")

myWindow = None

layar.mainloop()
