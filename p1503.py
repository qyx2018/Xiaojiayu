from tkinter import *

root = Tk()
textLabel = Label(root, text = 'Testing')
textLabel.pack(side = LEFT)
photo = PhotoImage(file = '20161024144619_FLXfK.gif')
imgLabel = Label(root, image = photo)
imgLabel.pack(side = RIGHT)

mainloop()