from tkinter import (
    Tk, Button, Menu, Toplevel
)

def donothing():
    filewin = Toplevel(layar)
    button = Button(master=filewin, text="Do Nothing Button", command=filewin.destroy)
    button.pack()

layar = Tk()
layar.title("Menu")
layar.geometry("300x100")

appmenu = Menu(master=layar)
layar.config(menu=appmenu)

# file menu
filemenu = Menu( master=appmenu, tearoff=0)
appmenu.add_cascade( label="File", menu=filemenu)

filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save As", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=layar.quit)

# edit menu
editmenu = Menu( master=appmenu, tearoff=0)
appmenu.add_cascade( label="Edit", menu=editmenu)

editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

# help menu
helpmenu = Menu( master=appmenu, tearoff=0)
appmenu.add_cascade( label="Help", menu=helpmenu)

helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About ....", command=donothing)

# sub menu /nested menu : kontak menu
kontakmenu = Menu( master=helpmenu, tearoff=0)
helpmenu.add_cascade(label="kontak", menu=kontakmenu)

kontakmenu.add_command(label="personal", command=donothing)
kontakmenu.add_command(label="official", command=donothing)

layar.mainloop()
