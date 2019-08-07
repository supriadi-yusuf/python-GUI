import tkinter

layar = tkinter.Tk()
layar.title('canvas')

canvas = tkinter.Canvas( master=layar, bg='blue', height=250, width=300)

coord = 10, 50, 240, 210 #tuple
arc = canvas.create_arc( coord, start=0, extent=150, fill='red')
line = canvas.create_line( 10, 10, 200, 200, fill='white')

canvas.pack()

layar.mainloop()
