import GUI
import Archetypes
import json
import uuid
import os

class Character: 
	def __init__(self,name, game):
		pc = self
		self.name = name
		self.stats = {}
		self.expertise = {
			'expertise1': 1
		}
		self.archetype = ""
		self.id = str(uuid.uuid4())
		self.game = game
		
	def add_species (self, species):
            self.species = species
	
#	def add_expertise (self, expertise_name):
#		self.expertise.append ({expertise_name : 1})
	
	def call_combobox_archetype_select (self, pc, title, values):
		self.combobox = GUI.combobox(pc, title, values)
		self.combobox.call()
	
	def call_combobox_stat_select (self, pc, title, archetype):
		self.combobox = GUI.combobox_1 (pc, title, archetype)
		self.combobox.call()
		
	def set_archetype(self, archetype):
		self.archetype = archetype
		return (self.archetype)
		print ("Character Archetype: ", self.archetype )
		
	def set_stats(self, stats):
		self.stats = stats
		print (self.name, self.stats)
		return self.stats
		
	def save_character(self):
		data = {
			'name': self.name,
			'stats': self.stats,
			'archetype' : self.archetype,
			'expertise': self.expertise,
			'id': self.id
		}
		
		filename = os.path.join (self.game.dir , "CharacterDatabase.json")
		
		if os.path.isfile (filename):
			print ("File Exists")
			with open (filename, "r") as file:
				characters_data = json.load(file)
				characters_data.append(data)
			with open (filename, "w") as file:
				json.dump(characters_data, file)
		else: 
			print ("File does not exist")
			with open (filename, "w") as file:
				json.dump([data], file)
			
