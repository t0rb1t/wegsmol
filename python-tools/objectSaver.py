#!/usr/bin/python3

#consider removing csvInterp dependency
import pickle

def objPickler(theObject, newFileName):
    #saves list (theObject) as ./pickles/newFileName
    with open(("./pickles/{}.pkl".format(newFileName)), "wb") as pickleFile:
        pickle.dump(theObject, pickleFile)
    return 

def unPickler(filename):
    #retrieves object data from ./pickles/filename
    with open(("./pickles/{}.pkl".format(filename)), "rb") as pickleFile:
        return pickle.load(pickleFile)

# if __name__ == '__main__':
#     filename = "tempDataName"
#     objPickler(*(tempFunc(), filename))
#     unpickled = unPickler(filename)
#     for i in unpickled:
#         print(i.specs())
#         print(type(i)==csvInterp.weapons)