from tkinter import *
from tkinter.ttk import Progressbar
from threading import Thread
import time
import sys

root = Tk()
root.title("Progress Bar")
root.geometry("500x200")
root.resizable(width=False, height=False)

s_info = StringVar()
l_info = Label(root, textvariable=s_info)
l_info.pack()

p_bar = Progressbar(root, orient=HORIZONTAL, length=400, mode="determinate")
p_bar.pack()

#Button(master=root, text="Quit", command = root.destroy).pack(pady=30)

def my_progress(master, max=100):
    p_bar['maximum'] = max
    p_bar['value'] = 0

    for i in range(1,max+1):
        p_bar['value']=i
        s_info.set("connecting to server : {} %".format(i))
        time.sleep(0.1)

    #master.destroy()

def tutup_window(window):
    if p_bar['value'] == 100:
        window.destroy()
    else:
        window.after(100, lambda : tutup_window(window))

t = Thread(target=my_progress, args=(root, 100))
t.start()

root.after(100, lambda : tutup_window(root))

root.mainloop()
