from tkinter import *

root = Tk()

def callback(event):
	print('Position: ', repr(event.char))

frame = Frame(root, width = 200, height = 200)
frame.bind('<Key>', callback)
frame.focus_set()
frame.pack()

mainloop()