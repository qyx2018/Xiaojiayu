from tkinter import *

root = Tk()

def create():
	top = Toplevel()
	top.title('Fishc.com')
	msg = Message(top, text = 'I love Fishc.com!')
	msg.pack()
	
Button(root, text = 'Create top level', command = create).pack()

mainloop()