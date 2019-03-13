#!/usr/bin/python3
import random, sys, math

def first():
	stats = {'s':1, 'm':1, 'i':1, 't':1, 'e':1, 'd':1}
	stats[(random.choice(list(stats)))] += 7
	return stats

def userin(args):
	if len(args)>=2:
		level = int(args[1])
	else:
		level = int(input("What is the level? > "))
	level+=3
	return level

def levelup(stats,level):
	randstat = random.choice(list(stats))
	if level <= 0:
		return stats, level
	elif stats[randstat]>=10:
		# print("oops")
		return levelup(stats,level)
	else:
		stats[randstat]+=1
		return levelup(stats,level-1)

def battmake(stats):
	batt = 100+30*stats['m']
	return batt

def shademake(stats):
	shade = 5*stats['m']+5*stats['e']+50
	return shade

def healthmake(stats):
	health = 25+(math.ceil(2.5*stats['e']))
	return health

def speedmake(stats):
	speed = 5+(math.ceil(0.5*stats['e']))
	return speed

def main(args):
	stats = first()
	if type(args) == list:
		level = userin(args)
	elif type(args) == int:
		level = args
	stats = levelup(stats,level)[0]
	batt = battmake(stats)
	shade = shademake(stats)
	health = healthmake(stats)
	speed = speedmake(stats)
	return stats, batt, shade, health, speed

if __name__ == '__main__':
	stats, batt, shade, health, speed = main(sys.argv)
	if "all" in sys.argv:
		print("The character's stat block is {}".format(list(stats.values())))
		print("They have {} health".format(health))
		print("They have {} shade".format(shade))
		print("They have {} batt".format(batt))
		print("Their shade will last for {} turns if they use no other utils".format(batt/20))

#remember round up is math.ceil(#)