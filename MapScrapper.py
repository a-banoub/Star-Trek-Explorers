import requests
import bs4
import json
import math

filename = 'MapData.json'

currentplanet = 'Sol'

destination = input('Planet to Search?')


with open(filename, "r") as file:
	
	mapdata = json.load(file)
	found = False
	print (mapdata)
	
	for feature in mapdata['features']:
		
		if feature ["properties"] ["name"] == currentplanet:
				print("Found by Name:", feature)
				startingcoords = feature['geometry']['coordinates']
	
	for feature in mapdata['features']:
		
		if feature ["properties"] ["name"] == destination:
			if feature ["properties"] ["subclass"] == 'major':
				
				print("Found by Name:", feature)
				destinationcoords = feature['geometry']['coordinates']
				found = True
				break
		if not found: 
			print('Planet not Found')
			
print ('Starting Coords: ', startingcoords, 'Destination Coords: ', destinationcoords)
			
distance = math.sqrt(
	(destinationcoords[0] - startingcoords[0]) ** 2 +
	(destinationcoords[1] - startingcoords[1]) ** 2
)

print ('Distance = ', distance)