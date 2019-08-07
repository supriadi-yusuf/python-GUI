import tkinter

layar = tkinter.Tk()
layar.title("entry")
layar.geometry("300x100") # width X height

lb = tkinter.Label(master=layar, text="User Name : ")
lb.pack(side=tkinter.LEFT)

username_var = tkinter.StringVar()
entri_username = tkinter.Entry(master=layar, textvariable=username_var, bd=5)
entri_username.pack(side=tkinter.RIGHT)

username_var.set('supriadi')

layar.mainloop()
