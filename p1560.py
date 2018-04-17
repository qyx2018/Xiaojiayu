from tkinter import *

root = Tk()

def callback():
	print('Shot')
	
	
photo = PhotoImage(file = '20161024144619_FLXfK.gif')
Label(root, image = photo).pack()
Button(root, text = 'Click', command = callback).place(relx = 0.5, rely = 0.5, anchor = CENTER)

mainloop()