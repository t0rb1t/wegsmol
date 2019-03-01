#!/usr/bin/python3

import pickle, csvInterp

def objPickler(theObject, newFileName):
    #saves list (theObject) as ./pickles/newFileName
    with open(("./pickles/{}".format(newFileName)), "wb") as pickleFile:
        pickle.dump(theObject, pickleFile)
    return 

def unpickler(filename):
    #retrieves object data from ./pickles/filename
    with open(("./pickles/{}".format(filename)), "rb") as pickleFile:
        return pickle.load(pickleFile)

if __name__ == '__main__':
    filename = "tempDataName.pkl"
    objPickler(*(tempFunc(), filename))
    unpickled = unpickler(filename)
    for i in unpickled:
        print(i.specs())
        print(type(i)==csvInterp.weapons)