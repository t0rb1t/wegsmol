#!/usr/bin/python3

import csv

"""
this doesn't work yet
the spacing is weird with a couple perks
there is no obvious notation that shows the name
"""

csvfile = 'perks.csv'
perkslist = []
tempdict = {'Description':"", 'Requirements':"", 'Cost':"", 'Name':""}
Requirements = 'Requirement: '
Cost = 'Cost: '
Description = 'Description: '


with open("wegsmol-perks.txt", 'r') as file:
	with open('wegsmol-perks.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['Name', 'Requirements', 'Description', 'Cost', 'Name'])
		for line in file:
			if 'Requirement: ' in line:
				tempdict['Requirements'] = line[13::][:-1]
				# print(tempdict['Requirements'])
			elif 'Cost: ' in line:
				tempdict['Cost'] = line[6:]
				# print(tempdict['Cost'])
			elif 'Description: ' in line:
				tempdict['Description'] = line[13::]
				# print(tempdict['Description'])
			elif ' Perks' in line:
				pass
			elif line[0] == "-":
				tempdict['Description'] = tempdict['Description']+" "+line
				# print(tempdict['Description'])
			else:
				tempdict['Name'] = line
				# print(tempdict['Name'])
				perkslist.append(tempdict)
				if tempdict['Name'] != "":
					writer.writerow(tempdict)
# print(tempdict['Cost'], tempdict['Requirements'])

# csv.DictWriter(csvfile)