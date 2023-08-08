import uuid
import Map

class planet:
	def __init__(self, name):
		planet = self
		self.id = str(uuid.uuid4())
		
		max_distance_ly = int ( input ("Max Distance from Current Location"))
		self.coords = Map.generate_random_coordinates (max_distance_ly)

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