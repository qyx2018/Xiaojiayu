from tkinter import *

root = Tk()

def callback():
	fileName = colorchooser.askcolor()
	print(fileName)
	
Button(root, text = 'Choose color', command = callback).pack()

mainloop()