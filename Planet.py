import uuid
import MapMaker
import os
import json

class planet:
	def __init__(self, name, game):
		planet = self
		self.game = game		
		max_distance_ly = int ( input ("Max Distance from Current Location"))

		self.coords = MapMaker.generate_random_coordinates (max_distance_ly, self.game)
		
		self.properties = {
				"class": "planet",
				"id" : str(uuid.uuid4()),
				"name": name,
				"sub class": "User Created Planet",
				"wiki": None,
				"z": None
		}
		self.geometry ={
			"type": "Point",
			"coordinates": self.coords
		}
	
	def saveplanet(self):
		planetlog = os.path.join(self.game.dir, 'MapData.json')
		data = {"Properties": self.properties, "geometry": self.geometry}
		
		if os.path.isfile(planetlog):
			print ("File Exists")
			
			with open(planetlog, "r") as file:
				file_content = file.read()
				planet_data = json.loads(file_content)
				index_to_replace = None
			
			for i, feature in enumerate(planet_data['features']):
				if feature["properties"]["id"] == self.properties['id']:
					index_to_replace = i
					break
				
				if index_to_replace is not None:
					planet_data['features'][index_to_replace] = data
					
				else:
					planet_data['features'].append(data)
				
				with open(planetlog, "w") as file:
					json.dump(planet_data, file)		