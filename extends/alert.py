"""
this tutorial is based on https://tkdocs.com/tutorial/windows.html
"""

import tkinter
import tkinter.messagebox as mymessage

def doMessage():
    myAnswer = mymessage.askyesno( message="Are you Supriadi?",
     icon="question", title="confirmation" )
    print(myAnswer)

layar = tkinter.Tk()
layar.title("Window")
layar.geometry("200x200")

button = tkinter.Button( layar, text="my message", command=doMessage)
button.place(x=50,y=50)

layar.mainloop()
