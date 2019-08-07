from tkinter import *

# https://www.youtube.com/watch?v=-nmzq3xiZ6I&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d&index=4

root = Tk()

lb1 = Label(root, text="Nama")
lb2 = Label(root, text="Password")

entry1 = Entry(root)
entry2 = Entry(root)

lb1.grid(row=0) # column is 0 by default
#lb1.grid(row=0, sticky=W) # column is 0 by default
lb2.grid(row=1) # column is 0 by default
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

lb1.grid_configure(sticky = W) # sticky should be W E N S

cb = Checkbutton(root, text="Keep me logging in to this site")
cb.grid(columnspan=2) # merge 2 columnn

root.mainloop()
