#!/usr/bin/python3

import pickle, csvInterp

def listPickler(theObject, newFileName):
    with open(newFileName, "wb") as pickleFile:
        pickle.dump(theObject, pickleFile)
    return

def unpickler(filename):
    with open(filename, "rb") as pickleFile:
        return pickle.load(pickleFile)

def tempFunc():
    csvAsDict = csvInterp.myCsvReader('weapon-stats.csv')
    weapons = csvInterp.weaponsToClass(csvAsDict)
    return weapons

if __name__ == '__main__':
    filename = "tempDataName.pkl"
    listPickler(*(tempFunc(), filename))
    unpickled = unpickler(filename)
    for i in unpickled:
        print(i.specs())
        print(type(i)==csvInterp.weapons)