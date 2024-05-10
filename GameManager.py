import uuid
import os
import shutil
import ship
import json
import CharacterSheet
import Archetypes
import PDFCreator
import MapMaker

GameStates = [
	'Downtime', 'On Duty', 'Away Mission'
]

gamelog = 'gamelog.json'

class game ():
	def copymapdata(self): 
		source_file = 'MapData.json'
		destination_file = os.path.join (self.dir, source_file)
		shutil.copy(source_file, destination_file)
	def __init__(self, name):
			self.game = self
			self.properties = {
				'Campaign Name': name ,
				'ID' : str(uuid.uuid4()),
				'Characters': [],
				'Current System': 'Sol',
				'Ship' : None,
				'Captain' : None,
				'GameState' : GameStates [0],
				'Explored Planets' : [],
				'Ship' : [],
			}
			self.dir = None
		
	def make_game_directory(self):
		self.dir = os.path.join('Games',self.properties['Campaign Name'])
		os.makedirs(self.dir)
		return self.dir 

	def load_game_data(self, filename, index):
		with open(filename, 'r') as file:
			data = json.load(file)

		try: 
			index = int (index)
		except ValueError: 
			print ("Invalid Index. Please provide a valid index.")
			return
		
		if index < 0 or index >= len(data):
				print ("Invalid Index. Please provide a valid index.")
				return
		
		game_data = data[index]
		self.properties['Campaign Name'] = game_data['Campaign Name']
		self.properties['ID'] = game_data['ID']
		self.properties['Characters'] = game_data['Characters']
		self.properties['Current System'] = game_data['Current System']
		self.properties['Ship'] = game_data['Ship']
		self.properties['Captain'] = game_data['Captain']
		self.properties['GameState'] = game_data['GameState']
		self.properties['Explored Planets'] = game_data['Explored Planets']
		self.dir = os.path.join('Games',self.properties['Campaign Name'])


		print (self.properties)
	
	def savegamedata(self):
		
		data = {
			'Campaign Name' : self.properties['Campaign Name'],
			'ID' : self.properties['ID'],
			'Characters' : self.properties['Characters'],
			'Current System': self.properties['Current System'],
			'Ship' : self.properties['Ship'],
			'Captain' : self.properties['Captain'],
			'GameState' : self.properties['GameState'],
			'Explored Planets' : self.properties['Explored Planets']
		}
		print (data)
		
		
		if os.path.isfile(gamelog):
			print ("File Exists")
			with open(gamelog, "r") as file:
				file_content = file.read()
			
				game_data = json.loads(file_content)
				index_to_replace = None
				
				for i, existing_data in enumerate(game_data):
					if existing_data['ID'] == data['ID']:
						index_to_replace = i
						break
				
				if index_to_replace is not None:
					game_data[index_to_replace] = data
				
				else:
					game_data.append(data)
					
				with open(gamelog, "w") as file:
					json.dump(game_data, file)
							
#			except json.JSONDecodeError:
#				game_data = [data]
#				with open(gamelog, "w") as file:
#					json.dump(game_data, file)
		
		else:
			game_data = [data]
			with open(gamelog, "w") as file:
				json.dump(game_data, file)

	def newpc (self, game):
		CharacterName = input("Character Name: ")

		PlayerCharacter = CharacterSheet.Character(CharacterName, game)	
		print (PlayerCharacter.name)

		species = input ("Species Name: ")
		PlayerCharacter.add_species (species)

		archetype_names = list(Archetypes.archetypes.keys())
		combo = PlayerCharacter.call_combobox_archetype_select(PlayerCharacter, "Choose Archetype", archetype_names)

		print (PlayerCharacter.name)
		print (PlayerCharacter.archetype)
		print (PlayerCharacter.stats)


		PlayerCharacter.save_character()
		print ("PC Saved")

		PDFCreator.mkpdf(PlayerCharacter, game)

	def mainmenu(self, game):
		print ("Characters, Planet Notes, Etc")
		userinput = input ("Prompt")
		
		if userinput == "newpc":
			self.newpc(self)
			self.mainmenu

		if userinput == "planets":
			MapMaker.plotcourse(self.properties['Current System'], self)
			self.mainmenu

		if userinput == "newship":
			shipname = input ("Ship Name?")
			self.properties ['Ship'] = ship.ship (shipname)
			
		else: 
			print ("Command Not Recognized")
			self.mainmenu