#!/usr/bin/python3
import os
import enMan as e
import tkinter as tk

enemies = []

def uno():
	funcDict = {'report':	e.report,
			'turn':		e.classTurn,
			'save':		e.storeEnemies,
			'weapon':	e.weapon,
			'roll':		e.roll}

	root = tk.Tk()
	level = tk.IntVar()
	
	canvas = tk.Canvas(root, height=700, width=700)
	canvas.grid()
	frame = tk.Frame(root, bg='#21385b', padx=2, pady=2)
	frame.place(relx=0.005, rely=0.005, relwidth=0.99, relheight=0.99)
	
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
		"""
		this function is designed to get the selection from the command box
		and then run the corresponding command
		"""
		print(enemies,*enemiesBox.curselection(),selectedCommand.get())
		if selectedCommand.get() == "report":
			e.report()
		elif selectedCommand.get() == "turn":
			e.classTurn()
		elif selectedCommand.get() == "save":
			e.storeEnemies()
		elif selectedCommand.get() == "weapon":
			pass
		elif selectedCommand.get() == "roll":
			pass
		else:
			funcDict[selectedCommand.get()](*enemiesBox.curselection(),selectedCommand.get())
	
	def attack():
		damage = int(extraString.get())
		number = enemiesBox.curselection()[0]
		name = enemiesBox.get(number)
		print(damage, name)
		e.attack(name, damage)
	
	def kill():
		number = enemiesBox.curselection()[0]
		name = enemiesBox.get(number)
		print(name,"was KILLED")
		enemiesBox.delete(number)
		return e.kill(name)
	
	def name():
		return e.enemyNames()
	
	def listPikl():
		"""
		This allows you to get piclked enemies
		The root part of this function is just creating and drawing the popul
		The fetch function actually grabs the piclke and is SUPPOSED to import it
		But that hasn't been implemented yet
		"""
		def fetch():
			selected = picklesbox.curselection()[0]
			toFetch = picklesbox.get(selected)
			print(toFetch[0:-4])
			e.fetchEnemies(toFetch[0:-4])
		canvas2 = tk.Tk()
		picklesbox = tk.Listbox(canvas2)
		print(os.listdir('./pickles'))

		for i in os.listdir('./pickles'):
			picklesbox.insert(tk.END, i)
		picklesbox.grid(column=0, row=0)
		fetchButton = tk.Button(canvas2, text="Fetch", command=fetch)
		fetchButton.grid(column=0, row=1)
	#button to execute commands

	"""
	These two sections are here to 'design' and place the various elements
	Nothing else is done here really
	"""
	execButton = tk.Button(frame, text="Execute", command=tres)
	killButton = tk.Button(frame, text="Kill", command = kill)
	creatButto = tk.Button(frame, text="Spawn", command=dos)
	nameButton = tk.Button(frame, text="List People", command=name)
	attaButton = tk.Button(frame, text="Attack", command=attack)
	piklButton = tk.Button(frame, text="List Pickles", command=listPikl)

	nameButton.grid(column=0, row=0, padx=2, pady=2)
	enemiesBox.grid(column=0, row=1, padx=2, pady=2)
	selCommand.grid(column=0, row=2, padx=2, pady=2)
	execButton.grid(column=0, row=3, padx=2, pady=2)
	piklButton.grid(column=0, row=4, padx=2, pady=2)
	killButton.grid(column=1, row=0, padx=2, pady=2)
	levelScale.grid(column=2, row=0, padx=2, pady=2)
	creatButto.grid(column=3, row=0, padx=2, pady=2)
	attaButton.grid(column=4, row=0, padx=2, pady=2)
	extraField.grid(column=4, row=1, padx=2, pady=2)

	root.mainloop()

def sample():
	print("lol")
	return False

uno()