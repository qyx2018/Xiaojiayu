from tkinter import *

def callback():
	var.set('I don\'t believe!')
	
root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set('Testing.aaksdjalkdjflajdkldsfklsdfk\naldkjfi9ekdkdkkadk3ljk54')
textLabel = Label(frame1,
				  textvariable = var,
				  fg = 'black',
				  justify = LEFT)
photo = PhotoImage(file = '20161024144619_FLXfK.gif')
imgLabel = Label(frame1, image = photo)
imgLabel.pack(side = RIGHT)
theButton = Button(frame2, text = 'Haha, 18 years old.', command = callback)
theButton.pack()

frame1.pack(padx = 10, pady = 10)
frame2.pack(padx = 10, pady = 10)

mainloop()