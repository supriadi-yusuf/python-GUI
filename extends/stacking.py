import tkinter

layar = tkinter.Tk()
layar.title("window utama")
layar.geometry('400x400')

lb1 = tkinter.Label(master=layar,text='contoh', relief='raised')
lb1.grid(column=0,row=0)

lb2 = tkinter.Label(master=layar,text='selamat malam', relief='raised')
lb2.grid(column=0,row=0)

layar.after(5000,lambda:lb1.lift())

layar.mainloop()
