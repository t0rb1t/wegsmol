#!/usr/bin/python3

import csv, sys

with open('weapon-stats.csv', newline='') as csvfile:
    weaponRead = csv.DictReader(csvfile)
    for i in weaponRead:
        if i['Name'] != '':
            # print(i)
            pass
    exWeap = weaponRead[0]