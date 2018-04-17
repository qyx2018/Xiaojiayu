from tkinter import *

root = Tk()
v = IntVar()
c = Checkbutton(root, text = 'Testing', variable = v)
c.pack()
l = Label(root, textvariable = v)
l.pack()

mainloop()