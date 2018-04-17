from tkinter import *

root = Tk()

text = Text(root, width = 30, height = 5, undo = True)
text.pack()
text.insert(INSERT, 'I love fishc.com')

def show():
	text.edit_undo()
	
def back():
	text.edit_redo()
	
Button(root, text = '撤销', command = show).pack()
Button(root, text = '恢复', command = back).pack()

mainloop()