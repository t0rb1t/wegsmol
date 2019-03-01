#!/usr/bin/python3

import csv, sys

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
    def specs(self):
        return self.__dict__

def myCsvReader(filename):
    with open(filename, newline='') as csvfile:
        weaponRead = csv.DictReader(csvfile, delimiter=',')
        filteredWeapons = []
        for i in weaponRead:
            if i['Name'] != '':
                filteredWeapons.append(i)
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