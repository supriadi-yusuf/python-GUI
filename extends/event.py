from tkinter import *

def klik_kiri(event):
    print("left button is pressed.")

def klik_tengah(event):
    print("middle button is pressed.")
    #print(dir(event))
    #print(dir(event.widget))
    #print(type(event.widget))

def klik_kanan(event):
    print("right button is pressed.")

root = Tk()

frame = Frame( master=root, width=300, height=250)
frame.pack()

frame.bind('<Button-1>', klik_kiri)
frame.bind('<Button-2>', klik_tengah)
frame.bind('<Button-3>', klik_kanan)

root.bind('<Destroy>', lambda event : print("window is destroyed."))

root.mainloop()
