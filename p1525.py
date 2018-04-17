from tkinter import *

root = Tk()

text = Text(root, width = 20, height = 5)
text.pack()
text.insert(INSERT, 'I love FIshC.com')

def show():
	print('AABBCC.')
	
b1 = Button(text, text = 'Click', command = show)
text.window_create(INSERT, window = b1)

mainloop()