from tkinter import *

root = Tk()

def callback():
	print('was used.')
	
mb = Menubutton(root, text = 'Click', relief = RAISED)
mb.pack()

filemenu = Menu(mb, tearoff = False)

filemenu.add_checkbutton(label = 'Open', command = callback, selectcolor = 'yellow')
filemenu.add_checkbutton(label = 'save', command = callback)

filemenu.add_separator()
filemenu.add_command(label = 'quit', command = root.quit)

mb.config(menu = filemenu)

mainloop()