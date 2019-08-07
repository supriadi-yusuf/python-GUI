from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Drop down list")

fr1 = Frame(root, bg="blue", width=200)
fr1.pack(side=LEFT, fill=Y)

fr2 = Frame(root, bg="red")
fr2.pack(fill=BOTH, expand=1)

#fr = LabelFrame(root, text="User", bg="red", width=300, height=300)
#fr.pack(side=TOP, fill=X)

pilihan = ("supriadi", "m. najib", "tuan ma", "kancil")
selected = StringVar()
#selected.set(pilihan[0])
OptionMenu(fr2, selected, *pilihan).pack(side=TOP, fill=X)

root.mainloop()
