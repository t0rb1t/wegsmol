#!/usr/bin/python3

import csv, sys, os, objectSaver

class weapons:
    def __init__(self, name, damage, wType, handed, idealR, redPerMeter, defDiff):
        self.name = name
        self.wType = wType
        self.handed = 1 if handed == 'TRUE' else 2
        if self.wType == 'Ranged':
            self.ranged(idealR, redPerMeter, defDiff, damage)
        elif self.wType == 'Melee':
            self.damage = int(damage[4:])
        elif self.wType == 'Throwable':
            pass
    def ranged(self, idealR, redPerMeter, defDiff, damage):
        self.damage = int(damage)
        self.idealR = idealR
        self.redPerMeter = eval(redPerMeter)
        self.defDiff = defDiff
    def specs(self):
        #TODO: clean this up, or... try to
        data =     ('This is the          '+self.name+'\n')
        if self.wType == 'Melee':
            data += ('Damage             = '+str(self.damage)+'+Str Roll\n')
        elif self.wType == 'Ranged':
            data +=('Damage             = {damage}\n'
                    'Type               = {wType}\n'
                    'It is                {handed} handed\n'
                    'Default Difficulty = {defDiff}\n'
                    'Ideal Range        = {idealR}\n'
                    'Reduction Amount/m = {redPerMeter}'.format(**self.__dict__))
        return data

def myCsvReader(filename, exporto=True):
    if os.path.isfile(("./pickles/{}.pkl".format(filename[:-4]))):
        filteredWeapons = objectSaver.unPickler(filename[:-4])
    else:
        with open(filename, newline='') as csvfile:
            weaponRead = csv.DictReader(csvfile, delimiter=',')
            filteredWeapons = []
            for i in weaponRead:
                if i['Name'] != '':
                    filteredWeapons.append(i)
        if exporto:
            objectSaver.objPickler(filteredWeapons,filename[:-4])
    return filteredWeapons

def weaponsToClass(wepList):
    newWepList = []
    for i in wepList:
        tempWep = weapons(i['Name'],i['Damage'],i['Type'],i['Single Handed'],i['Ideal range (meters)'],i['Reduction Window'],i['Default Difficulty'])
        newWepList.append(tempWep)
    return newWepList

if __name__ == '__main__':
    filteredWeapons = myCsvReader('weapon-stats.csv')
    classWeapons = weaponsToClass(filteredWeapons)
    for i in classWeapons:
        print(i.specs())
        print()