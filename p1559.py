from tkinter import *

root = Tk()

def callback():
	print('Shot')
	
Button(root, text = 'Click', command = callback).place(relx = 0.5, rely = 0.5, anchor = CENTER)

mainloop()