import tkinter
import tkinter.messagebox

layar = tkinter.Tk()
layar.title("button")
layar.geometry("200x200")

def helloCallback():
    msg=tkinter.messagebox.showinfo( "Hello Python", "Hello World")

button = tkinter.Button( layar, text="my button", command=helloCallback)
button.place(x=50,y=50)

layar.mainloop()
