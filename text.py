from tkinter import (
    Tk, Text, INSERT, END
)

from tkinter.messagebox import showinfo

layar = Tk()
layar.title("Text")

text = Text(master=layar)
text.insert( INSERT, "Hello......")
text.insert( END, "Bye Bye......")
text.pack()

text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")

text.tag_config("here", background="yellow", foreground="blue")
text.tag_config("start", background="black", foreground="green")

showinfo("isi text", text.get("1.0", END))

layar.mainloop()
