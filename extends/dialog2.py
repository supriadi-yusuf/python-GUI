from tkinter import *

class MyDialog:

    def __init__(self, parent):

        top = self.top = Toplevel(parent)
        top.title("Dialog")

        Label(top, text="Value").pack()

        self.e = Entry(top)
        self.e.pack(padx=5)

        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

        top.grab_set()

    def ok(self):

        print("value is {}".format(self.e.get()))

        self.top.grab_release()
        self.top.destroy()

    def __del__(self):
        print("{} is deleted ..".format(self.__class__.__name__))


def showDialog():
    d = MyDialog(root)
    root.wait_window(d.top)


root = Tk()
root.title("main window")
root.geometry("400x400")

Button(root, text="Hello!", command=showDialog).pack()
root.update()

root.mainloop()
