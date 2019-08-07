import tkinter
from tkinter.messagebox import showinfo

def list1selection():
    showinfo("List1-selected", list1.curselection())

def list2selection():
    showinfo("List2-selected", list2.curselection())

layar = tkinter.Tk()
layar.title("listbox")

# list 1
list1 = tkinter.Listbox( master=layar, selectmode=tkinter.SINGLE,
    exportselection=0) # exportselection=0 means allowing us to select item at one
                    # listbox without clearing selected item in other listbox

list1.insert( 1, "Python")
list1.insert( 2, "Perl") # we can also type list1.insert( 1, "Perl")
list1.insert( 3, "C")
list1.insert( 4, "PHP")
list1.insert( 5, "JSP")
list1.insert( 6, "Ruby")

list1.select_set(1) #select 2nd item

list1.pack(side =tkinter.TOP)

# list 2
list2 = tkinter.Listbox(master=layar, selectmode=tkinter.MULTIPLE)

list2.insert( 1, "Python")
list2.insert( 2, "Perl") # we can also type list1.insert( 1, "Perl")
list2.insert( 3, "C")
list2.insert( 4, "PHP")
list2.insert( 5, "JSP")
list2.insert( 6, "Ruby")

list2.pack(side =tkinter.BOTTOM)

list2.select_set(2) #select third item
list2.select_set(4) #select fifth item

tkinter.Button(master=layar,text="listbox1",command=list1selection).pack()
tkinter.Button(master=layar,text="listbox2",command=list2selection).pack()

layar.mainloop()
