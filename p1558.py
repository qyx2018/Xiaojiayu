from tkinter import *

root = Tk()

Label(root, text = 'User').grid(row = 0, sticky = W)
Label(root, text = 'Password').grid(row = 1, sticky = W)

Entry(root).grid(row = 0, column = 1)
Entry(root, show = '*').grid(row = 1, column = 1)
photo = PhotoImage(file = '20161024144619_FLXfK.gif')
Label(root, image = photo).grid(row = 0, column = 2, rowspan = 2, padx = 5, pady= 5)

Button(text = 'Sub', width = 10).grid(row = 2, columnspan = 3, pady = 5)

mainloop()