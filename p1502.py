import tkinter as tk

class App:
	def __init__(self, root):
		frame = tk.Frame(root)
		frame.pack()
		self.hi_there = tk.Button(frame, text = "打招呼", bg = 'black', fg = 'white', command = self.say_hi)
		self.hi_there.pack(side = tk.LEFT)
		
	def say_hi(self):
		print('你好，测试中...')

root = tk.Tk()
root.title('Fishc.com')
app = App(root)

root.mainloop()