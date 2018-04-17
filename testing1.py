from tkinter import *

root = Tk()
text = Text(root, width = 30, height = 5)
text.pack()
text.insert(INSERT, 'I love fishc.com!')

def getIndex(text, index):
	print(text.index)
#	print(str.split(text.index(index)))
	return tuple(map(int, str.split(text.index(index), '.')))

start = 1.0
count = 1

while True:
	pos = text.search('o', start, stopindex = END)
#	print(pos, count)
	if not pos:
		break
	print('Find, pos is: ', getIndex(text, pos))
	start = pos + '+1c'
	count += 1
	
mainloop()