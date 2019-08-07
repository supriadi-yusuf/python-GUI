from tkinter import (
    Tk, Message, RAISED, StringVar, CENTER
)

layar = Tk()
layar.title("Message")
#layar.geometry("250x100")

isi = StringVar()
message = Message(master=layar, relief=RAISED, textvariable=isi, #width=200,
justify=CENTER)
message.pack()

isi.set("Hey! How are you doing?")

layar.mainloop()
