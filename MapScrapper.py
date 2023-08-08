import requests
import bs4
import json

filename = 'MapData.json'

planet = input('Planet to Search?')

with open(filename, "r") as file:
	mapdata = json.load(file)
	found = False
	print (mapdata)
	
	for feature in mapdata['features']:
		
		if feature ["properties"] ["name"] == planet:
			if feature ["properties"] ["subclass"] == 'major':
				print("Found by Name:", feature)

				found = True
				break
		
	if not found: 
		print('Planet not Found')