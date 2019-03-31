#!/usr/bin/python3

"""
this script is for managing enemies.
that is why it's called enMan, that's short for enemy Manager
Documentation is not great, 
feel free to add documentation and make a pull request
usage:

python3 enMan.py (# of enemies, level of enemies)
"""

#system modules
import sys, time, datetime, random

#custom modules
import charactergen, names, namegenerator, objectSaver, csvInterp

# global funcDict

class enemy:
	"""
	cShade means current shade
	mShade means max shade
	"""
	def __init__(self, level, name, shadeActive=True):
		#TODO: Allow people to send in weapons list already.
		self.level = level
		self.name = name
		self.stats, self.mBatt, self.mShade, self.mHealth, self.speed = charactergen.main(level)
		self.cBatt, self.cShade, self.cHealth = self.mBatt, self.mShade, self.mHealth
		self.shadeActive = shadeActive
		self.weapons = list()
	def damage(self, amount, kind):
		if self.shadeActive is False:
			self.cHealth -= amount
		elif self.cShade > amount:
			self.cShade -= amount
		else:
			amount -= self.cShade
			self.cHealth -= amount
			self.cShade = 0
		print(self.name,"was DAMAGED")
	def turn(self):
		if self.shadeActive:
			self.cBatt -= 2
		if self.cShade < self.mShade:
			self.cShade += min(self.mShade-self.cShade, self.roll('m'))
	def weaponize(self, weapList, quantity):
		for i in range(quantity):
			self.weapons.append(random.choice(weapList))
	def roll(self, stat):
		die = random.randint(1,10)
		result = self.stats[stat] + die
		print(result)
		return result
	def selfReport(self):
		data = ('{name}\n'
				'Stats   = {stats}\n'
				'Health  = {cHealth}/{mHealth}\n'
				'Shade   = {cShade}/{mShade}\n'
				'Batt    = {cBatt}/{mBatt}\n'
				'Speed   = {speed} meters/turn\n'
				'Level   = {level}\n'.format(**self.__dict__))
		data += 'Weapons = {}'.format([i.name for i in self.weapons])
		return data

def classTurn(enemies):
	for i in enemies:
		i.turn()
	return enemies

def enemyNames(enemies):
	for i in enemies:
		print(i.name)
	return enemies

def report(enemies, name=None):
	if name == None:
		for i in enemies:
			print(i.selfReport())
			print()
	else:
		for i in enemies:
			if i.name.lower() == name.lower():
				print(i.selfReport())
	print()
	return enemies

def attack(enemies, name, damage, kind="physical"):
	for i in enemies:
		if i.name.lower() == name.lower():
			i.damage(int(damage), kind)
	return enemies

def storeEnemies(enemies, filename=datetime.datetime.now().strftime("%y-%m-%d-%H-%M")):
	#TODO: It's storing the wrong one or something?
	single = False
	for i in enemies:
		if i.name == filename:
			print(i.name)
			single = True
			theEnemy = i
	if single:
		objectSaver.objPickler([theEnemy], filename)
	elif not single:
		objectSaver.objPickler(enemies, filename)
	return enemies

def fetchEnemies(enemies, filename, mode='add'):
	#TODO: ENSURE THAT IMPORTED ENEMIES AREN'T DUPED NAMES
	storedenemies = objectSaver.unPickler(filename)
	if mode == "replace":
		return storedenemies
	elif mode == "add":
		enemies += storedenemies
		return enemies

def kill(enemies, name):
	if name == 'all':
		return []
	for i in enemies:
		if i.name == name:
			enemies.remove(i)
	return enemies

def spawn(enemies, level):
	#TODO: Ensure that there are no name dupes!!!
	try:
		level = int(level)
	except ValueError:
		level = int(input("what level should the new enemy be? > "))

	name = names.get_first_name().lower()
	while name in [i.name for i in enemies]:
		name = names.get_first_name().lower()
	newEnemy = enemy(level, name)
	enemies.append(newEnemy)
	print(newEnemy.name,"was spawned")
	return enemies

def weapon(enemies, mode, name=None, filename='weapon-stats.csv'):
	tempWep = csvInterp.myCsvReader(filename)
	weapList = csvInterp.weaponsToClass(tempWep)
	if mode=='all':
		for i in enemies:
			i.weaponize(weapList, 2)
	elif mode=='single':
		#TODO: finish this
		pass
	return enemies

def helpMessage(enemies):
	helpFile = open("enMan-commands","r")
	print(helpFile.read())
	return enemies

def commands(enemies, funcDict):
	def isGood(funcDict, listy, state=False):
		if len(listy) <= 0:
			return state, None
		elif len(listy) > 0:
			for i in funcDict:
				if listy[0] in i:
					return True, i
			return isGood(funcDict, listy[1::], False)
	#interprets user input, and makes the magic happen
	command = input("> ")
	commList = list(map(str,command.split(" ")))
	# print(commList)
	if 'stop' in commList:
		return
	else:
		goodCommand, dictPart = isGood(funcDict, commList)
		if goodCommand:
			try:
				# print(*commList[1::])
				enemies = funcDict[dictPart](enemies, *commList[1::])
			except TypeError:
				print("try entering that command again.")
		else:
			print("That doesn't seem to be a valid command. Type ? for help")
	return commands(enemies, funcDict)

def startEncounter(numberOfEnemies, level):
	enemies = []
	for i in range(numberOfEnemies):
		spawn(enemies, level)
	return commands(enemies, funcDict)

def main(args):
	if len(sys.argv) == 2:
		numberOfEnemies, difficulty = 0, 0
	elif len(sys.argv) <= 1:
		try:
			numberOfEnemies = int(input("how many enemies should there be? > "))
			if numberOfEnemies > 0:
				difficulty = int(input("what level should the enemies be? > "))
			else:
				difficulty = 0
		except ValueError:
			print("please just type numbers.")
			return main(args)
	elif len(sys.argv) == 3:
		numberOfEnemies = int(sys.argv[1])
		difficulty = int(sys.argv[2])
	print("\nenter ? for help\n")
	startEncounter(numberOfEnemies, difficulty)

funcDict = {('attack', 'a', 'att'):attack,
			('report', 'r', 'rep'):report,
			('help', 'h', "?"):helpMessage,
			('turn', 't'):classTurn,
			('names', 'name', 'n', 'ls'):enemyNames,
			('save', 'store', 's'):storeEnemies,
			('fetch', 'f', 'retreive'):fetchEnemies,
			('kill', 'k'):kill,
			('spawn', 'sp'):spawn,
			('weapon', 'w', 'we'):weapon
			}

if __name__ == "__main__":
	main(sys.argv)
