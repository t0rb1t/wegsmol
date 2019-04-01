#!/usr/bin/python3

import enMan as e
import tkinter as tk

enemies = []

def uno():
	funcDict = {'attack':e.attack,
			'report':	e.report,
			'turn':		e.classTurn,
			'save':		e.storeEnemies,
			'fetch':	e.fetchEnemies,
			'weapon':	e.weapon,
			'roll':		e.roll}

	root = tk.Tk()
	level = tk.IntVar()
	
	canvas = tk.Canvas(root, height=700, width=700)
	canvas.grid()

	frame = tk.Frame(root, bg='#21385b')
	frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
	
	#Place where spawned enemies show up
	enemiesBox = tk.Listbox(frame)
	
	def dos():
		e.spawn(level.get())
		enemiesBox.insert(tk.END, e.enemies[-1].name)
	
	#what level should the spawned enemies be?
	levelScale = tk.Scale(frame, orient=tk.HORIZONTAL, variable = level, from_ = 1, to = 25)
	
	selectedCommand = tk.StringVar()
	selCommand = tk.OptionMenu(frame, selectedCommand, *list(funcDict))
	
	extraString = tk.StringVar()
	extraField = tk.Entry(frame, textvariable=extraString)

	def tres():
		print(enemies,*enemiesBox.curselection(),selectedCommand.get())
		funcDict[selectedCommand.get()](*enemiesBox.curselection(),selectedCommand.get())
	def kill(number):
		name = enemiesBox.get(number)
		print(name,"was KILLED")
		enemiesBox.delete(number)
		return e.kill(name)
	def name():
		return e.enemyNames()
	#button to execute commands
	execButton = tk.Button(frame, text="Execute", command=tres)
	killButton = tk.Button(frame, text="Kill", command = lambda: kill(enemiesBox.curselection()[0]))
	creatButto = tk.Button(frame, text="Spawn", command=dos)
	nameButton = tk.Button(frame, text="List People", command=name)
	# createButton = tk.Button(frame, text="Spawn", command=lambda: spawn(level.get()))
	

	nameButton.grid(column=0, row=0)
	enemiesBox.grid(column=0, row=1)
	selCommand.grid(column=0, row=2)
	execButton.grid(column=0, row=3)
	killButton.grid(column=1, row=0)
	extraField.grid(column=1, row=1)
	levelScale.grid(column=2, row=0)
	creatButto.grid(column=3, row=0)

	root.mainloop()

def sample():
	print("lol")
	return False

uno()