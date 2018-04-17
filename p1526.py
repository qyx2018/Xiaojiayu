from tkinter import *

root = Tk()

text = Text(root)
#text = Text(root, width = 30, height = 10)

text.pack()
text.insert(INSERT, 'I love Fishc.com')
photo = PhotoImage(file = '20161024144619_FLXfK.gif')

def show():
	text.image_create(END, image = photo)

b1 = Button(text, text = 'Click', command = show)
text.window_create(INSERT, window = b1)

mainloop()