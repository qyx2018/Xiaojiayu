from tkinter import *

root = Tk()

frame = Frame(root)
frame.pack(padx = 10, pady = 10)
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()

def test(content):
	if content.isdigit():
		return True
	else:
		return False
		

testCMD = root.register(test)
e1 = Entry(frame, textvariable = v1, width = 10, validate = 'key', validatecommand = (testCMD, '%P'))
e1.grid(row = 0, column = 0)
Label(frame, text = '+').grid(row = 0, column = 1)

e2 = Entry(frame, textvariable = v2, width = 10, validate = 'key', validatecommand = (testCMD, '%P'))
e2.grid(row = 0, column = 2)
Label(frame, text = '+').grid(row = 0, column = 3)

e3 = Entry(frame, textvariable = v3, width = 10, validate = 'key', validatecommand = (testCMD, '%P'))
e3.grid(row = 0, column = 4)

def calc():
	result = int(v1.get()) + int(v2.get())
	v3.set(result)
	
#def clear1():
#	e1.delete(0, END)
#	e2.delete(0, END)
#	e3.delete(0, END)
	
Button(frame, text = 'Result', command = calc).grid(row = 1, column = 2, pady = 5)
#Button(frame, text = 'Clear', command = clear1).grid(row = 1, column =1, pady = 5)
mainloop()