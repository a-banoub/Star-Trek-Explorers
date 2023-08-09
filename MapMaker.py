import requests
import bs4
import json
import math
import random

filename = 'MapData.json'


distance = 0.0646027555153078

light_years_conversion_distance = 12.6
scaling_factor = light_years_conversion_distance / distance



				
def plotcourse (currentplanet):	
	
	with open(filename, "r") as file:
		
		mapdata = json.load (file)
		found = False
		
		def get_starting_coords(currentplanet): 
			for feature in mapdata['features']:
				if feature ["properties"] ["name"] == currentplanet:
						print("Found by Name:", feature)
						startingcoords = feature['geometry']['coordinates']
						return startingcoords
				else: 
					pass
					
	startingcoords = get_starting_coords(currentplanet)
	destination = input('Planet to Search?')
	for feature in mapdata['features']:
		if feature ["properties"] ["name"] == destination:
			if feature ["properties"] ["subclass"] == 'major':
				print("Found by Name:", feature)
				destinationname = feature['properties'] ['name']
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
	
	distance_ly = distance * scaling_factor
	
	print (destinationname, 'is', distance_ly, 'light years away')
		
	def calculate_travel_time(warp_factor):
		
		c = 3.0 * 10**8  # Speed of light in m/s
		wf = warp_factor
		speed = wf ** (10/3) * c  # Speed in m/s
		distance_meters = distance_ly * (9.461e15)
		travel_time_seconds = distance_meters / speed
		travel_time_days = travel_time_seconds / (24 * 60 * 60)
		
		print ('Warp Factor: ', wf)
		print ('Speed: ', speed)
		print(f'Travel Time: {travel_time_days:.2f} days')

		return travel_time_days
	
	for warp_factor in range(1, 10):
		travel_time = calculate_travel_time(warp_factor)
		if travel_time > 365:
			travel_years = travel_time/365
			print(f"Warp Factor {warp_factor}: Travel Time = {travel_years:.2f} years")
		else: 
			print(f"Warp Factor {warp_factor}: Travel Time = {travel_time:.2f} days")
			
	user_input = input ('Plot a course? Y/N')
		
	if user_input == ('Y'):
		currentplanet = destinationname
		print ('Moved to: ', currentplanet)
		return (currentplanet)
	
	else:
		pass

	
	
	def generate_random_coordinates(max_distance_ly):
		startingcoords = get_starting_coords(currentplanet)
		
		max_distance_m = max_distance_ly * (9.461e15)  # Convert light years to meters
		
		delta_x = random.uniform(-max_distance_m, max_distance_m)
		delta_y = random.uniform(-max_distance_m, max_distance_m)
		new_coords = [
			startingcoords[0] + delta_x,
			startingcoords[1] + delta_y
		]
		return new_coords