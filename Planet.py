import uuid
import MapMaker

class planet:
	def __init__(self, name, game):
		planet = self
		self.id = str(uuid.uuid4())
		self.game = game
		max_distance_ly = int ( input ("Max Distance from Current Location"))
		
		self.coords = MapMaker.generate_random_coordinates (max_distance_ly, self.game)
		
		self.properties = {
				"class": "planet",
				"id": self.id,
				"name": name,
				"sub class": "User Created Planet",
				"wiki": None,
				"z": None
		}
		self.geometry ={
			"type": "Point",
			"coordinates": self.coords
		}
	
	