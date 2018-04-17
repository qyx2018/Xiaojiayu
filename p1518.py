from tkinter import *

root = Tk()

theLB = Listbox(root, setgrid = True)
theLB.pack()

for item in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']:
	theLB.insert(END, item)

theButton = Button(root, text = 'Delete', command = lambda x = theLB: x.delete(ACTIVE))
theButton.pack()

mainloop()