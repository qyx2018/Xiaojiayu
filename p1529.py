from tkinter import *
import hashlib

root = Tk()
text = Text(root, width = 30, height = 5)
text.pack()
text.insert(INSERT, 'I love fishc.com!')
contents = text.get(1.0, END)

def getSig(contents):
	m = hashlib.md5(contents.encode())
	return m.digest()
	
sig = getSig(contents)

def check():
	contents = text.get(1.0, END)
	if sig != getSig(contents):
		print('Has been changed.')
	else:
		print('Didn\'t change.')
		
Button(root, text = 'Check', command = check).pack()

mainloop()