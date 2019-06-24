#!/usr/bin/python3

import csv, sys, os, objectSaver

class weapon:
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

class util:
    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)
        self.Draw = int(self.Draw)
        self.Solo = True if self.Solo == True else False
        # self.Value = int(self.Value[1:-1])
        self.Strain = float(self.Strain)
    def specs(self):
        #TODO: clean this up, or... try to
        data = ('This is the       {Name}\n'
                'Nickname        = {Nickname}\n'
                'Price           = {Value}\n'
                'Draw            = {Draw}\n'
                'Strain          = {Strain}\n'
                'Unintegrated    = {Solo}\n'
                'Purpose         = {Notes}'.format(**self.__dict__))
        return data
        

def myCsvReader(filename, exporto=True):
    if os.path.isfile(("./pickles/{}.pkl".format(filename[:-4]))):
        csvItems = objectSaver.unPickler(filename[:-4])
    else:
        with open(filename, newline='') as csvfile:
            csvRead = csv.DictReader(csvfile, delimiter=',')
            csvItems = []
            for i in csvRead:
                if i['Name'] != '':
                    csvItems.append(i)
        if exporto:
            objectSaver.objPickler(csvItems,filename[:-4])
    return csvItems

def weaponsToClass(wepList):
    newWepList = []
    for i in wepList:
        tempWep = weapon(i['Name'],i['Damage'],i['Type'],i['Single Handed'],i['Ideal range (meters)'],i['Reduction Window'],i['Default Difficulty'])
        newWepList.append(tempWep)
    return newWepList

def utilsToClass(utilList):
    newUtilList = []
    for i in utilList:
        tempUtil = util(**i)
        newUtilList.append(tempUtil)
    return newUtilList

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please put \"weapon\" or \"util\" as an arg")
    else:
        filename = ("{}-stats.csv".format(sys.argv[1]))
    csvItems = myCsvReader(filename)
    if sys.argv[1] == "weapon":
        classed = weaponsToClass(csvItems)
    elif sys.argv[1] == "util":
        classed = utilsToClass(csvItems)
    for i in classed:
        print(i.specs())
        print()