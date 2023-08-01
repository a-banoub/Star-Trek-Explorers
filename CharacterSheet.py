import GUI
import Archetypes


class Character: 
	def __init__(self,name):
		pc = self
		self.name = name
		self.stats = {}
		self.expertise = []
		self.archetype = ""
	
	def add_expertise (self, expertise_name):
		self.expertise = {expertise_name : 1}
	
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