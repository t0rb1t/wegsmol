#!/usr/bin/python3
import charactergen, names, namegenerator, sys

global funcDict

class enemy:
	"""
	cShade means current shade
	mShade means max shade
	"""
	def __init__(self, level, name, shadeActive=True, weapons=[]):
		self.level = level
		self.name = name
		self.stats, self.mBatt, self.mShade, self.mHealth, self.speed = charactergen.main(level)
		self.cBatt, self.cShade, self.cHealth = self.mBatt, self.mShade, self.mHealth
		self.shadeActive = shadeActive
		self.weapons = weapons
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
			self.cBatt -= 20
	def selfReport(self):
		print(self.name, "has these stats:",self.stats)
		print("Health: ",self.cHealth,"/",self.mHealth)
		print("Shade:  ",self.cShade,"/",self.mShade)
		print("Batt:   ",self.cBatt,"/",self.mBatt)
		print("Speed:  ",self.speed,"meters/turn")
		print("Level:  ",self.level)
		print("Weapons:",self.weapons)

def classTurn(enemies):
	for i in enemies:
		i.turn()

def enemyNames(enemies):
	for i in enemies:
		print(i.name)

def report(enemies, name=None):
	if name == None:
		for i in enemies:
			i.selfReport()
			print()
	else:
		for i in enemies:
			if i.name.lower() == name.lower():
				i.selfReport()
	print()
	return

def attack(enemies, name, damage, kind="physical"):
	for i in enemies:
		if i.name.lower() == name.lower():
			i.damage(int(damage), kind)

def helpMessage(enemies):
	helpFile = open("oopcharacters-commands","r")
	print(helpFile.read())
	return

def isGood(funcDict, listy, state=False):
    if len(listy) <= 0:
        return state, None
    elif len(listy) > 0:
        for i in funcDict:
            if listy[0] in i:
                return True, i
        return isGood(funcDict, listy[1::], False)

def commands(enemies, funcDict):
	#interprets user input, and makes the magic happen
	command = input("> ")
	commList = list(map(str,command.split(" ")))
	# print(commList)
	if 'stop' in commList or 'st' in commList:
		return
	else:
		goodCommand, dictPart = isGood(funcDict, commList)
		if goodCommand:
			try:
				funcDict[dictPart](enemies, *commList[1::])
			except TypeError:
				print("try entering that command again.")
		else:
			print("That doesn't seem to be a valid command. Type ? for help")
	return commands(enemies, funcDict)

def startEncounter(numberOfEnemies, difficulty):
	enemies = []
	for i in range(numberOfEnemies):
		enemies.append(enemy(difficulty, names.get_first_name().lower()))
	enemyNames(enemies)
	return commands(enemies, funcDict)

def main(args):
	if not len(sys.argv) > 1:
		try:
			numberOfEnemies = int(input("how many enemies should there be? > "))
			difficulty = int(input("what level shoul the enemies be? > "))
		except ValueError:
			print("please just type numbers.")
	elif len(sys.argv) == 3:
		numberOfEnemies = int(sys.argv[1])
		difficulty = int(sys.argv[2])
	print("\nenter ? for help\n")
	startEncounter(numberOfEnemies, difficulty)

funcDict = {('attack','a','att'):attack,
			('report','r','rep'):report,
			('help','h',"?"):helpMessage,
			('turn','t'):classTurn,
			('names','n'):enemyNames
			}

if __name__ == "__main__":
	main(sys.argv)
