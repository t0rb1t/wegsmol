#!/usr/bin/python3

#custom
import namegenerator, charactergen, csvInterp

#system
import sys, random, math

class char:
	def __init__(self, level, name):
		#TODO: Allow people to send in weapons list already.
		self.level = level
		self.name = name
		self.stats, self.mBatt, self.mShade, self.mHealth, self.speed = charactergen.main(level)
		self.weapons = list()
	def weaponize(self, weapList, quantity):
		for i in range(quantity):
			self.weapons.append(random.choice(weapList))
	def utilitize(self, utilList):
		self.utilities = []
	def selfReport(self):
		data = ('{name}\n'
				'Stats   = {stats}\n'
				'Health  = {mHealth}\n'
				'Shade   = {mShade}\n'
				'Batt    = {mBatt}\n'
				'Speed   = {speed} meters/turn\n'
				'Level   = {level}\n'.format(**self.__dict__))
		data += 'Weapons = {}'.format([i.name for i in self.weapons])
		return data

def statgen(level):
	remaining = level+9
	shouldbe = level+15
	ratio = 2
	# print(level, remaining)
	statlist = [1,1,1,1,1,1]
	for i in range(6):
		stat = math.ceil(remaining/ratio) if math.ceil(remaining/ratio) <= 9 else 9
		statlist[i] += stat
		remaining -= stat
	# random.shuffle(statlist)
	if shouldbe != sum(statlist):
		print(statlist, remaining)
		print(sum(statlist), shouldbe)
		print("PANIC! THE NUMBERS DON'T ADD UP")
	if 0 in statlist:
		print("PANIC! THERE IS A 0")
	return statlist

builds = 	{'tank':'emtdsi',
			'technophile':'tmedsi',
			'magic':'imdste'
}


if __name__ == "__main__":
	# print("This is the player character generator")
	# print("You are in interactive mode")
	# level = int(input("What level is your character? > "))
	# build = input("What build? > ")
	level = 24
	stats = statgen(level)
	build = 'magic'
	statDict = {}
	for i in range(6):
		letter = builds[build][i]
		statDict[letter] = stats[i]
	print(statDict)
	# uno, dos, tre = 'm', 't', 'e'
	# statDict = {uno:stats[0], dos:stats[1], tre:stats[2]}
	print(stats, sum(stats))
