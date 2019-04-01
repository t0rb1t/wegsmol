#!/usr/bin/python3

#custom
import namegenerator, charactergen, csvInterp, objectSaver

#system
import sys, random, math


class char:
	def __init__(self, level, name, stats):
		#TODO: Allow people to send in weapons list already.
		self.level = level
		self.name = name
		self.stats = stats
		self.mShade = 100
		self.mBatt = 10+stats['m']
		self.mHealth = 25+math.ceil(2.5*stats['e'])
		self.speed = 2+math.ceil(stats['d']/5)
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
	statslist = [1,1,1,1,1,1,1]
	statsum = level+9
	for i in range(len(statslist)):
		temp = int(statsum / 2)
		temp = min([temp, 9])
		statsum -= temp
		statslist[i] += temp
	if sum(statslist) != level+15:
		print(level+15, sum(statslist))
	return statslist

builds = 	{'tank':'ewmrdsi',
			'technophile':'emdrwsi',
			'magic':'imrdsew'
}



if __name__ == "__main__":
	if len(sys.argv) == 1:
		print("This is the player character generator")
		print("You are in interactive mode")
		level = int(input("What level is your character? > "))
		build = input("What build? > ")
	elif len(sys.argv) == 3:
		if sys.argv[1] == 'i':
			objectSaver.unPickler(sys.argv[2])
		try:
			level = int(sys.argv[1])
			build = sys.argv[2]
		except ValueError:
			print("something happened that I didn't plan for")
			exit()
	else:
		print("something happened that I didn't plan for")
		exit()
	if build in ('custom', 'other'):
		build = input("order these letters the way you want your stats prioritized\nMISDREW").lower()
	
	stats = statgen(level)
	statDict = {}
	for i in range(len(stats)):
		letter = builds[build][i]
		statDict[letter] = stats[i]
	print(statDict)
	print(stats, sum(stats))
	character = char(level,'len',statDict)