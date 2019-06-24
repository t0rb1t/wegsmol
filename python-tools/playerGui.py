#!/usr/bin/python3

from playerChar import *

import tkinter as tk

def uno():
	root = tk.Tk()
	level = tk.IntVar()
	def dos():
		stats = statgen(level.get())
		print(stats)

	canvas = tk.Canvas(root, height=700, width=700)
	canvas.pack()

	frame = tk.Frame(root, bg='#21385b')
	frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

	levelScale = tk.Scale(frame, variable = level, from_ = 1, to = 25)
	levelScale.pack()

	nameField = tk.Entry(frame)
	nameField.pack()

	createButton = tk.Button(frame, text="Create Character", command=dos)
	createButton.pack()
	

	root.mainloop()


def sample():
	print("lol")
	return False

uno()