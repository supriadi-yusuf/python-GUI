"""
this tutorial is based on https://tkdocs.com/tutorial/windows.html
"""

import tkinter
from tkinter import filedialog

def openFile():
    filename = filedialog.askopenfilename(title="pilih file", parent=layar,
        filetypes=( ( "python", ".py"), ( "text file", ".txt")),
        multiple=True,
        initialdir="/home/supriadi/latihan/python",
        initialfile="readme.txt")
    print(filename)

def saveAsFile():
    filename = filedialog.asksaveasfilename(title="simpan file", parent=layar,
        filetypes=( ( "python", ".py"), ( "text file", ".txt")),
        #multiple=True,
        defaultextension="txt",
        confirmoverwrite=True,
        initialdir="/home/supriadi/latihan/python",
        initialfile="readme.txt")
    print(filename)

def openDir():
    dirname = filedialog.askdirectory(title="pilih direktori", parent=layar,
        #filetypes=( ( "python", ".py"), ( "text file", ".txt")),
        #multiple=True,
        #defaultextension="txt",
        #confirmoverwrite=True,
        initialdir="/home/supriadi/latihan/python")

    print(dirname)

if __name__ == "__main__":
    layar = tkinter.Tk()
    layar.title("Window")
    layar.geometry("200x200")


    button = tkinter.Button( layar, text="open file", width="10", command=openFile)
    button.place(x=50,y=50)

    button2 = tkinter.Button( layar, text="save as file", width="10", command=saveAsFile)
    button2.place(x=50,y=80)

    button3 = tkinter.Button( layar, text="open directory", width="10", command=openDir)
    button3.place(x=50,y=110)


    layar.mainloop()
