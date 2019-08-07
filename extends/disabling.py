import tkinter

def disableParent():
    if btEnable['state'] == tkinter.DISABLED: # check if btEnable is disabled
        lyr2.grab_set() # make window lyr2 enable and other window disable
        btEnable['state'] = tkinter.NORMAL # set btEnable to NORMAL/enable
        btDisable['state'] = tkinter.DISABLED # set btDisable to disable

def enableParent():
    if btDisable['state'] == tkinter.DISABLED:
        lyr2.grab_release() # make all window enable
        btDisable['state'] = tkinter.NORMAL # set btDisable to NORMAL/enable
        btEnable['state'] = tkinter.DISABLED # set btEnable to disable

lyr = tkinter.Tk()
lyr2 = tkinter.Toplevel(master=lyr)

lyr.title("utama")
lyr2.title("anak")

lyr.geometry("400x400")
lyr2.geometry("400x400")

entVar = tkinter.StringVar()
ent = tkinter.Entry(master=lyr, textvariable=entVar)
ent.pack()

btEnable = tkinter.Button(master=lyr2, state=tkinter.DISABLED, text="enable utama", command=enableParent)
btDisable = tkinter.Button(master=lyr2, text="disable utama", command=disableParent)

btEnable.pack()
btDisable.pack()

lyr.mainloop() 
