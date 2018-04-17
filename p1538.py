from tkinter import *

root = Tk()
w = Canvas(root, width = 400, height = 200)
w.pack()

def paint(event):
	x1, y1 = (event.X - 1), (event.Y - 1)
	x2, y2 = (event.X + 1), (event.Y + 1)
	w.create_oval(x1, y1, x, y2, fill = 'red')
	
w.bind('<B1 - Motion>', paint)
Label(root, text = '画图...').pack(side = BOTTOM)

mainloop()