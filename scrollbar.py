from tkinter import (
    Tk, RIGHT, Y, Scrollbar, Listbox, END, BOTH, LEFT
)

layar=Tk()
layar.title("Scrollbar")

myScrollbar = Scrollbar(master=layar)
#myScrollbar.pack(side=RIGHT, fill=Y)
#myScrollbar.pack(side=LEFT, fill=Y)

myList = Listbox(master=layar,
                #height=5,
                yscrollcommand=myScrollbar.set)
for line in range(100):
    myList.insert(END, "This is line number " + str(line))

#myList.pack(side=LEFT,fill=BOTH)
myList.pack(side=LEFT,fill=Y)
myScrollbar.pack(side=LEFT, fill=Y)
myScrollbar.config(command=myList.yview)

layar.mainloop()
