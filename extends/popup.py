from tkinter import *

root = Tk()
root.title("Pop Up Demo")
root.geometry("500x500")

popup = Menu(root, tearoff=0)
popup.add_command(label="Next")
popup.add_command(label="Previous")
popup.add_separator()
popup.add_command(label="Home")

#root.bind("<Button-3>", lambda event : popup.post(event.x_root, event.y_root))

def do_popup(event):
    try:
        #popup.tk_popup(event.x_root, event.y_root, 0)
        popup.post(event.x_root, event.y_root)
    finally:
        popup.grab_release()

root.bind("<Button-3>", do_popup)
root.bind("<Button-1>", lambda e : popup.unpost())

mainloop()
