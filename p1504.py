from tkinter import *

root = Tk()
photo = PhotoImage(file = '20161024144619_FLXfK.gif')
textLabel = Label(root, 
				  text = 'If you want to learn Python\n to Fishc',
				  justify = LEFT,
				  image = photo,
				  compound = CENTER,
				  font = ('华康少女字体', 20),
				  fg = 'black'
				  )
textLabel.pack()

mainloop()