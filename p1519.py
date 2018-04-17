from tkinter import *

root = Tk()

theLB = Listbox(root, setgrid = True)
theLB.pack()
for item in range(11):
	theLB.insert(END, item)
	
mainloop()