#!/usr/bin/python3

import csv, sys

class weapons:
    def __init__(self, name, damage, wType, handed, idealR, redWindow, defDiff):
        self.name = name
        self.damage = damage
        self.wType = wType
        self.handed = 1 if handed == 'TRUE' else 2
        if self.wType == 'Ranged':
            self.ranged(idealR, redWindow, defDiff)
    def ranged(self, idealR, redWindow, defDiff):
        self.idealR = idealR
        self.redWindow = redWindow
    def specs(self):
        return self.__dict__

def myCsvRead(filename):
    with open(filename, newline='') as csvfile:
        weaponRead = csv.DictReader(csvfile, delimiter=',')
        tempWep = []
        filteredWeapons = []
        for i in weaponRead:
            if i['Name'] != '':
                tempWep = weapons(i['Name'],i['Damage'],i['Type'],i['Single Handed'],i['Ideal range (meters)'],i['Reduction Window'],i['Default Difficulty'])
                filteredWeapons.append(tempWep)

    return filteredWeapons
        

if __name__ == '__main__':
    filteredWeapons = myCsvRead('weapon-stats.csv')
    for i in filteredWeapons:
        print(i.specs())