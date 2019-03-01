#!/usr/bin/python3

import pickle, csvInterp

def pickler(theObject):
    return

def tempFunc():
    csvAsDict = csvInterp.myCsvReader('weapon-stats.csv')
    weapons = csvInterp.weaponsToClass(csvAsDict)
    # print([i.__dict__ for i in weapons])
    return weapons

if __name__ == '__main__':
    print(pickler(tempFunc()))