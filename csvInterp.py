#!/usr/bin/python3

import csv, sys

class weapons:
    def __init__(self, name, damage, type, handed, idealR, redWindow):
        self.name = name
        self.damage = damage
        self.type = type
        self.handed = handed
        if self.type == 'Ranged':
            self.ranged(self, idealR, redWindow)
    def ranged(self, idealR, redWindow)
        self.idealR = idealR
        self.redWindow = redWindow

with open('weapon-stats.csv', newline='') as csvfile:
    weaponRead = csv.DictReader(csvfile, delimiter=',')
    filteredWeapons = []
    for i in weaponRead:
        if i['Name'] != '':
            filteredWeapons.append(i)
    print(filteredWeapons[1]['Name'])
