from tkinter import *

root = Tk()

def callback():
	print('Was used.')
	
menubar = Menu(root)
openVar = IntVar()
saveVar = IntVar()
exitVar = IntVar()

filemenu = Menu(menubar, tearoff = True)
filemenu.add_checkbutton(label = 'Open', command = callback, variable = openVar)
filemenu.add_checkbutton(label = 'Save', command = callback, variable = saveVar)
filemenu.add_separator()
filemenu.add_checkbutton(label = 'Quit', command = root.quit, variable = exitVar)
menubar.add_cascade(label = 'File', menu = filemenu)

editVar = IntVar()
editVar.set(1)

editmenu = Menu(menubar, tearoff = True)
editmenu.add_radiobutton(label = '剪切', command = callback, variable = editVar, value = 1)
editmenu.add_radiobutton(label = '拷贝', command = callback, variable = editVar, value = 2)
editmenu.add_radiobutton(label = '粘贴', command = callback, variable = editVar, value = 3)

menubar.add_cascade(label = '编辑', menu = editmenu)

root.config(menu = menubar)

mainloop()