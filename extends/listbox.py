#http://effbot.org/tkinterbook/listbox.htm#listbox.Listbox.config-method

from tkinter import *

root = Tk()

item_cfg_1 = {"bg":"black", "fg":"white", "selectbackground":"red", "selectforeground":"purple"}
item_cfg_2 = {"bg":"yellow", "fg":"blue"}
item_cfg_3 = {"bg":"green", "fg":"black"}

listbox = Listbox(root, height=10, width=10, **item_cfg_1)

for item in ("item 1","item 2","item 3","item 4","item 5","item 6"):
    listbox.insert(END, item)

listbox.pack(fill=BOTH, expand=1)

listbox.selection_set(2)
listbox.itemconfig(0, **item_cfg_2)
listbox.itemconfig(1, **item_cfg_3)

listbox.bind("<Double-Button-1>", lambda event : print(listbox.nearest(event.y)))
listbox.bind("<Key>", lambda event : print(event.keycode))

print(listbox.get(0,END))
print(listbox.size())
print(listbox.curselection())

listbox.focus_set()

root.mainloop()
