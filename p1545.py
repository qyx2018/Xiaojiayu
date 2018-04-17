from tkinter import *

OPTIONS = [
	'California',
	'345',
	'FF',
	'ENZO',
	'Laferrari'
	]

root = Tk()

variable = StringVar()
variable.set(OPTIONS[0])

w = OptionMenu(root, variable, *OPTIONS)
w.pack()

def callback():
	print(variable.get())

Button(root, text = 'Click', command = callback).pack()

mainloop()